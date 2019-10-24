[![Build Status](https://travis-ci.org/pescobar/ansible-role-labkey.svg?branch=master)](https://travis-ci.org/pescobar/ansible-role-labkey)
[![Ansible Galaxy](https://img.shields.io/badge/galaxy-pescobar.labkey-blue.svg)](https://galaxy.ansible.com/pescobar/labkey)

pescobar.labkey
=========

Installs a labkey server in Centos7

This role will install postgres + Java (openjdk) + Apache tomcat + labkey

You should configure Apache or Nginx (or any other reverse proxy) outside of this role (see examples).


Role Variables
--------------

Register [here](https://www.labkey.com/products-services/labkey-server/download-community-edition/) to obtain
the download URL


```
labkey_tarball_url: "http://labkey.s3.amazonaws.com/downloads/general/r/18.3/LabKey18.3-61163.720-community-bin.tar.gz"

labkey_install_folder: "/opt"

labkey_user: "labkey"
labkey_group: "labkey"

# use the default value "ROOT.xml" if you plan to access labkey in the root url e.g. http://domain.com
# define this var to a custom name e.g. "labkey.xml" if you plan to access labkey in a sub-url like http://domain.com/labkey
labkey_config_file: "ROOT.xml"

labkey_db_name: "labkey"
labkey_db_user: "labkeydbuser"
labkey_db_pass: "labkeydbpass"

labkey_smtp_host: "smtp.example.com"
labkey_smtp_user: ""
labkey_smtp_port: 25

labkey_domain: "{{ ansible_fqdn }}"

# should we install the epel-rpm which provides the epel repos?
# or this is already provided in a different way? e.g. Katello
labkey_install_epel_repo: True
```

Dependencies
------------

- [anxs.postgresql](https://galaxy.ansible.com/ANXS/postgresql)
- [pescobar.apache_tomcat](https://galaxy.ansible.com/pescobar/apache_tomcat)


Example Playbook installing only tomcat + labkey (no reverse proxy)
----------------
```
- name: Configure labkey
  hosts: webserver
  gather_facts: True
  remote_user: root

  tasks:

    - name: Deploy labkey server
      import_role:
        name: pescobar.labkey
      vars:
        labkey_domain: "{{ ansible_fqdn }}"
        labkey_install_folder: "/opt"
        labkey_user: "labkey"
        labkey_group: "labkey"
        labkey_db_name: "labkey"
        labkey_db_user: "labkeydbuser"
        labkey_db_pass: "labkeydbpass"
        labkey_smtp_host: "smtp.example.com"
        labkey_smtp_user: ""
        labkey_smtp_password: ""
        labkey_smtp_from: ""
        labkey_smtp_port: 25
```

Example Playbook with apache as reverse proxy
-------------------

```
- name: Configure labkey
  hosts: webserver
  gather_facts: True
  remote_user: root

  tasks:
    
    - name: Deploy LabKey
      import_role:
        name: pescobar.labkey
      vars:
        labkey_domain: "{{ ansible_fqdn }}"
        labkey_install_folder: "/opt"
        labkey_user: "labkey"
        labkey_group: "labkey"
        labkey_db_name: "labkey"
        labkey_db_user: "labkeydbuser"
        labkey_db_pass: "labkeydbpass"
        labkey_smtp_host: "smtp.example.com"
        labkey_smtp_user: ""
        labkey_smtp_password: ""
        labkey_smtp_from: ""
        labkey_smtp_port: 25

    - name: Deploy apache webserver as reverse proxy
      import_role:
        name: geerlingguy.apache
      vars:
        apache_vhosts:
          - servername: "{{ labkey_domain }}"
            serveralias: "www.{{ labkey_domain }}"
            serveradmin: "foo@bar.com"
            documentroot: "/var/www/html"
            extra_parameters: |

              ProxyRequests Off
              ProxyPreserveHost On

              <Proxy *>
                  Order deny,allow
                  Allow from all
              </Proxy>

              ProxyPass / http://localhost:8080/ retry=1
              ProxyPassReverse / http://localhost:8080/
```          

License
-------

GPLv3

Author Information
------------------

Pablo Escobar Lopez
