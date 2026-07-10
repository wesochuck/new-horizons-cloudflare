import re
import base64

with open("index.html") as f:
    html = f.read()

match = re.search(r'data:image/png;base64,([^"]+)', html)
if match:
    img_data = base64.b64decode(match.group(1))
    with open("logo.png", "wb") as f:
        f.write(img_data)
    print("Logo extracted successfully.")
else:
    print("Logo not found.")
