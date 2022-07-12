from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

__all__ = ["BASE", "get_db"]


class _DBConnect:
    # 定义一个变量
    # _SQLALCHEMY_DATABASE_URL = "sqlite:///./sqlite_database.db"
    _SQLALCHEMY_DATABASE_URL = "mysql+pymysql://root:1234567@localhost:3306/cloudmusic?charset=utf8"
    # SQLALCHEMY_DATABASE_URL = "postgresql://user:password@postgresserver/db"

    # 创建一个连接
    _engine = create_engine(
        _SQLALCHEMY_DATABASE_URL
    )

    # 创建一个持久对象，好处就是可以一次添加多个对象
    SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=_engine)

    # 定义一个ORM模型基类
    Base = declarative_base()
    # 绑定连接，使用表元数据和引擎
    Base.metadata.create_all(bind=_engine)


# _DBConnect.Base赋值给BASE变量
BASE = _DBConnect.Base


def get_db():
    """
    初始化持久对象，并yield返回
    无论失败与否最后都会调用关闭
    :return:
    """
    db = _DBConnect.SessionLocal()
    try:
        yield db
    finally:
        print('db close')
        db.close()
    # return db
