from acm.oj import OJ
import json

user = OJ(user_id='2021213532',
          password='Dh213546879',

          mode='校外',           # 访问模式 [校内/校外]
          code_mode='自动',       # 验证码识别模式 [自动/手动]
          wvpn_token='ff3cdec221dec8e5'
          ).login()
#user.save("data1.json")

# user = OJ('2021213532', 'dh213546879', wvpn_token='6c115ea6072f7793').login()
user.submit_test_code()