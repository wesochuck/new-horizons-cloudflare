import re
with open("index.html") as f:
    html = f.read()
body = re.search(r'<body.*?>(.*?)</body>', html, re.DOTALL)
if body:
    print(body.group(1))
