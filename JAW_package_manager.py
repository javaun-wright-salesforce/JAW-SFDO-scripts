#!/usr/local/bin/python3
import yaml
import urllib.request
import pprint

# Read/Wrrite managed and unmanaged packages in cumulus.yml file.

test_yml = "https://raw.githubusercontent.com/GeekStewie/universities/master/test.yml"

def get_yml_pkg(yml_url): # return a dictionary with package information from a url
    captured_yml =  urllib.request.urlopen(yml_url)
    '''Capture package section in cumulus.yml'''
    return yaml.safe_load(captured_yml)
    

raw_yml = get_yml_pkg(test_yml)
pprint.pprint(raw_yml)
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


## Resources:
# test yml: https://raw.githubusercontent.com/GeekStewie/universities/master/test.yml
# urllib module: https://www.geeksforgeeks.org/python-urllib-module/
# Python YAML: https://pyyaml.org/wiki/PyYAMLDocumentation