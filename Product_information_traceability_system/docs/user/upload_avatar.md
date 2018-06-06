#### 上传头像接口

    POST /user/upload/

##### request请求

    avatar      file 登录账号

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