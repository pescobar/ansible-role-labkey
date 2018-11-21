[![Build Status](https://travis-ci.org/pescobar/ansible-role-labkey.svg?branch=master)](https://travis-ci.org/pescobar/ansible-role-labkey)
[![Ansible Galaxy](https://img.shields.io/badge/galaxy-pescobar.labkey-blue.svg)](https://galaxy.ansible.com/pescobar/labkey)

pescobar.labkey
=========

Installs a labkey server


Role Variables
--------------

Register [here](https://www.labkey.com/products-services/labkey-server/download-community-edition/) to obtain
the download URL


```
labkey_tarball_url: "http://labkey.s3.amazonaws.com/downloads/general/r/18.3/LabKey18.3-61163.720-community-bin.tar.gz"

labkey_install_folder: "/opt"

labkey_user: "labkey"
labkey_group: "labkey"

labkey_db_name: "labkey"
labkey_db_user: "labkeydbuser"
labkey_db_pass: "labkeydbpass"

labkey_smtp_host: "smtp.example.com"
labkey_smtp_user: ""
labkey_smtp_port: 25

labkey_domain: "{{ ansible_fqdn }}"

# should we install the epel-rpm which provides the epel repos?
# or this is already provided in a different way? e.g. Katello
install_epel_rpm: True
```

Dependencies
------------

- [pescobar.postgres](https://galaxy.ansible.com/pescobar/postgres)
- [pescobar.tomcat](https://galaxy.ansible.com/pescobar/tomcat)


Example Playbook
----------------

    - hosts: servers
      roles:
         - { role: pescobar.labkey,
	     tomcat_user: "labkey",
	     tomcat_group: "labkey",
	     postgres_user_to_create: "labkeydbuser",
	     postgress_user_password: "labkeydbpass",
	     postgres_db_to_create: "labkey"}

License
-------

GPLv3

Author Information
------------------

Pablo Escobar Lopez
