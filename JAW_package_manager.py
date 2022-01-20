#!/usr/local/bin/python3
import yaml
import urllib.request
import pprint
import argparse

# Running cumulus task to update dependencies.
parser = argparse.ArgumentParser(description='Update cumulus package dependency.')
parser.add_argument('-u', '--url', dest="github_url", help="Github url to package dependency xml.", required=True)
args = parser.parse_args()

url_yml = args.github_url  # Storing the users org.
CUMULUS_File = "cumulusci.yml"

test_yml = "https://raw.githubusercontent.com/GeekStewie/universities/master/test.yml"  # yml package
TEST_FILE = 'test_cumulus.yml'


def load_in_github_dependency(yml_url):  # return a dictionary with package information from a url.
    """captures dependency yml from github"""
    captured_yml = urllib.request.urlopen(yml_url)
    return yaml.safe_load(captured_yml)


def rewrite_dependency_yml(dependency_data):
    """rewriting key-value pairs in dependency yml"""
    comment_section = {"dependencies": {}}
    for i in dependency_data['project']['dependencies']:
        for k, v in i.items():
            comment_section['dependencies'].update({k: v})
    return comment_section


def load_in_cumulus_yml():
    """capturing and storing cumulus file yml"""
    with open(CUMULUS_File, 'r') as f:
        cumulus_yml = yaml.safe_load(f)
        return cumulus_yml


def update_cumulus_yml(cumulus_yml, dependency_data):
    """Writing dependency data into project section"""
    cumulus_yml['project'].update(dependency_data)
    return cumulus_yml


# Compare dependency section against partner list, use comment as flag 
def write_yml_pkg(yml_file, yml_data):  # Add dependency data to cumulus.yml file
    """Writing updated cumulus file"""
    with open(yml_file, "w") as f:
        '''Updating cumulus.yml with github dependencies'''
        yaml.dump(yml_data, f, sort_keys=False)


github_dependency_yml = load_in_github_dependency(url_yml)

updated_dependencies = rewrite_dependency_yml(github_dependency_yml)
pprint.pprint(updated_dependencies)

cumulus_data = load_in_cumulus_yml()

updated_cumulus_yml = update_cumulus_yml(cumulus_data, updated_dependencies)

# TODO -- replace testfile with cumulus file
write_yml_pkg(CUMULUS_File, updated_cumulus_yml)
# write_yml_pkg('jaw_test_dependencies.yml', github_dependency_yml)

# Notes section:

# Questions:
# - How do i store a list of packages externally?
# -- YML File hosted on github
#
#
# - How can I check for dependencies?
# -- The update_dependencies task


# Resources:
# test yml: https://raw.githubusercontent.com/GeekStewie/universities/master/test.yml
# urllib module: https://www.geeksforgeeks.org/python-urllib-module/
# Python YAML: https://pyyaml.org/wiki/PyYAMLDocumentation

# task:  https://cumulusci.readthedocs.io/en/latest/tasks.html?highlight=update_dependencies#update-dependencies

# update_dependencies task
# update_dependencies:
#   options:
#     dependencies:


# Flows
# flows:
# deploy_remote_site:
# description: Add our site into our remote site list.
# steps:
# 1:
# create_remote_site_path:
# class_path: cumulusci.tasks.command.Command
# options:
# command: ./remote_site.py
# 2:
# deploy_site:
# class_path: cumulusci.tasks.salesforce.DeployBundles
# options:
# path: sfdo_temp/
