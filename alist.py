import sys,os,argparse,json,requests,time
from urllib import parse

parser = argparse.ArgumentParser(description='操作Alist')
parser.add_argument("--file", help="上传文件名", default="")
args = parser.parse_args()

alist_host="http://alist:5344"
UserAgent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36'

# 获取Token
def login():
  url = f'{alist_host}/api/auth/login?Password=admin&Username=admin'
  payload = {}
  headers = {}
  response = requests.request("POST", url, headers=headers, data=payload)
  result = json.loads(response.text)
  return result['data']['token']

# 新建存储
def storage_create(token,body):
    url = f'{alist_host}/api/admin/storage/create'
    storage_header = {
        'UserAgent': UserAgent,
        'Authorization': token
    }
    try:
        return requests.post(url, json=body, headers=storage_header, timeout=60)
    except Exception as e:
        return {'code': -1, 'message': e}
  
# 上传文件
def Upload(token,localPath, remotePath, fileName, password = ''):
    upload_header = {
        'UserAgent': UserAgent,
        'Authorization': token,
        'File-Path': parse.quote(f'{remotePath}/{fileName}'),
        'Password': password,
        'Content-Length': f'{os.path.getsize(localPath)}'
    }
    try:
        return json.loads(requests.put(f'{url}/fs/put', headers=upload_header, data=open(localPath, 'rb').read()).text)
    except Exception as e:
        return {'code': -1, 'message': e}
   


if __name__ == '__main__':
    auth_token=login()
    storage_create(auth_token,args.storage_body)
    time.sleep(2)
    Upload(auth_token,"downloads","encrypt_folder",args.file)
    
    
