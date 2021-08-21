from ncclient import manager

nc_template = open("config-template.xml").read()
nc_payload = nc_template.\
                    format(int_name='Loopback0',
                          int_desc="Configured by NETCONF")

with manager.connect(host='172.16.2.34', username='root',
                     password='xxxx', hostkey_verify=False) as nc_conn:
    netconf_reply = nc_conn.edit_config(nc_payload, target="candidate")
    print(netconf_reply)
    reply = nc_conn.commit()
    print(reply)

