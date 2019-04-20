# coding:utf-8


header = {
    'Content-Type': 'application/json',
}


body = {
    'add_client_mobileandemail': {
            "cardCore": "",         # 卡芯码
            "email": "",            # 邮箱，非必填
            "mobile": ""            # 电话号码，非必填
    }
}


url = {
    'add_client_mobileandemail': '/addClientMobileAndEmail',
}
