# JAW-SFDO-scripts


Scripts
Remote site script:

This scipt utilizes the remote site settings to deploys our orgs instance URL into our trusted sites.

Remote site script file

The script removes extra step for SE’s after they install certain packs or add certain configurations which require the orgs own URL to be added as a trusted remote site.

This support NxDO builds which need to to set this when orgs are built or whenever a MIDO pack has a lightning component that runs in Experience Cloud or externally. Since the IDO “hosts” the component, so we need to be able to set it.


Package manager script:

This program writes a remote package dependency into the projects Cumulusci file. Provide using a url 

Run command:
./JAW_package_manager.py --url <Github URL>