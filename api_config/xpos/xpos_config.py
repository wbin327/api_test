# coding:utf-8


header = {
    'Content-Type': 'application/json',
}


body = {
    'add_client_mobileandemail': {
            "cardCore": "",         # 卡芯码
            "email": "",            # 邮箱，非必填
            "mobile": ""            # 电话号码，非必填
    },
    'advertise_image': {

    },
    'cash_receipt': {
        "orderLegalAmountStr": "",  # 下单法币金额
        "actualLegalAmountStr": ""  # 实收法币金额
    },
    'confirm_consumer_order': {
        "merchantOrderNo": "",      # 数字货币订单号
        "cardCoreCode": "",         # 卡芯码
        "authCode": "",             # des加密后的数据
        "authNumber": ""            # 芯片生成密钥的次数
    },
    'create_consumer_order': {
        "orderAmountStr": 0,        # 下单金额
        "orderUnit": "",            # 下单单位
        "chargeUnit": "",           # 交易单位
        "type": 0                   # 下单定价方式       0：现金定价 1:数字货币定价
    },
    'create_websocket_token': {

    },
    'digital_currency': {
        "status": 0,                # 状态；0表示下线，1:上线，2:删除
    },
    'find_card_balance': {
        'cardCode': '',             # 卡芯码
        'authCode': '',             # 卡片认证结果
        'authNumber': '',           # 卡片内部认证次数
        'randomCode': '',           # 查卡时生成随机数
    },
    'get_card_secret': {
        'coreCode': '',             # 卡芯码
    },
    'jobnum_login': {
        'imeiCode': '',             # pos机Imei码
        'jobNumber': '',            # 工号
        'passWord': '',             # 密码
        'ip': '',                   # 登陆pos机ip
        'posVersion': '',           # pos版本号
    },
    'logininfo_refresh': {

    },
    'mobile_code': {
        'mobile': '',               # 电话号码
    },
    'mobile_login': {
        'imeiCode': '',             # posimei
        'mobile': '',               # 电话号码
        'verify': '',               # 验证码
        'ip': '',                   # pos机ip地址
        'posVersion': '',           # pos机版本号
        'loginType': '',            # 登陆类型
    },
    'mobileoremail_login': {
        'imeiCode': '',             # posimei
        'userName': '',             # 手机号码或邮箱
        'password': '',             # 密码
        'ip': '',                   # pos机ip地址
        'posVersion': '',           # pos机版本号
        'loginType': '',            # 登陆类型
    },
    'restart_consumer_order': {
        'merchantOrderNo': '',      # 数字货币订单号
    },
    'search_merchant_tax': {

    },
    'search_card': {
        "cardCode": "",             # 卡芯码
    },
    'search_order_detail': {
        "orderNo": '',              # 订单号
    },
    'search_order_list': {
        "dtBegin": '',              # 统计开始时间
        "dtEnd": '',                # 统计结束时间
        "pageIndex": '',            # 当前页码，默认第一页
        "pageSize": '',             # 每页显示长度，默认20
        "type": '',                 # -1查询所有消费订单，0查询现金收银消费订单，1查询数字货币收银消费订单
    },
    'search_random': {
        "randomCode": "",           # 随机数
    },
    'write_card_secret': {
        'coreCode': '',             # 卡芯码
        'authCode': '',             # 卡片认证结果
        'authNumber': '',           # 卡片内部认证次数
    },
    'create_user_order': {
        "merchantOrderNo": '',      # 商户订单号
        "qrCode": '',               # 二维码
    },
    'cancel_merchant_consume': {
        "merchantOrderNo": '',      # 数字货币订单号
    },

}


url = {
    'add_client_mobileandemail': '/apiMerchantPos/api/card/addClientMobileAndEmail',
    'advertise_image': '/apiMerchantPos/api/advertise/image',
    'cash_receipt': '/apiMerchantPos/api/v1/merchant/charge/cashReceipt',
    'confirm_consumer_order': '/apiMerchantPos/api/v1/merchant/charge/confirmConsumerOrderByCard',
    'create_consumer_order': '/apiMerchantPos/api/v1/merchant/charge/createConsumerOrder',
    'create_websocket_token': '/apiMerchantPos/api/posWebSocket/creatWebSocketToken',
    'digital_currency': '/apiMerchantPos/api/basicData/digitalCurrency/list',
    'find_card_balance': '/apiMerchantPos/api/card/findCardBalanceBycardNo',
    'get_card_secret': '/apiMerchantPos/api/card/getCardSecret',
    'jobnum_login': '/apiMerchantPos/api/login/jobnum',
    'logininfo_refresh': '/apiMerchantPos/api/loginInfo/refresh',
    'mobile_code': '/apiMerchantPos/api/mobileCode/get',
    'mobile_login': '/apiMerchantPos/api/login/mobile',
    'mobileoremail_login': '/apiMerchantPos/api/login/mobileOremail',
    'restart_consumer_order': '/apiMerchantPos/api/v1/merchant/charge/restartConsumerOrder',
    'search_card': '/apiMerchantPos/api/card/searchCard',
    'search_order_detail': '/apiMerchantPos/api/v1/merchant/charge/searchOrderDetailByOrderNo',
    'search_order_list': '/apiMerchantPos/api/v1/merchant/charge/searchOrderListByUserId',
    'search_random': '/apiMerchantPos/api/card/searchRandom',
    'write_card_secret': '/apiMerchantPos/api/card/writeCardSecret',
    'search_merchant_tax': '/apiMerchantPos/api/v1/merchant/charge/searchMerchantTax',
    'create_user_order': '/apiMerchantPos/api/v1/merchant/charge/createUserOrderByQrCode',
    'cancel_merchant_consume': '/apiMerchantPos/api/v1/merchant/charge/cancleMerchantConsumeOrder',
}