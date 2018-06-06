#### 删除产品接口

    POST /product/delproduct/

##### request请求

    product_id      int 产品编号

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
        'code': 2000,
        'msg': '产品不存在'
    }

###### 失败响应3

    {
        'code': 900,
        'msg': '访问数据库出错'
    }
