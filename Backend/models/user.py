from application import db
from libs.date_helper import getCurrentTime


class User(db.Model):
    __tablename__ = 'user'

    id = db.Column(db.Integer, primary_key=True)
    login_name = db.Column(db.String(25), nullable=False, unique=True)
    _login_pwd = db.Column(db.String(150), nullable=False)
    status = db.Column(db.Integer, nullable=False, server_default="1")
    updated_time = db.Column(db.DateTime, nullable=False, server_default=db.FetchedValue())
    created_time = db.Column(db.DateTime, nullable=False, server_default=db.FetchedValue())

class Article(db.Model):
    __tablename__ = 'article'
    __table_args__ = {
        'mysql_charset': 'utf8'
    }

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(150), nullable=False, unique=True)
    content = db.Column(db.Text,nullable=True)
    read_times = db.Column(db.Integer, nullable=False, server_default="0")
    comment_times = db.Column(db.Integer, nullable=False, server_default="0")
    # 文章分类
    article_type = db.Column(db.String(20), nullable=False)
    updated_time = db.Column(db.DateTime, nullable=False, server_default=db.FetchedValue())
    created_time = db.Column(db.DateTime, nullable=False, server_default=db.FetchedValue())
    @staticmethod
    def add_article(form):
        # 添加文章数据到实例中
        model_article = Article()
        model_article.title = form['title']
        model_article.content = form['content']
        model_article.article_type = form['article_type']
        model_article.created_time = model_article.updated_time = getCurrentTime()
        return model_article
    @staticmethod
    def modify_article(form):
        # 修改文章
        model_article = Article.query.filter_by(title=form['title']).first()
        model_article.content = form['content']
        model_article.title = form['modified_title']
        model_article.article_type = form['article_type']
        model_article.updated_time = getCurrentTime()
        return model_article
    @staticmethod
    def delete_article(form):
        # 删除文章
        model_article = Article.query.filter_by(title=form['title']).first()
        return model_article

class Draft(db.Model):
    # 草稿模型
    __tablename__ = 'draft'
    __table_args__ = {
        'mysql_charset': 'utf8'
    }

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(150), nullable=False, unique=True)
    content = db.Column(db.Text, nullable=True)

    @staticmethod
    def add_draft(form):
        model_draft = Draft()
        model_draft.title = form['title']
        model_draft.content = form['content']
        return model_draft

    @staticmethod
    def modify_draft(form):
        model_draft = Draft.query.filter_by(title=form['title']).first()
        model_draft.content = form['content']
        model_draft.title = form['modified_title']
        return model_draft

    @staticmethod
    def delete_draft(form):
        model_draft = Draft.query.filter_by(title=form['title']).first()
        return model_draft


class Comment(db.Model):
    __tablename__ = 'comment'
    __table_args__ = {
        'mysql_charset': 'utf8'
    }

    id = db.Column(db.Integer, primary_key=True)
    article_id = db.Column(db.Integer,nullable=False, unique=False)
    content = db.Column(db.Text,nullable=False)
    nickname = db.Column(db.String(20), nullable=True, unique=False)
    created_time = db.Column(db.DateTime, nullable=False, server_default=db.FetchedValue())

db.create_all()
