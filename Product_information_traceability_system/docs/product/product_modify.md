#### 修改产品信息接口

    POST /product/changeproduct/

##### request请求

    batch_id        int 批次编号
    name            str 产品名称
    desc            str 产品描述
    product_id      int 产品编号
    inspector_id    int 质检员编号

    product_image   file 产品图片

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
        'code': 1003,
        'msg': '没有权限进行此操作'
    }

###### 失败响应3

    {
        'code': 900,
        'msg': '访问数据库出错'
    }

###### 失败响应4

    {
        'code': 2003,
        'msg': '产品不能分配给管理员'
    }

###### 失败响应5

    {
        'code': 1000,
        'msg': '用户名不存在'
    }

###### 失败响应6

    {
        'code': 2000,
        'msg': '产品不存在'
    }