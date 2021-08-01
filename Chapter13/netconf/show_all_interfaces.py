from ncclient import manager
with manager.connect(host='172.16.2.50', username='root',
                     password='rootroot', hostkey_verify=False) as m:
    result = m.get_config("running",
                          filter=('subtree',
                                  '<interfaces xmlns="http://openconfig.net/yang/interfaces"/>'))
    print (result)
