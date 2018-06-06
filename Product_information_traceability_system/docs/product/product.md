#### 搜索产品接口

    POST /product/product/

##### request请求

    product_info        str 搜索信息

##### response响应

###### 成功响应

    {
        'code': 200,
        'product_list': [
            {
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
            }
        ]
    }

###### 失败响应1

    {
        'code': 201,
        'msg': '搜索结果为空'
    }