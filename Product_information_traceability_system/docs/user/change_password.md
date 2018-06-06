#### 管理员修改密码接口

    POST /user/changepassword/

##### request请求

    old_password        str 管理员旧密码
    new_password        str 管理员新密码

##### response响应

###### 成功响应

    {
        'code': 200,
        'msg': '请求成功'
    }

###### 失败响应1

    {
        'code': 900,
        'msg': '访问数据库出错'
    }

###### 失败响应2

    {
        'code': 1001,
        'msg': '密码错误'
    }