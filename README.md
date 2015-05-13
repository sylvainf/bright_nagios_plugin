# Bright nagios plugin
A nagios NRPE based plugin for Bright Cluster Manager

This plugin is using the Bright Computing pythoncm API.

#### INSTALLATION ####
  * Edit your Nrpe.conf file :
```
command[brtnagioso]=/usr/lib64/nagios/plugins/brtnagios.py -o
command[brtnagiosd]=/usr/lib64/nagios/plugins/brtnagios.py -d
command[brtnagiosw]=/usr/lib64/nagios/plugins/brtnagios.py -w
```

  * Copy your Cluster certificate in a place readable by NGIOS/NRPE daemon
  * Copy plugin in your nagios plugin directory and edit the path to certificates
