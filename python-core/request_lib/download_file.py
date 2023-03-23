import shutil

import requests


def download1(res):
    file = open("img/sun-hat.jpg", "wb")
    file.write(res.content)


def download2(url):
    local_filename = url.split('/')[-1]
    # NOTE the stream=True parameter below
    with requests.get(url, stream=True) as r:
        r.raise_for_status()
        with open(local_filename, 'wb') as f:
            for chunk in r.iter_content(chunk_size=1024):
                # if chunk:
                f.write(chunk)
    return local_filename


def download3(url):
    local_filename = url.split('/')[-1]
    with requests.get(url, stream=True) as r:
        with open(local_filename, 'wb') as f:
            shutil.copyfileobj(r.raw, f)

    return local_filename


r = requests.get('https://cdn.pixabay.com/photo/2018/07/05/02/50/sun-hat-3517443_1280.jpg', stream=True)
download1(r)
# download2(r.url)
# download3(r.url)
