

import requests

url = "http://challenge-c38c2cccd8a7e8bb.sandbox.ctfhub.com:10800/flag_in_here"

for i in range(5):
    for j in range(5):
        url_final = url + "/" + str(i) + "/" + str(j)
        r = requests.get(url_final)
        r.encoding = "utf-8"
        get_file=r.text
        if "flag.txt" in get_file:
            print(url_final)

