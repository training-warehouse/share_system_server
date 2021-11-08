# -*- coding: utf-8 -*-
"""
@author: LiaoKong
@time: 2021/11/08 22:58 
"""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

url = 'sqlite:///./share_system_db.db'

Engine = create_engine(url, encoding='utf-8', echo=True,
                       connect_args={'check_same_thread': False})
LocalSession = sessionmaker(bind=Engine, autoflush=False, autocommit=False,
                            expire_on_commit=True)

Base = declarative_base()
