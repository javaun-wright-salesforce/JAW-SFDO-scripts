#!/usr/local/bin/python3
import os
import re
import argparse
# import cumulusci.core.dependencies.dependencies

CUMULUS_file = 'cumulus.yml'
# Read/Wrrite managed and unmanaged packages in cumulus.yml file.

def get_cumulus_pkg(): # return a dictionary with package information
    '''Capture package section in cumulus.yml'''
    with open(CUMULUS_file, 'r') as f:
        print(f)





# Notes section:

## Topics to review 
# - cumulusci repo, DynamicDependency class

## Steps:
# 1. Recieve URL with pkg data file.yml (hosted on github)
# 2. Store packages info as a dictionary
# 4. run the update_dependencies task and use the --dependencies arg.

## Questions:
# - How do i store a list of packages externally?
# -- YML File hosted on github 
#
# - What does DynamicDependency class in cumulus do?
#
#
# - How can I check for dependencies?
# -- The update_dependencies task 
