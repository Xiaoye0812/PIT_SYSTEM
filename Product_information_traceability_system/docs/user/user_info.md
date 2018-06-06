#### 获取当前用户信息接口

    GET /user/userinfo/

##### request请求



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