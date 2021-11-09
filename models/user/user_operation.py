# -*- coding: utf-8 -*-
"""
@author: LiaoKong
@time: 2021/11/09 22:47 
"""

from sqlalchemy.orm import Session
from models.user.user_model import User


def get_username_and_pwd(db: Session, username: str, md5_pwd: str) -> User:
    user = db.query(User.id, User.username, User.avatar, User.ip,
                    User.last_login_date).filter(
        User.username == username, User.password == md5_pwd).first()

    return user
