import utils 
import sys
import re

def main():
    # Exit if user fails proper argument supply:
    if len(sys.argv) < 2:
        print("At least two arguments are required. See documentation for more detail.")
        sys.exit(1)

    # Sys args:
    sys1 = sys.argv[1]

    # Regex helpers:
    csv_exp = re.compile(r".csv$")

    # Sequence of terminal arguments & functions:
    if sys1 == "dir":
        print(dir(utils.DataChecker))

    if csv_exp.search(sys1):
        instance = utils.DataChecker(sys1)

        if len(sys.argv) < 3:
            print("If user supplies a csv file, another argument must be supplied to terminal.")

        if sys.argv[2] == "minimalPrimaryKey":
            print(instance.minimalPrimaryKey())
        
        elif sys.argv[2] == "rowsDuplicated":
            print(instance.rowsDuplicated())
        
        elif sys.argv[2] == "describeData":
            print(instance.describeData())

        elif sys.argv[2] == "columnNames":
            print(instance.columnNames())

        elif sys.argv[2] == "checkNPI":
            npi = input("NPI Column: ")
            print(instance.checkNPI(npi))

        elif sys.argv[2] == "checkMPN":
            mpn = input("MPN Column: ")
            print(instance.checkMPN(mpn)) 
        else:
            print(f'"{sys.argv[2]}" argument not recognized')

if __name__ == "__main__":
    main()

