import sys,os,argparse,json,requests,time,base64
from urllib import parse

parser = argparse.ArgumentParser(description='操作Alist')
parser.add_argument("--storage_body", help="存储设置base64加密", default="")
parser.add_argument("--path", help="上传本地路径", default="")
parser.add_argument("--fileName", help="上传文件名", default="")
args = parser.parse_args()

alist_host="http://alist-encrypt:5344"
UserAgent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36'

# 获取Token
def login():
  url = f'{alist_host}/api/auth/login?Password=admin&Username=admin'
  payload = {}
  headers = {}
  response = requests.request("POST", url, headers=headers, data=payload,timeout=60)
  result = json.loads(response.text)
  return result['data']['token']

# 新建存储
def storage_create(token,body):
    data=json.loads(body.decode("utf-8").replace('\n', '').replace(' ', ''))
    url = f'{alist_host}/api/admin/storage/create'
    storage_header = {
        'UserAgent': UserAgent,
        'Authorization': token
    }
    try:
        return requests.post(url, json=data, headers=storage_header, timeout=60)
    except Exception as e:
        return {'code': -1, 'message': e}
  
# 上传文件，由于Rclone的Bug已经修复，直接使用Rclone上传
def Upload(token,localPath, remotePath, fileName, password = ''):
    try:
        upload_header = {
            'UserAgent': UserAgent,
            'Authorization': token,
            'File-Path': parse.quote(f'{remotePath}/{fileName}'),
            'Password': password,
            'Content-Length': f'{os.path.getsize(localPath)}'
        }
        return json.loads(requests.put(f'{alist_host}/api/fs/put', headers=upload_header, data=open(localPath, 'rb').read()).text)
    except Exception as e:
        return {'code': -1, 'message': e}
   
if __name__ == '__main__':
    auth_token=login()
    storage_result = json.loads(storage_create(auth_token,base64.b64decode(args.storage_body)).text)
    if storage_result['message']=='success':
        print("挂载成功")
#        quit()
        time.sleep(2)
        upload_result=Upload(auth_token,args.path,"encrypt_folder",args.fileName)
        print(upload_result)
    else:
        print("出错了，可能是存储字符串错误")
        quit()
