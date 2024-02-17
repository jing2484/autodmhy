 名称: autodmhy  
 版本: v1.7  
 作者: kidtic   
 说明: 实现动漫花园www.dmhy.org自动追番功能   

## 环境
提前设置好代理与比特彗星的远程下载功能

## 使用 
autodmhy.py会自动遍历当前目录下的所有文件夹，只有文件夹中有dmhy.json的才会被当作工作目录。   
    终端运行 【autodmhy.py add "动漫名" "关键词" [S2]】 会添加指定的目录S2可加可不加   
    终端运行 【autodmhy.py ref】会重新刷新所有的dmhy.json的items，同步网站内容。   
    终端运行 【autodmhy.py】 动态更新items，并且进行自动补充下载   

## 目录结构
    xxx动漫1/
        xxx01.mp4
        xxx02.mp4
        dmhy.json
    xxx动漫2/
        xxx01.mp4
        xxx02.mp4
        dmhy.json
    autodmhy.py

## 版本改动:
    v1.1 - 将所有正在追番的目录打印出来，并且停在最后。
    v1.2 - 取消代理
    v1.3 - 修改框架 dmhy.json
    v1.4 - 加入重命名功能，不过需要把比特彗星的任务停掉重新运行才行。
    v1.5 - 修复v1.4的两个bug
    v1.6 - 增加add添加动漫
    v1.7 - 增加比特彗星自动删除任务列表功能，防止重名的时候会产生冲突。