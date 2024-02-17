'''
目前的问题：
1. 所有带集数的ova都会重复
2. mkv视频不识别 fix
3. 不识别S2 fix
4. 调整好所有文件夹格式，不需要识别文件的请勿有方括号 fix
5. 不继续搜索子子文件夹 fix
'''


import os
import re
import sys

def find_common_substrings(strings):
    min_str = min(strings, key=len)
    substrings = []
    length = len(min_str)
    while length > 0:
        for i in range(len(min_str) - length + 1):
            substr = min_str[i:i+length]
            if all(substr in s for s in strings):
                substrings.append(substr)
        length -= 1
    substrings = [s for s in substrings if not any(s != t and s in t for t in substrings)]
    return substrings

def first_num(s):
    # 使用正则表达式寻找1位或2位的数字
    match = re.search(r'\d{1,2}', s)
    # 如果找到匹配项，返回该数字，否则返回None
    return int(match.group()) if match else None

def autoReName_mp4(titlename,videofile):
    '''
    智能重命名
    '''
    result = find_common_substrings(videofile)
    strings_list = []
    for estr in videofile:
        vidname = estr
        houzhui = ".mp4"
        if vidname.endswith(".mkv"):
            houzhui = ".mkv"
        elif vidname.endswith(".mp4"):
            houzhui = ".mp4"
        
        for spe in result:
            estr = estr.replace(spe,"")
        #找到头个位数字
        print(estr)
        tnum = first_num(estr)
        if tnum is None:
            strings_list.append([vidname,""])
        else:
            strnum = "{:02d}".format(tnum)
            print(strnum)
            instr = titlename+" E"+strnum+houzhui
            strings_list.append([vidname,instr])
    return strings_list

def get_videoTitle_frompwd(current_dir):
    # 获取当前目录的父文件夹
    parent_dir = os.path.basename(current_dir)
    print("parent_dir",parent_dir)
    matchs  = re.findall('\[(.*?)\]', parent_dir)
    titlename = "name"
    si = ""
    print("titlename match: ")
    print(matchs)
    if len(matchs)==1:
        titlename = matchs[0]
    if len(matchs)==2:
        titlename = matchs[0]
        temp = matchs[1]
        if len(temp)>=2 and temp[0]=='S':
            si = matchs[1]
    print(titlename,si)
    return titlename+" "+si

def autoReName_mp4_indir(dir):
    tempfname =  os.listdir(dir)
    videofile = []
    for e in tempfname:
        if e=="dmhy.json":
            return None
        if e.endswith(".mp4") or e.endswith(".mkv"):
            videofile.append(e)
    print(videofile)
    if len(videofile)==0:
        print("没有找到mp4视频")
        return None

    #获取视频名字
    titlename = get_videoTitle_frompwd(dir)
    if titlename=="name ":
        print("不是标准视频库")
        return None
    #智能重新命名
    strings_list = autoReName_mp4(titlename,videofile)

    #重复名字将不会重新命名
    strset = []
    for i in range(len(strings_list)):
        if strings_list[i][1] in strset:
            strings_list[i][1] = strings_list[i][0]
        elif strings_list[i][1]=="":
            strings_list[i][1] = strings_list[i][0]
        else:
            strset.append(strings_list[i][1])
        
    #列出结果
    for i in range(len(strings_list)):
        print(strings_list[i][1]+"  <=  "+strings_list[i][0])
    return strings_list

def allrename():
    for dirpath, dirnames, filenames in os.walk('.'):
            if dirpath != ".":
                break
            for dirname in dirnames:  #遍历所有文件夹下的内容
                workpath = os.path.join(dirpath, dirname)
                print("==============="+workpath)
                renamelist =  autoReName_mp4_indir(workpath)
                if renamelist is None:continue
                keystr = input("按回车确定 e取消")
                if keystr=='':
                    print("开始重命名")
                    for i in range(len(renamelist)):
                        os.rename(workpath+"/"+renamelist[i][0],workpath+"/"+renamelist[i][1])
                elif keystr=='e':
                    print("取消重命名")



if __name__ == '__main__':
    args = sys.argv
    if len(args)>=2:
        indir = "./"+args[1]
        print(indir)
        renamelist =  autoReName_mp4_indir(indir)
        if renamelist is None:
            input("不是标准文件夹")
            exit()
        keystr = input("按回车确定 e取消")
        if keystr=='':
            print("开始重命名")
            for i in range(len(renamelist)):
                os.rename(indir+"/"+renamelist[i][0],indir+"/"+renamelist[i][1])
        elif keystr=='e':
            print("取消重命名")

    else:
        allrename()
            
