#### 添加质检员接口

    POST /user/addinspector/

##### request请求

    username        str 登录账号
    name            str 姓名
    password        str 密码
    inspector_id    str 质检员编号

##### response响应

###### 成功响应

    {
        'code': 200,
        'msg': '请求成功'
    }

###### 失败响应1

    {
        'code': 1003,
        'msg': '没有权限进行此操作'
    }

###### 失败响应2

    {
        'code': 901,
        'msg': '参数错误'
    }

###### 失败响应3

    {
        'code': 1005,
        'msg': '用户编号已存在'
    }

###### 失败响应4
    {
        'code': 900,
        'msg': '访问数据库出错'
    }