# coding: utf-8
from sqlalchemy import Column, Integer, String, BigInteger
from .my_db import BASE


class Playlist(BASE):
    __tablename__ = 'playlists'

    id = Column(String(255), primary_key=True)
    name = Column(String(255))
    type = Column(String(255))
    tags = Column(String(255))
    create_time = Column(String(255))
    update_time = Column(String(255))
    tracks_num = Column(Integer)
    play_count = Column(Integer)
    subscribed_count = Column(Integer)
    share_count = Column(Integer)
    comment_count = Column(Integer)
    nickname = Column(String(255))
    gender = Column(String(255))
    user_type = Column(String(255))
    vip_type = Column(String(255))
    province = Column(String(255))
    city = Column(String(255))


class User(BASE):
    __tablename__ = 'table_name'

    id = Column(BigInteger, primary_key=True, unique=True)
    age = Column(Integer)

    class Config:
        orm_mode = True
