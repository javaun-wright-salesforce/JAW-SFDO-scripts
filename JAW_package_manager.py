#!/usr/local/bin/python3

import yaml
import urllib.request
import pprint
# Running cumulus task to update dependencies.

test_yml = "https://raw.githubusercontent.com/GeekStewie/universities/master/test.yml"  # yml package
filename = 'jaw_test_dependencies.yml'


def get_yml_pkg(yml_url):  # return a dictionary with package information from a url.
    captured_yml = urllib.request.urlopen(yml_url)
    '''Capture package section in cumulus.yml'''
    return yaml.safe_load(captured_yml)


def load_cumulus_yml():
    with open('cumulusci.yml', 'r') as f:
        cumulus_yml = yaml.safe_load(f)
        return cumulus_yml


def update_cumulus_file(yml_data, dependency_data):
    yml_data['tasks']['update_dependencies']["options"] = dependency_data['project']['dependencies']


def write_yml_pkg(yml_file, yml_data):  # Add dependency data to cumulus.yml file
    with open(yml_file, "w") as f:
        '''Updating cumulus.yml with github dependencies'''
        f.write(yaml.safe_dump(yml_data))


raw_yml = get_yml_pkg(test_yml)
cumulus_data = load_cumulus_yml()
update_cumulus_file(cumulus_data, raw_yml)
write_yml_pkg('filename.yml', cumulus_data)


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
