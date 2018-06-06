#### 登录接口

    POST /user/login/

##### request请求

    username        str 用户账号
    password        str 用户密码

##### response响应

###### 成功响应

    {
        'code': 200,
        'user_info': {
            'id': 用户编号,
            'avatar': 头像,
            'name': 姓名,
            'type': 身份 0为管理员 1为质检员
        }
    }

###### 失败响应1

    {
        'code': 1000,
        'msg': '用户名不存在'
    }

###### 失败响应2

    {
        'code': 1001,
        'msg': '密码错误'
    }