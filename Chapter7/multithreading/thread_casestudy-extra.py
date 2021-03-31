# this is a code without using any threads
from time import time

from getfilelistpy import getfilelist
import gdown

resource = {
    "api_key": "AIzaSyDYKmm85keqnk4bF1DpYa2bxddKrGns4z0",
    "id": "0B8TxHW2Ci6dbckVweTRtTlV3RUU",
    "fields": "files(name,id,webContentLink)",
}

res = getfilelist.GetFileList(resource)
files_list = res['fileList'][0]

t1 = time()
for item in files_list['files']:
    gdown.download( item['webContentLink'],
                    './files/{}'.format(item['name']),
                    quiet=False)

print('Time taken to download: %s seconds', time() - t1)