import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_opt_labkey(host):
    f = host.file('/opt/labkey')
    assert f.is_symlink
    assert f.exists