#### 修改质检员信息接口

    POST /user/changeinspector/

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
        'code': 901,
        'msg': '参数错误'
    }

###### 失败响应2

    {
        'code': 900,
        'msg': '访问数据库出错'
    }

###### 失败响应3

    {
        'code': 1000,
        'msg': '用户名不存在'
    }

###### 失败响应4

    {
        'code': 1006,
        'msg': '不能修改管理员'
    }

###### 失败响应5

    {
        'code': 1003,
        'msg': '没有权限进行此操作'
    }