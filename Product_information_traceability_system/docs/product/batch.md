#### 批次信息接口

    GET /product/batch/

##### request请求



##### response响应

###### 成功响应

    {
        'code': 200,
        'batch_list': [
            {
                'batch_id': 批次编号,
                'create_time': 创建时间,
                'update_time': 更新时间
            },
        ]

    }

###### 失败响应1

