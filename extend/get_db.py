# -*- coding: utf-8 -*-
"""
@author: LiaoKong
@time: 2021/11/08 23:30 
"""
from .db import LocalSession


def get_db():
    try:
        db = LocalSession()
        yield db
    finally:
        db.close()
