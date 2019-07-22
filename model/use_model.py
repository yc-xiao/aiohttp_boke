"""
    TODO:
        提供数据库的CDUG功能
        操作对象， 表名， 具体数据
"""
from .model import UserModel, ArticleModel, CommentModel

mmap = {
    "UserModel": UserModel,
    "ArticleModel": ArticleModel,
    "CommentModel": CommentModel
}

def new(session, table, datas):
    obj = mmap[table](**datas)
    session.add(obj)
    session.commit()

def delete(session, table, datas):
    # session.query(Student).filter(Student.id == 1001).delete()
    pass

def update(session, table, datas):
    pass

def find(session, table, datas):
    pass
