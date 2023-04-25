import sys
import argparse
import json
import requests

parser = argparse.ArgumentParser(description='操作Alist')
parser.add_argument("--act", help="操作", default="")
args = parser.parse_args()

def login():
  url = "http://alist:5244/api/auth/login?Password=admin&Username=admin"
  payload = {}
  headers = {}
  response = requests.request("POST", url, headers=headers, data=payload)
  result = json.loads(r.text)
  return result['data']['token']

if __name__ == '__main__':
  if args.act=='login':
    auth_token=login()
    print(auth_token)
  else:
    quit()
