# -*- coding: utf-8 -*-
"""
@author: LiaoKong
@time: 2021/11/08 22:21 
"""
import uvicorn
from fastapi import FastAPI, Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session

from extend.db import Engine, LocalSession, Base
from extend.get_db import get_db
from utils.get_md5_data import get_md5_pwd
from models.user.user_operation import get_username_and_pwd

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
def login(user: OAuth2PasswordRequestForm = Depends(),
          db: Session = Depends(get_db)):
    username = user.username
    pwd = user.password
    md5_pwd = get_md5_pwd(pwd)
    user = get_username_and_pwd(db, username, md5_pwd)
    if user:
        user_info = {'username': user.username, 'avatar': user.avatar,
                     'ip': user.ip, 'last_login_date': user.last_login_date}
        return JSONResponse(
            {'code': 200, 'msg': '登录成功', 'token': '', 'user': user_info})

    return JSONResponse({'code': 500, 'msg': '用户名密码错误'})


if __name__ == '__main__':
    uvicorn.run('main:app', reload=True, host='0.0.0.0', port=8080)
