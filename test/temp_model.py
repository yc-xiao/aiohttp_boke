from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from model import ArticleModel, CommentModel, UserModel, get_unit_id
#engine = create_engine('mysql+aiomysql://root:333333@localhost:3306/boke')
#Session =  sessionmaker(bind=engine)


# 创建引擎，连接数据库。
engine = create_engine('mysql+pymysql://root:333333@localhost:3306/boke')
# 获取会话对象
Session = sessionmaker(bind=engine)
# 创建session对象:
session =  Session()
user_id, writor_id, actor_id, article_id, comment_id = [get_unit_id() for i in range(5)]
user = {
    'user_id': user_id,
    'name': 'yc',
    'password': 'dda12'
}
article = {
    'article_id': article_id,
    'writor_id': writor_id,
    'title': 'python使用',
    'content': 'aa'*1000
}
comment = {
    'comment_id': comment_id,
    'article_id': article_id,
    'writor_id': writor_id,
    'actor_id': actor_id,
    'content': 'aa'*1000
}
# 创建新User对象:
new_user = UserModel(**user)
new_article = ArticleModel(**article)
new_comment = CommentModel(**comment)
# 添加到session:
session.add(new_user)
session.add(new_article)
session.add(new_comment)
# 提交即保存到数据库:
session.commit()
# 关闭session:
session.close()
