#!/usr/local/bin/python3
import os
import re
import argparse

parser = argparse.ArgumentParser(description='Deploy Remote site.')
parser.add_argument('-o', '--org', dest="usr_org", help="Specify org name to deploy remote site settings.")
args = parser.parse_args()

Org = args.usr_org  # Storing the users org.


def capture_instance_url(org_name):  # Capturing Instance URL  current org's instance_url.
    stream = os.popen('cci org info {}'.format(org_name)).read()  # Running Command to display our instance url.
    re_instance_url = re.search("(instance_url).+(https.+m)", stream)  # Regex that captures our instance.
    instance_url = re_instance_url.group(2)
    return instance_url


def create_deploy_directory(directory_path, xml_path, remote_site_xml):
    try:
        os.makedirs(directory_path)
    except FileExistsError:
        # directory already exists
        pass
    with open(xml_path, "w") as f:
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



# flows:
    # deploy_remote_site:
        # description: Add our site into our remote site list.
        # steps:
            # 1:
                # task: command
                # options:
                # command: ./remote_site_script.py --org dev
            # 2:
                # task: deploy_pre
                # options:
                # path: sfdo_temp/
