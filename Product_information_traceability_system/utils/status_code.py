# 通用响应

SUCCESS = {'code': 200, 'msg': '请求成功'}
DATABASE_ERROR = {'code': 900, 'msg': '访问数据库出错'}
PARAMS_ERROR = {'code': 901, 'msg': '参数错误'}
SEARCH_RESULT_IS_NULL = {'code': 201, 'msg': '搜索结果为空'}

# 用户模块

USER_IS_NOT_EXISTS = {'code': 1000, 'msg': '用户名不存在'}
USER_PASSWORD_ERROR = {'code': 1001, 'msg': '密码错误'}
USER_NOT_LOGIN = {'code': 1002, 'msg': '请先登录'}
USER_NOT_MANAGER = {'code': 1003, 'msg': '没有权限进行此操作'}
USER_CAN_NOT_DEL_MANAGER = {'code': 1004, 'msg': '不能删除管理员'}
USER_IS_ALREADY_EXISTS = {'code': 1005, 'msg': '用户编号已存在'}
USER_CAN_NOT_CHANGE_MANAGER = {'code': 1006, 'msg': '不能修改管理员'}

# 产品模块

PRODUCT_IS_NOT_EXISTS = {'code': 2000, 'msg': '产品不存在'}
PRODUCT_IS_EXISTS = {'code': 2001, 'msg': '产品编号已存在'}
PRODUCT_NOT_YOURS = {'code': 2002, 'msg': '这不是你质检的产品'}
PRODUCT_NOT_GET_MANAGER = {'code': 2003, 'msg': '产品不能分配给管理员'}
PRODUCT_ALREADY_CHANGED = {'code': 2004, 'msg': '产品已质检，不可更改'}
