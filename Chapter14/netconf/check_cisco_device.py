from ncclient import manager

with manager.connect(host='172.16.2.34', username='root', password='xxxx', hostkey_verify=False) as m:
   capabilities = []
   for capability in m.server_capabilities:
      capabilities.append(capability)
   capabilities = sorted(capabilities)
   for cap in capabilities:
     print(cap)

   result = m.get_config(source="running")
   print (result)
