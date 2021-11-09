# -*- coding: utf-8 -*-
"""
@author: LiaoKong
@time: 2021/11/09 23:06 
"""
import hashlib


def get_md5_pwd(pwd: str):
    m = hashlib.md5()
    m.update(pwd.encode())
    return m.hexdigest()


if __name__ == '__main__':
    print(get_md5_pwd('123456'))