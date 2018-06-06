#### 搜索质检员接口

    POST /user/inspector/

##### request请求

    search_info         str 搜索信息

##### response响应

###### 成功响应

    {
        'code': 200,
        'inspector_list': [
            {
                'id': 质检员编号,
                'avatar': 头像,
                'name': 名字,
                'username': 登录账号,
                'password': 登录密码,
                'type': 类型 0为管理员 1为质检员
            },
        ]
    }

###### 失败响应1

    {
        'code': 1003,
        'msg': '没有权限进行此操作'
    }

###### 失败响应2

    {
        'code': 201,
        'msg': '搜索结果为空'
    }