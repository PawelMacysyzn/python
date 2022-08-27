import requests
import os
from functools import partial


def save_url_file(url, dir_catalog, file_name, msg):
    print(msg.format(file_name))

    r = requests.get(url, stream=True)
    file_path = os.path.join(dir_catalog, file_name)

    with open(file_path, "wb") as f:
        f.write(r.content)


msg = "Please wait - the file {} will be downloaded"
dir_catalog = os.path.abspath(os.getcwd())

save_url_to_dir = partial(save_url_file, msg=msg, dir_catalog=dir_catalog)


file_name = 'spis.html'
url = 'http://mobilo24.eu/spis'

save_url_to_dir(file_name=file_name, url=url)
