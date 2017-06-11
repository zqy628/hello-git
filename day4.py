# -*- coding: utf-8 -*-
#找出指定文件夹中的所有以txt结尾的文件，包括所有嵌套的子文件夹。

import os

txt_files = []

if os.path.isdir('C:\Users\QY.Z\PycharmProjects\helloworld'):#判断是否为目录
    for dir_path, dir_names, file_names in os.walk('C:\Users\QY.Z\PycharmProjects\helloworld'):#三元组
        # print dir_path
        for file_name in file_names:
            if file_name.endswith('.txt'):
                txt_files.append(file_name)


print txt_files