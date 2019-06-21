import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_opt_labkey(host):
    f = host.file('/opt/labkey')
    assert f.is_symlink
    assert f.exists


def test_tomcat_service(host):
    s = host.service('tomcat')
    assert s.is_running
    assert s.is_enabled


def test_tomcat_listen_address(host):
    # install iproute to use the socket test
    host.ansible("command", "yum -y install iproute", become=True, check=False)
    s = host.socket('tcp://0.0.0.0:8080')
    assert s.is_listening
