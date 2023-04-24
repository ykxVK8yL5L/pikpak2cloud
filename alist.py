import sys
import argparse
import os
import json
import requests

parser = argparse.ArgumentParser(description='操作Alist')
parser.add_argument("--act", help="挂行动作", default="")
parser.add_argument("--url", help="下载链接", default="")
parser.add_argument("--token", help="Aliyun的token", default="")
parser.add_argument("--dir", help="加密目录", default="")
parser.add_argument("--file", help="上传的文件名", default="")
args = parser.parse_args()


def download(downloadUrl:str):
  urlinfo = downloadUrl.split("##");
  cmd = "aria2c --conf aria2.conf --seed-time=0 -o "+urlinfo[1]+" -d downloads -c \""+urlinfo[0]+"\""
  os.system(cmd)

def upload(filename: str):
  url = "http://alist:5344/api/auth/login?Password=admin&Username=admin"
  payload={}
  headers = {}
  response = requests.request("POST", url, headers=headers, data=payload)
  logininfo = json.loads(response.text);
  token = logininfo['data']['token']
  cmd = "curl -T 'zouzou.mp4' 'http://alist:5344/api/fs/put  -X 'PUT' \
  -H 'Accept: application/json, text/plain, */*' \
  -H 'Accept-Language: zh-CN,zh;q=0.9,en;q=0.8' \
  -H 'Authorization: "+token+"' \
  -H 'File-Path: %2Fencrypt_folder%2F"+filename+"' \
  -H 'Origin: http://alist:5344' \
  -H 'Password;' \
  -H 'Referer: http://alist:5344/encrypt_folder' \
  -H 'User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36' \
  --compressed \
  --insecure"
  os.system(cmd)
  
def mount_aliyun(refresh_token:str,root_id:str):
  
  
if __name__ == '__main__':
  if args.act=='mount':
    mount_aliyun(args.token,args.dir)
  elif args.act=='download':
    download(args.url)
  else:
    upload(args.file)

