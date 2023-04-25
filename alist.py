import sys
import os
import argparse
import json
import requests


parser = argparse.ArgumentParser(description='操作Alist')
parser.add_argument("--file", help="上传文件名", default="")
args = parser.parse_args()

def login():
  url = "http://alist:5244/api/auth/login?Password=admin&Username=admin"
  payload = {}
  headers = {}
  response = requests.request("POST", url, headers=headers, data=payload)
  result = json.loads(response.text)
  return result['data']['token']

if __name__ == '__main__':
    auth_token=login()
    url = "http://alist:5244/api/admin/setting/list?group=0"
    payload = {}
    headers = {
      'Authorization': auth_token
    }
    response = requests.request("GET", url, headers=headers, data=payload)
    print(response.text)
