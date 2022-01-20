#!/usr/local/bin/python3
import os
import re
import argparse

parser = argparse.ArgumentParser(description='Deploy Remote site. and custom label')
parser.add_argument('-o', '--org', dest="usr_org", help="Specify org name to deploy remote site settings.", required=True)
args = parser.parse_args()

Org = args.usr_org  # Storing the users org.


def capture_instance_url(org_name):  # Capturing Instance URL  current org's instance_url.
    stream = os.popen('cci org info {}'.format(org_name)).read()  # Running Command to display our instance url.
    re_instance_url = re.search("(instance_url).+(https.+m)", stream)  # Regex that captures our instance.
    instance_url = re_instance_url.group(2)
    return instance_url


def create_deploy_directory(directory_path, file_path, xml_data, filename):
    path = os.path.join(directory_path, file_path)
    try:
        os.makedirs(path)
    except FileExistsError:
        # directory already exists
        pass

    with open("{}{}".format(path, filename), "w") as f:
        f.write(xml_data)


deploy_data = capture_instance_url(Org)

remote_site_xml = """<?xml version="1.0" encoding="UTF-8"?>
<RemoteSiteSetting xmlns="http://soap.sforce.com/2006/04/metadata">
    <disableProtocolSecurity>false</disableProtocolSecurity>
    <isActive>true</isActive>
    <url>{}</url>
</RemoteSiteSetting>

""".format(deploy_data)


custom_label_xml = """<?xml version="1.0" encoding="UTF-8"?>
<CustomLabels xmlns="http://soap.sforce.com/2006/04/metadata">
    <labels>
        <fullName>{}</fullName>
        <language>en_US</language>
        <protected>false</protected>
        <shortDescription>{}</shortDescription>
        <value>{}</value>
    </labels>
</CustomLabels>
""".format("Domain_Base", "Domain_Base", deploy_data)

# Setting up file path and xml file name.
RSS_xml_file = "sfdo_trusted_site.remoteSite-meta.xml"
custom_label_file = "CustomLabels.labels-meta.xml"

deploy_dir, RSS_deploy_path = "sfdo_temp/", "remoteSiteSettings/"
custom_label_path = "labels/"

create_deploy_directory(deploy_dir, RSS_deploy_path, remote_site_xml, RSS_xml_file)
create_deploy_directory(deploy_dir, custom_label_path, custom_label_xml, custom_label_file)


# flows:
# -deploy_remote_site:
# --description: Add our site into our remote site list.
# --steps:
# ---1:
# ----task: command
# ----options:
# -----command: ./remote_site_script.py --org dev
# ---2:
# ----task: deploy_pre
# ----options:
# -----path: sfdo_temp/
