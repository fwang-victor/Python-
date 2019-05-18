import json
import requests
from wxpy import *

def Get_Text_message(message):
    url = 'http://openapi.tuling123.com/openapi/api/v2'
    api_key = 'b8cb68f90670494cb03272beaa522423'
    info = {
    "perception": {
        "inputText": {
            "text":message
        },
    },
    "userInfo": {
        "apiKey":api_key,
        "userId": "wechat"
    }
}
    rep = requests.post(url,data = json.dumps(info).encode('utf8'))
    result = json.loads(rep.text)
    rs = result['results'][0]['values']['text']
    return rs

#
bot = Bot(cache_path=True) # 初始化机器人对象
chat_groups = bot.groups().search('机器人总动员')[0] #获取聊天群对象
chat_self = bot.groups().search('二环上的帅哥美女')[0]


@bot.register([chat_groups,chat_self],TEXT)
def Auto_reply_Text(msg):
    return Get_Text_message(msg.text)
#
embed()
