#!/usr/local/bin/python3
from os import read
import re
import yaml
import urllib.request
import pprint
# Running cumulus task to update dependencies.


test_yml = "https://raw.githubusercontent.com/GeekStewie/universities/master/test.yml"  # yml package
filename = 'jaw_test_dependencies.yml'
CUMULUS_File = "cumulusci.yml"


def get_yml_pkg(yml_url):  # return a dictionary with package information from a url.
    '''Capture package section in cumulus.yml'''
    captured_yml = urllib.request.urlopen(yml_url)
    return yaml.safe_load(captured_yml)


def load_cumulus_yml():
    with open(CUMULUS_File, 'r') as f:
        cumulus_yml = yaml.safe_load(f)
        return cumulus_yml


def update_cumulus_file(cumulus_yml, dependency_data):
    cumulus_yml['tasks'].update({"update_dependencies": {"options":[dependency_data['project']]}})
    updated_cumulus = {'project': {"project":cumulus_yml['project']}, 
                        'tasks': {"tasks":cumulus_yml['tasks']}, 
                        'flows': {"flows":cumulus_yml['flows']}}
    return updated_cumulus


    # cumulus_yml['tasks']['update_dependencies']["options"] = dependency_data['project']['dependencies']


def write_yml_pkg(yml_file, yml_data):  # Add dependency data to cumulus.yml file
    with open(yml_file, "w") as f:
        '''Updating cumulus.yml with github dependencies'''
        # f.write(yaml.safe_dump(yml_data))

        f.write(yaml.safe_dump(yml_data['project']))
        f.write(yaml.safe_dump(yml_data['tasks']))
        f.write(yaml.safe_dump(yml_data['flows']))


def find_and_replace(file, dependency_data, regex):
    '''Use regex to search for project section, and append dependency dictionary'''
    with open(file, 'w'):
        for line in file:
            re.search(regex, line)


github_dependency_ymal = get_yml_pkg(test_yml)

cumulus_data = load_cumulus_yml()

updated_cumulus_ymal = update_cumulus_file(cumulus_data, github_dependency_ymal)

# write_yml_pkg('filename.yml', updated_cumulus_ymal)



#TODO: See if we can rewrite ymal dictionaries back in the same order they were read in.
# - Order: cumulus_data.get('project'), cumulus_data['tasks'], cumulus_data['flows']

#TODO: Use regular expresion to find the  section in cumulus.yml (use a comment to flag spot).
# - Either create a custom  'update_dependencies' task in the task section or add dependencies to the top of the file.
#

pprint.pprint(cumulus_data)
# ---------------------

# command: "cci task run update_dependencies --dependencies test.yml"
# Notes section:


# Questions:
# - How do i store a list of packages externally?
# -- YML File hosted on github
#
# - What does DynamicDependency class in cumulus do?
#
# - How can I check for dependencies?
# -- The update_dependencies task

## Resources:
# test yml: https://raw.githubusercontent.com/GeekStewie/universities/master/test.yml
# urllib module: https://www.geeksforgeeks.org/python-urllib-module/
# Python YAML: https://pyyaml.org/wiki/PyYAMLDocumentation
# update_dependencies:  https://cumulusci.readthedocs.io/en/latest/tasks.html?highlight=update_dependencies#update-dependencies



# update_dependencies task  
# update_dependencies:
#   options:
#     dependencies: