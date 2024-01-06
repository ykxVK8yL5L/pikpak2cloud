# pikpak2cloud
###### 目前上传10G以上文件经常出错 尽量不要上传10G以上的大文件吧   
### 在网盘根目录建立encrypt_folder目录作为默认上传目录 
# 20230426 Alist上传基本完成 目前只能上传文件 需要添加secrets   
ALIST_STORAGE_BODY：Alist添加存储的json对象的base64加密，有些难懂 建议看视频操作。稍后放上视频链接   
支持Alist的话相当于支持了其它的网盘 已不仅限于阿里云了

https://youtu.be/KXXTwzZlGNc

# 20240106Alist使用远程数据库实现一次配置到处使用   
config.json文件内容
```
{
  "force": false,
  "site_url": "",
  "cdn": "",
  "jwt_secret": "wlTTJM2ndocNcsw5",
  "token_expires_in": 48,
  "database": {
    "type": "postgres",
    "host": "xxxxxx",
    "port": 5433,
    "user": "xxxxx",
    "password": "xxxxxx",
    "name": "xxxxxx",
    "db_file": "data/data.db",
    "table_prefix": "x_",
    "ssl_mode": "prefer"
  },
  "scheme": {
    "address": "0.0.0.0",
    "http_port": 5244,
    "https_port": -1,
    "force_https": false,
    "cert_file": "",
    "key_file": "",
    "unix_file": "",
    "unix_file_perm": ""
  },
  "temp_dir": "data/temp",
  "bleve_dir": "data/bleve",
  "dist_dir": "",
  "log": {
    "enable": true,
    "name": "data/log/log.log",
    "max_size": 50,
    "max_backups": 30,
    "max_age": 28,
    "compress": false
  },
  "delayed_start": 0,
  "max_connections": 0,
  "tls_insecure_skip_verify": true,
  "tasks": {
    "download": {
      "workers": 5,
      "max_retry": 1
    },
    "transfer": {
      "workers": 5,
      "max_retry": 2
    },
    "upload": {
      "workers": 5,
      "max_retry": 0
    },
    "copy": {
      "workers": 5,
      "max_retry": 2
    }
  },
  "cors": {
    "allow_origins": [
      "*"
    ],
    "allow_methods": [
      "*"
    ],
    "allow_headers": [
      "*"
    ]
  }
}
```
   
# Alist如果使用rclone copy出错的话，请改用alist的api上传具体看视频介绍   
# 20230518新增加密转存至tmp.link功能    
需要添加1个secrets:   
TMP_TOKEN:可以在tmp.link后台的curl上传处获取   
# 20230421新增加密转存阿里云功能 
需要添加两个secrets:   
ALIYUN_REFRESH_TOKEN:阿里云刷新Token用来挂载阿里云webdav    
RCLONE_ALIYUN_CONF:Rclone用来拷贝文件到阿里云Webdav,或添加到已有secrets.内容为固定的。
```
[aliyun]
type = webdav
url = http://alist:5344/
vendor = other
[alist]
type = webdav
url = http://alist-encrypt:5344/dav
vendor = other
user = admin
pass = VmiZZcVpZnbDzjmqI5VnevHKOnQU
```

如果需要自定义密码：可自建secrets

# 由于github的限制 Linux的Actions最大只能传9g的文件 Mac最大能传14g。
pikpak转存到其它网盘(Onedriver，如需其它网盘修改rclone配置即可，视频只是以onedriver为例)
https://youtu.be/t9KhFoWQqEI

# 一共三个secrets:USERNAME、PASSWORD、RCLONE_CONF分别是PikPak的用户名密码和Rclone的配置文件
如果使用需要修改actions里的上传路径即rclone copy后面的远程路径为自己的名称。


