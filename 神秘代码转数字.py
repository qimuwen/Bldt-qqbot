# -*-coding = utf-8 -*-
# @Time:2021/10/11/12:59
# @Author:seven
# @File:神秘代码转数字.py
# @Software:PyCharm
"""print(lazy_pinyin('嗯'))
print(pinyin('中心', style=Style.FIRST_LETTER))
print(type(pinyin('中心', style=Style.FIRST_LETTER)))
['zhong', 'xin']
['n']
[['z'], ['x']]
<class 'list'>"""
from pypinyin import pinyin, lazy_pinyin, Style
def cookie(dm):
    w=''
    for q in dm:
        if  '\u4e00' <= q <= '\u9fa5':
             a=lazy_pinyin(q)[0]

             if a=='jia':
                 q='+'
             elif a=='jian':
                 q='-'
             elif a=='cheng':
                 q='*'
             elif a=='chu':
                 q='/'
             elif a=='yi':
                 q='1'
             elif a=='er' or a=='ai':
                 q='2'
             elif a == 'shan' or a=='san':
                 q = '3'
             elif a == 'si':
                 q = '4'
             elif a == 'wu':
                 q = '5'
             elif a == 'liu'or a=='lu':
                 q = '6'
             elif a=='qi':
                 q='7'
             elif a == 'ba' or a=='pa':
                 q = '8'
             elif a == 'jiu' or a=='qiu':
                 q = '9'
             elif a=='shi':
                 q='10'
        w+=q


    return w
# dm=input()
# cookie(dm)