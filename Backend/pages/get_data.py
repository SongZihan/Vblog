from flask import Blueprint, request

from application import db
from libs.return_data_helper import ops_renderJSON, ops_renderErrJSON
from models.user import User, Article, Draft, Comment

get_data = Blueprint("get_data", __name__)

@get_data.route('/homepage',methods=["GET"])
def homepage():
    """
    响应页面数据加载请求
    :return:
    数据类型：列表
    [(1, '修改后的标题', '测试用分类', “2020-06-05 10:18:36”)]
    """
    data = Article.get_homepage()

    return ops_renderJSON(data=data)

@get_data.route('/get_one_page',methods=["GET"])
def get_one_page():
    """
    响应具体页面的加载请求，返回特定文章的全部信息，包含评论
    :param
        id: 文章id，添加在get请求中，http://localhost:5000/get_data/get_one_page?id=2
    :return:
            {
          "code": 200,
          "data": [
            [
              1,
              "修改后的标题",
              "## 测试用内容 修改过了",
              "测试用分类",
              "2020-06-04 16:53:45",
              "2020-06-03 21:12:08",
              2,
              0
            ],
            [
              [
                2,
                "## 测试用评论",
                "喜喜",
                "2020-06-05 15:38:12"
              ],
              [
                3,
                "## 测试用评论2",
                "popp",
                "2020-06-05 15:38:21"
              ]
            ]
          ],
          "msg": "操作成功~~"
        }
    """
    id = request.args.get('id')
    data,model_article = Article.get_one_article(id)
    # 将阅读数加一添加到数据库中
    try:
        db.session.add(model_article)
        db.session.commit()
    except Exception as error:
        return ops_renderErrJSON(msg=str(error))
    else:
        return ops_renderJSON(data=data)

@get_data.route('/get_draft',methods=["GET"])
def get_draft():
    """
    响应页面数据加载请求
    :return:
    数据类型：列表
    [(1, '你好啊', ''), (2, 'ppp', '你的名字是？'), (3, '不可为空ma?', '可为空66666'), (5, '第二次创建', '可为空66666'), (6, 'xin的文章', 'xixihaha'), (7, '测试用草稿6', '')]
    """
    data = Draft.get_draft()

    return ops_renderJSON(data=data)
