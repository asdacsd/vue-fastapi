from pydantic import BaseModel
from typing import List, Optional


class PlayList(BaseModel):
    id: str
    name: str
    type: str
    tags: str
    create_time: str
    update_time: str
    tracks_num: int
    play_count: int
    subscribed_count: int
    share_count: int
    comment_count: int
    nickname: str
    gender: str
    user_type: str
    vip_type: str
    province: str
    city: str


class MyUser(BaseModel):
    # id: int
    age: int
