#!/usr/local/bin/python3
import os
import re
import argparse


parser = argparse.ArgumentParser(description='Deploy Remote site.')
parser.add_argument('-o', '--org', dest="usr_org", help="Specify org name to deploy remote site settings.")
args = parser.parse_args()

Org = args.usr_org  # Storing the users org.


def capture_instance_url(org_name): # Capturing Instance URL  current orgs instance_url.
    stream = os.popen('cci org info {}'.format(org_name)).read() # Running Command to display our instance url.

    re_instance_url = re.search("(instance_url).+(https.+m)", stream) # Regex that captures our instance.
    instance_url = re_instance_url.group(2)
    return instance_url
    

def create_deploy_directory(directory_path, xml_path, remote_site_xml):
    try:
        os.makedirs(directory_path)
    except FileExistsError:
        # directory already exists
        pass

    with open(xml_file_path, "w") as f:
        f.write(remote_site_xml)


deploy_data = capture_instance_url(Org)

xml_data = """<?xml version="1.0" encoding="UTF-8"?>
<RemoteSiteSetting xmlns="http://soap.sforce.com/2006/04/metadata">
    <disableProtocolSecurity>false</disableProtocolSecurity>
    <isActive>true</isActive>
    <url>{}</url>
</RemoteSiteSetting>
""".format(deploy_data) 

# Setting up file path and xml file name.
deploy_directory_path = "sfdo_temp/remoteSiteSettings"
xml_file = "sfdo_trusted_site.remoteSite-meta.xml"
xml_file_path = "{}/{}".format(deploy_directory_path, xml_file)

create_deploy_directory(deploy_directory_path, xml_file_path, xml_data)
os.popen( "cci task run deploy_pre --path sfdo_temp/ --org {}".format(Org)) # cci task run deploy_pre --path sfdo_temp/ --org dev

# Notes

# OS file path for temp dir: /Users/javaun.wright/workspace/projects/JAW_work/jaw_nonprofit/sfdo_temp/remoteSiteSettings

# Pre-req - pass in org name as argument variable.

# 1. Generate xml data into temp folder: ./sfdo_temp/remoteSiteSettings/ 
# 2. rename xml : LabelHere.remoteSite-meta.xml # LabelHere = any name
# 3. cci task run deploy --path force-app --org OrgNameHere #-- Point deploy to this folder.


# Notes May need package.xml file - incase reading error.
#   cci task run update_package_xml --path sfdo_temp/ --org dev


