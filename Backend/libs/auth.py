from datetime import datetime, timedelta

import jwt
from flask import request

from config.base_setting import SECRET_WORD
from libs.return_data_helper import ops_renderJSON, ops_renderErrJSON


def jwt_login(form):
    """
    该函数在接收登录表单的数据之后返回加密的jwt token
    :param form: 登录表单
    :return: jwt token
    """
    now = datetime.utcnow()
    # 设置两小时后过期
    exp_datetime = now + timedelta(hours=6)
    # 通过用户名核对和密码验证之后返回jwt
    encoded_jwt = jwt.encode({
        'username': form.username.data,
        # exp是到期时间
        'exp': exp_datetime,
        # is_valid 是否有效，如果为false则就算在有效期内也被判定需要重新登录
        'is_valid':True
    }, SECRET_WORD, algorithm='HS256')

    return encoded_jwt.decode("utf-8")


def login_required(func):
    def wrapper(*args, **kw):
        # 测试token,从header中获取接收的token，并使用UTF-8进行编码，否则无法使用jwt.decode
        try:
            token = request.headers.get('Authorization', default=None).encode('utf-8')
            decode_token = jwt.decode(token,SECRET_WORD, algorithms=['HS256'])
        except Exception as err:
            return ops_renderErrJSON(msg='you need login~',data=str(err))
        else:
            # 将数值型的时间转换为datatime类型以比较 https://blog.csdn.net/weixin_41789707/article/details/83009235
            jwt_time = datetime.fromtimestamp(decode_token['exp'])
            if jwt_time < datetime.utcnow():
                return ops_renderErrJSON(msg='your jwt is out of time~')
            elif not decode_token['is_valid']:
                return ops_renderErrJSON(msg='you need login~')
            else:
                msg = func(*args, **kw)
                if msg[0] == -1:
                    return ops_renderErrJSON(msg=msg[1])
                else:
                    return ops_renderJSON(msg=msg)

    return wrapper
