import pandas as pd
import re
from itertools import combinations

class DataChecker:
    def __init__(self, data: str):
        self.__data = pd.read_csv(data)
    
    @property
    def data(self):
        return self.__data
    
    @data.setter
    def data(self, data):
        if not isinstance(data, pd.DataFrame):
            raise TypeError(f"{data} must be a string")

        self.__data = data
        
    def __str__(self):
        return f"DataChecker object with {self.data} attached"

    # Return Column Names:
    def columnNames(self):
        dataColumns = self.data.columns
        return dataColumns
    
    # Sum of duplicate rows:
    def rowsDuplicated(self):
       dupeRows = self.data.duplicated().sum()
       return dupeRows
   
    # Algorithm to return a minimally sufficient primary key
    def minimalPrimaryKey(self):
        
        # Iterate over all possible sizes of combinations 
        # (from 1 to the number of columns + 1 since Python stops at index
        # before right limit)
        for n in range(1, len(self.data.columns)+1):
            
            # Iterate over all combinations of columns of size n
            for c in combinations(self.data.columns, n):
                
                # Check if there are no duplicated rows in the subset of columns
                if not self.data[list(c)].duplicated().any() and not self.data[list(c)].isnull().any().any():
                     minimalKey = self.data[list(c)].columns
                     print(f'A minimal primary key found: {", ".join(str(col) for col in minimalKey)}')
                     return minimalKey
                elif n == len(self.data.columns):
                     print("No primary key identified")
    
    # Check format of NPI
    def checkNPI(self, columnName):
        if columnName not in self.data.columns:
            return f'{columnName} not found'
        
        # Print a pseudo-error if missing data is found
        if self.data[columnName].isnull().any() == True:
            raise ValueError(f'Execution halted: Missing data found in {columnName}')
        
        # Retrieve User-Identified NPI column:
        npiVals = self.data[columnName].astype(str)
        
        # Check regular exp
        if all(re.match(r'^\d{10}$', string) and len(string) == 10 for string in npiVals):
            return "Valid"
        else:
            return "Invalid"
        
    # Check format of MPN
    def checkMPN(self, columnName):
        if columnName not in self.data.columns:
            return f'{columnName} not found'
        
        if self.data[columnName].isnull().any() == True:
            raise ValueError(f'Execution halted: Missing data found in {columnName}')
        
        # Retrieve User-Identified MPN column:
        mpnVals = self.data[columnName].astype(str)
        
        # Check regular exp
        if all(re.match(r'^\d{6}$', string) and len(string) == 6 for string in mpnVals):
            return "Valid"
        else:
            return "Invalid"
        
    # Describe Data
    def describeData(self, columnName = None):
        if columnName is None:
            return self.data.describe()
        else:
            return self.data[columnName].describe()
        

def main():
    data = input("CSV file: ")
    data_checker = DataChecker(data)
    return data_checker.minimalPrimaryKey()

if __name__ == "__main__":
    main()