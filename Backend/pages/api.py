from flask import Blueprint, request
from werkzeug.security import generate_password_hash, check_password_hash
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import exc

from application import db
from libs.auth import login_required, jwt_login
from libs.date_helper import getCurrentTime
from libs.return_data_helper import ops_renderErrJSON, ops_renderJSON
from libs.wtf_helper import Register, Login
from models.user import User, Article, Draft, Comment

api = Blueprint("api", __name__)


@api.route('/login',methods=["POST"])
def login():
    print(request.form)
    form = Login()
    if form.validate():
        user = User.query.filter_by(login_name=form.username.data).first()
        # 使用check_password_hash验证用户密码，其中第一个参数是数据库中查询的用户加密密码，第二个参数是用户输入的密码
        if check_password_hash(user._login_pwd, form.password.data):
            # 通过验证的话就使用flask-login想客户端发送cookie
            jwt_token = jwt_login(form)
            return ops_renderJSON(msg="login success~~",data=jwt_token)
        else:
            return ops_renderErrJSON(msg="密码错误")
    else:
        return ops_renderErrJSON(msg=str(form.errors))

@api.route('/register',methods=["POST"])
def register():
    form = Register()
    if form.validate():
        # 将用户信息注册进数据库
        model_user = User()
        model_user.login_name = form.username.data
        # 使用加密方法存储密码
        model_user._login_pwd = generate_password_hash(form.password.data)
        model_user.created_time = model_user.updated_time = getCurrentTime()
        try:
            db.session.add(model_user)
            db.session.commit()
        except Exception as error:
            return ops_renderErrJSON(msg=str(error))
        else:
            return ops_renderJSON(msg="注册成功~~")
    else:
        # 返回表单验证中的错误信息
        return ops_renderErrJSON(msg=str(form.errors))

@api.route('/get_data',methods=["GET","POST"],endpoint='get_data')
@login_required
def get_data():
    return 'you getted data~'


# 不添加endpoint的话使用装饰器多次会报错
@api.route('/add_article',methods=["POST"],endpoint='add_article')
@login_required
def add_article():
    """
    接收的数据格式
    :type form-data
    {
        title = db.Column(db.String(150), nullable=False, unique=True)
        content = db.Column(db.Text,nullable=True)
        read_times = db.Column(db.Integer, nullable=False, server_default="0")
        # 文章分类
        article_type = db.Column(db.String(20), nullable=False)
        updated_time = db.Column(db.DateTime, nullable=False, server_default=db.FetchedValue())
        created_time = db.Column(db.DateTime, nullable=False, server_default=db.FetchedValue())
    }
    :return:
        成功则返回 字符串
        失败则返回元组，状态码为-1
        最终客户端接收的数据格式：
            成功：{ "code":200,"msg":"注册成功~~","data":{} }
            失败：{ “code” = -1,msg = str(error),data = {} }
    """
    # 将用户信息注册进数据库
    form = request.get_json(silent=True)
    print(form)
    model_article = Article.add_article(form)
    try:
        db.session.add(model_article)
        db.session.commit()
    except Exception as error:
        return -1,str(error)
    else:
        # 添加成功返回文章id
        return 201,"添加成功~~",Article.query.filter_by(title=form['title']).first().id

@api.route('/modify_article',methods=["POST"],endpoint='modify_article')
@login_required
def modify_article():
    """
    修改以及存在的文章
    :param
        title:原文章的标题
        modified_title: 修改之后的文章标题
        content: 文章内容
        article_type: 文章类型
    :return:
    最终客户端接收的数据格式：
            成功：{ "code":200,"msg":"修改成功~~","data":{} }
            失败：{ “code” = -1,msg = str(error),data = {} }
    """
    form = request.get_json(silent=True)
    try:
        model_article = Article.modify_article(form)
        db.session.add(model_article)
        db.session.commit()
    except Exception as error:
        return -1, str(error)
    else:
        return 201,"修改成功~~",Article.query.filter_by(title=form['title']).first().id

@api.route('/delete_article',methods=["POST"],endpoint='delete_article')
@login_required
def delete_article():
    """
    修改以及存在的文章
    :param
        title:文章的标题
    :return:
    最终客户端接收的数据格式：
            成功：{ "code":200,"msg":"删除成功~~","data":{} }
            失败：{ “code” = -1,msg = str(error),data = {} }
    """
    form = request.get_json(silent=True)
    try:
        model_article,model_comment = Article.delete_article(form)
        db.session.delete(model_article)
        # 不能直接删除，会报Class ‘__builtin__.list’ is not mapped错误
        for i in model_comment:
            db.session.delete(i)
        db.session.commit()
    except Exception as error:
        return -1, str(error)
    else:
        return "删除成功~~"

@api.route('/manage_draft',methods=["POST"],endpoint='manage_draft')
@login_required
def manage_draft():
    """
    :param
    type: 操作类型
    add:
    创建文章：
        title: 文章标题 不可为空
        content: 文章内容
    修改文章:
        id: 文章id
        title： 修改后的标题
        content: 文章内容
    delete:
        id: 文章id
    :return:
    最终客户端接收的数据格式：
            成功：{ "code":200,"msg":"xx成功~~","data":{} }
            失败：{ “code” = -1,msg = str(error),data = {} }
            add模式会在data中返回文章id：
              "code": 200,
              "data": 5,
              "msg": "添加成功~~"
    """
    form = request.get_json(silent=True)
    if form['type'] == 'add':
        # 判断有无id字段
        try:
            form['id']
        except KeyError as err:
            # 没有则执行创建程序
            try:
                model_draft = Draft.add_draft(form)
                db.session.add(model_draft)
                db.session.commit()
            except Exception as error:
                return -1, str(error)
            else:
                # 返回id数据
                this_article_id = Draft.query.filter_by(title=form['title']).first().id
                return 201,"添加成功~~",this_article_id
        else:
            # 有则执行修改程序
            try:
                model_draft = Draft.modify_draft(form)
                db.session.add(model_draft)
                db.session.commit()
            except Exception as error:
                return -1, str(error)
            else:
                # 返回id数据
                this_article_id = Draft.query.filter_by(title=form['title']).first().id
                return 201, "修改成功~~", this_article_id
    else:
        # 否则执行删除程序
        try:
            model_draft = Draft.delete_draft(form)
            db.session.delete(model_draft)
            db.session.commit()
        except Exception as error:
            return -1, str(error)
        else:
            return "删除成功~~"

@api.route('/manage_comment',methods=["POST"],endpoint='manage_comment')
@login_required
def manage_comment():
    """
    :param
    type: 操作类型
    add:
        article_id: 对应文章id
        content: 评论内容
        nickname: 评论者昵称
    delete:
        id: 自身id
        article_id: 对应文章id
    :return:
    最终客户端接收的数据格式：
            成功：{ "code":200,"msg":"xx成功~~","data":{} }
            失败：{ “code” = -1,msg = str(error),data = {} }
    """
    form = request.get_json(silent=True)
    if form['type'] == 'add':
        try:
            model_comment,model_article = Comment.add_comment(form)
            db.session.add(model_comment)
            # 对article表中的comment_times字段进行改变
            db.session.add(model_article)
            db.session.commit()
        except Exception as error:
            return -1, str(error)
        else:
            return "添加成功~~"
    if form['type'] == 'delete':
        try:
            model_comment,model_article = Comment.delete_comment(form)
            db.session.delete(model_comment)
            # 对article表中的comment_times字段进行改变
            db.session.add(model_article)
            db.session.commit()
        except Exception as error:
            return -1, str(error)
        else:
            return "删除成功~~"
