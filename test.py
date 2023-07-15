# 读取配置文件
import json

with open('config.json', 'r') as configfile:
    config = json.load(configfile)

# 获取配置值
value = config['ksid']

print(value)
