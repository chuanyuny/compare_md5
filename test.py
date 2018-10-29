# -*- coding: utf-8 -*-
import hashlib
import os
import difflib
import time

def write_to_txt(path,content):
    fw = open(path,'a')
    fw.writelines(content)
    fw.close()

def read_txt(path):
    fo=open(path,'r')
    content=fo.readlines()
    fo.close()
    return content

def generate_md5(file_name):
    file_list=[] #存放给定文件夹下所有文件的路径。
    file_md5_list=[]  #存放当前文件夹下所有文件的md5值
    for root,dirs,files in os.walk(file_name):
        for file in files:
            file_list.append(os.path.join(root,file))
    for each in file_list:
        md5file = open(each, 'rb')
        md5 = hashlib.md5(md5file.read()).hexdigest()
        md5file.close()
        print(each,md5)
        file_md5_list.append(md5+'\n')
    return file_md5_list

def generate_html_result(filename):
    path = 'md5_compare_result.%f.html' % time.time()
    diffmkfile = open(path, 'w', encoding="utf-8")
    # diffmkfile = open('./result/.%f.html' % time.time(),'w',encoding="utf-8")
    diffmkfile.write("<meta charset='utf-8'>")
    diffmkfile.write(filename)
    diffmkfile.close()
    time.sleep(0.5)

if __name__ == "__main__":
    account_path=["","",""]
    token_path=["","",""]
    for each in account_path:
        content = generate_md5(each)
        try:
            write_to_txt('C:\\Users\\Administrator\\Desktop\\generate_md\aa.txt',content)
            print("md5值生成成功！")
        except:
            print("md5值生成失败！")

    for each in token_path:
        content2 = generate_md5(each)
        try:
            write_to_txt('C:\\Users\\Administrator\\Desktop\\generate_md\\tt.txt',content2)
            print("md5值生成成功！")
        except:
            print("md5值生成失败！")
    try:
        txt1=read_txt("C:\\Users\\Administrator\\Desktop\\generate_md\\aa.txt")
        txt2=read_txt("C:\\Users\\Administrator\\Desktop\\generate_md\\tt.txt")
        d=difflib.HtmlDiff()
        generate_html_result(d.make_file(txt1,txt2))
    except:
        print("对比失败")
    else:
        print("aa.txt 和 tt.txt 对比成功")


