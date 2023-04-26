# pikpak2cloud
#在网盘根目录建立encrypt_folder目录作为默认上传目录 
# 20230426 Alist上传基本完成 目前只能上传文件 需要添加secrets   
ALIST_STORAGE_BODY：Alist添加存储的json对象的base64加密，有些难懂 建议看视频操作。稍后放上视频链接   
支持Alist的话相当于支持了其它的网盘 已不仅限于阿里云了

# 20230421新增加密转存阿里云功能 
需要添加两个secrets:   
ALIYUN_REFRESH_TOKEN:阿里云刷新Token用来挂载阿里云webdav    
RCLONE_ALIYUN_CONF:Rclone用来拷贝文件到阿里云Webdav,或添加到已有secrets.内容为固定的。
```
[aliyun]
type = webdav
url = http://alist:5344/
vendor = other
```

如果需要自定义密码：可自建secrets

# 由于github的限制 Linux的Actions最大只能传9g的文件 Mac最大能传14g。
pikpak转存到其它网盘(Onedriver，如需其它网盘修改rclone配置即可，视频只是以onedriver为例)
https://youtu.be/t9KhFoWQqEI

# 一共三个secrets:USERNAME、PASSWORD、RCLONE_CONF分别是PikPak的用户名密码和Rclone的配置文件
如果使用需要修改actions里的上传路径即rclone copy后面的远程路径为自己的名称。


