# -*- coding: utf-8 -*-
"""
@author: LiaoKong
@time: 2021/11/09 22:46 
"""
from datetime import datetime

from extend.db import Base
from sqlalchemy import Column, Integer, String, DateTime, Date, ForeignKey
from sqlalchemy.orm import relationship


class Department(Base):
    __tablename__ = "department"
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(255))
    leader = Column(String(255))
    desc = Column(String(255))
    state = Column(Integer, default=1)
    user = relationship('User', backref='department')
    create_time = Column(DateTime, default=datetime.now())
    crate_date = Column(Date, default=datetime.now())


class User(Base):
    __tablename__ = "user"
    id = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String(255))
    pwd = Column(String(255))
    dep_id = Column(Integer, ForeignKey('department.id'))
    avatar = Column(String(255))
    addr = Column(String(255))
    # 1启动 2停用
    state = Column(Integer, default=1)
    last_login_date = Column(Date, default=datetime.now())
    ip = Column(String(255))
    create_time = Column(DateTime, default=datetime.now())
    crate_date = Column(Date, default=datetime.now())
