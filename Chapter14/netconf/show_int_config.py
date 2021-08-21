from ncclient import manager
interface_filter = """
<filter>
    <interfaces xmlns="http://openconfig.net/yang/interfaces">
        <interface>
            <name>{int_name}</name>
        </interface>
    </interfaces>
</filter>
"""

with manager.connect(host='172.16.2.34', username='root', password='xxxx', hostkey_verify=False) as conn:

    filter = interface_filter.format(int_name = "MgmtEth0/RP0/CPU0/0")
    result = conn.get_config("running", filter )
    print (result)
