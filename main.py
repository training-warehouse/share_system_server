# -*- coding: utf-8 -*-
"""
@author: LiaoKong
@time: 2021/11/08 22:21 
"""
import uvicorn
from fastapi import FastAPI, Depends
from fastapi.security import OAuth2PasswordRequestForm
from fastapi.middleware.cors import CORSMiddleware

from extend.db import Engine, LocalSession, Base

app = FastAPI(
    title='网盘分享系统'
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_methods=['*'],
    allow_headers=['*'],
    allow_credentials=True
)

Base.metadata.create_all(bind=Engine)




@app.post('/login')
def login(user: OAuth2PasswordRequestForm = Depends()):
    username = user.username
    pwd = user.password


if __name__ == '__main__':
    uvicorn.run('main:app', reload=True, host='0.0.0.0', port=8080)
