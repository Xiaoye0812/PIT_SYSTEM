#### 产品详情接口

    POST /product/productinfo/

##### request请求

    product_id        str 产品编号

##### response响应

###### 成功响应

    {
        'code': 200,
        'product_list': {
            'id': 产品编号,
            'name': 产品名称,
            'batch': 产品批次,
            'desc': 产品描述,
            'status': 产品质检状态 0为未质检 1为质检通过 2为质检未通过,
            'detection_time': 质检时间,
            'create_time': 创建产品时间,
            'update_time': 更新状态时间,
            'inspector': 质检员姓名,
            'image': 产品图片
        },
        'user_info': {
            'id': 用户编号,
            'avatar': 头像,
            'name': 姓名,
            'type': 身份 0为管理员 1为质检员
        }

    }

###### 失败响应1

    {
        'code': 201,
        'msg': '搜索结果为空'
    }