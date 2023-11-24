from setuptools import setup

setup(
   name='datashell',
   version='0.0',
   description='A package to checks csv files from the command line.',
   author='Haddon',
   author_email='hadsand95@gmail.com',
   packages=['datashell'],  #same as name
   install_requires=['pandas']
)