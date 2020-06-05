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
    @staticmethod
    def get_homepage():
        # 首页加载,[(1, '## 测试用内容 修改过了', '修改后的标题'), (2, '## 测试用内容111', '再次测试')]
        data =  Article.query.with_entities(Article.id,Article.title,
                                           Article.article_type,Article.updated_time,
                                           Article.comment_times,Article.read_times).all()
        # 将据中的datetime类型转换为字符串的日期
        for i in range(len(data)):
            data[i] = list(data[i])
            data[i][4] = str(data[i][4])
        return data

    @staticmethod
    def get_one_article(id):
        """
        返回一篇文章的全部信息
        :param id: 文章id
        :return:
        [1, '修改后的标题', '## 测试用内容 修改过了', '测试用分类', datetime.datetime(2020, 6, 4, 16, 53, 45), 0, 0]
        [[2, '## 测试用评论', '喜喜', '日期'],[...]]
        """
        # 文章的阅读次数+1
        model_article = Article.query.filter_by(id=id).first()
        model_article.read_times += 1

        article_data = Article.query.with_entities(Article.id,Article.title,Article.content,
                                           Article.article_type,Article.updated_time,
                                           Article.created_time,
                                           Article.comment_times,Article.read_times).filter_by(id=id).first()
        # 将数据中的datetime类型转换为字符串的日期
        article_data = list(article_data)
        article_data[4] = str(article_data[4])
        article_data[5] = str(article_data[5])

        # 查询对应的评论信息
        comment_data = Comment.query.with_entities(Comment.id,Comment.content,
                                                   Comment.nickname,Comment.created_time).filter_by(article_id=id).all()
        # 将据中的datetime类型转换为字符串的日期
        for i in range(len(comment_data)):
            comment_data[i] = list(comment_data[i])
            comment_data[i][3] = str(comment_data[i][3])

        # 将数据合并成一个列表
        data = [article_data,comment_data]


        return data,model_article




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

    @staticmethod
    def add_comment(form):
        # 添加评论
        model_comment = Comment()
        model_comment.article_id = int(form['article_id'])
        model_comment.content = form['content']
        model_comment.nickname = form['nickname']
        model_comment.created_time = getCurrentTime()
        # 添加评论的同时在Article表中添加一个评论计数
        model_article = Article.query.filter_by(id=int(form['article_id'])).first()
        model_article.comment_times += 1

        return model_comment,model_article

    @staticmethod
    def delete_comment(form):
        # 删除评论 , 使用id作为删除查询标准
        model_comment = Comment.query.filter_by(id=form['id']).first()
        # 同时在article表中执行评论减一
        model_article = Article.query.filter_by(id=form['article_id']).first()
        model_article.comment_times -= 1
        return model_comment,model_article


# db.create_all()
