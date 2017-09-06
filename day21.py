#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
在 python 中有 hashlib 和 base64 两大加密模块，将一串字符串先经过 hashlib.md5 加密，然后再经过 base64 加密，最后得到一串字符：

'NDRiMWZmMmVjZTk5MTFjMWI1MDNkYTY0MzZlYTAzMTA=\n'

在此给出 4 个选项

我们在一起吧
我选择原谅你
别说话，吻我
多喝热水
'''
import hashlib
import base64
print  hashlib.new("md5","多喝热水").hexdigest()
print base64.decodestring('NDRiMWZmMmVjZTk5MTFjMWI1MDNkYTY0MzZlYTAzMTA=') #加密