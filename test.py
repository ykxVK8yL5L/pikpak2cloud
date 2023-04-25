import requests

r  = requests.get('http://alist:5344/public/index.html')
print(r.text)
