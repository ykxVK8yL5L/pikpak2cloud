import sys
import argparse
import os
import json
import requests

parser = argparse.ArgumentParser(description='操作Alist')
parser.add_argument("--act", help="挂行动作", default="")
parser.add_argument("--url", help="下载链接", default="")
parser.add_argument("--refresh_token", help="Aliyun的refresh_token", default="")
parser.add_argument("--token", help="Alist的token", default="")
parser.add_argument("--dir", help="加密目录", default="")
parser.add_argument("--file", help="上传的文件名", default="")
args = parser.parse_args()


def login():
  return 'hello'
  url = "http://127.0.0.1:5344/api/auth/login?Password=admin&Username=admin"
  payload={}
  headers = {}
  response = requests.request("POST", url, headers=headers, data=payload)
  logininfo = json.loads(response.text);
  token = logininfo['data']['token']
  return token

def download(downloadUrl:str):
  urlinfo = downloadUrl.split("##");
  cmd = "aria2c --conf aria2.conf --seed-time=0 -o "+urlinfo[1]+" -d downloads -c \""+urlinfo[0]+"\""
  os.system(cmd)

def upload(filename: str,token:str):
  cmd = "curl -T 'zouzou.mp4' 'http://localhost:5344/api/fs/put  -X 'PUT' \
  -H 'Accept: application/json, text/plain, */*' \
  -H 'Accept-Language: zh-CN,zh;q=0.9,en;q=0.8' \
  -H 'Authorization: "+token+"' \
  -H 'File-Path: %2Fencrypt_folder%2F"+filename+"' \
  -H 'Origin: http://localhost:5344' \
  -H 'Password;' \
  -H 'Referer: http://localhost:5344/encrypt_folder' \
  -H 'User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36' \
  --compressed \
  --insecure"
  os.system(cmd)
  
def mount_aliyun(refresh_token:str,root_id:str,token:str):
  cmd = """
  curl 'http://localhost:5344/api/admin/storage/create' \
  -H 'Accept: application/json, text/plain, */*' \
  -H 'Accept-Language: zh-CN,zh;q=0.9,en;q=0.8' \
  -H 'Authorization: """+token+"""' \
  -H 'Connection: keep-alive' \
  -H 'Content-Type: application/json;charset=UTF-8' \
  -H 'Origin: http://localhost:5344' \
  -H 'Referer: http://localhost:5344/@manage/storages/create' \
  -H 'User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36' \
  --data-raw '{"id":1,"mount_path":"/aliyun","order":0,"driver":"AliyundriveOpen","cache_expiration":30,"status":"work","addition":"{\"root_folder_id\":\""""+root_id+"""\",\"refresh_token\":\""""+refresh_token+"""\",\"order_by\":\"\",\"order_direction\":\"\",\"oauth_token_url\":\"https://api.nn.ci/alist/ali_open/token\",\"client_id\":\"\",\"client_secret\":\"\",\"remove_way\":\"delete\",\"internal_upload\":false,\"AccessToken\":\"\"}","remark":"","modified":"2023-04-24T06:37:11.054213327Z","disabled":false,"enable_sign":false,"order_by":"","order_direction":"","extract_folder":"","web_proxy":false,"webdav_policy":"302_redirect","down_proxy_url":""}' \
  --compressed \
  --insecure
  """
  os.system(cmd)


if __name__ == '__main__':
  if args.act=='mount':
    mount_aliyun(args.refresh_token,args.dir,args.token)
  elif args.act=='download':
    download(args.url,args.token)
  elif args.act=='login':
    token=login()
    print(token)
  else:
    upload(args.file,args.token)

