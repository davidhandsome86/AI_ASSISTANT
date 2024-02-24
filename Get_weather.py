import requests
from pypinyin import pinyin, lazy_pinyin, Style
from Get_location import *

api_key = '' your api_key

def get_weather(): # get current weather in your location
    location = ''.join(lazy_pinyin(get_location())[4:6])
    url = 'https://api.seniverse.com/v3/weather/now.json'
    response = requests.get(url, params={
        'key': api_key,
        'location': location,
        'language': 'zh-Hans',
        'unit': 'c'
    }, timeout=1)
    results = response.json()["results"][0]["now"]
    content = '天气状况' + ":" + results["text"]  + ";" + '温度' + ":" + results["temperature"] + " °C"
    return content

def get_weather_n(n): #get n day weather in your location
    n = int(n)
    location = ''.join(lazy_pinyin(get_location())[4:6])
    url = 'https://api.seniverse.com/v3/weather/daily.json'
    response = requests.get(url, params={
        'key': api_key,
        'location': location,
        'language': 'zh-Hans',
        'unit': 'c',
        'start': 0,
        'days': n
    }, timeout=1)
    loca = response.json()["results"][0]["location"]["name"] + "地区 "
    results = response.json()["results"][0]["daily"]
    data = ''
    for i in range(n):
        date = "日期" + ':"' + results[i]["date"] + '" '  # 日期
        text_day = "白天天气状况" + ':"' + results[i]["text_day"] + '" '  # 白天天气现象文字
        text_night = "夜间天气状况" + ':"' + results[i]["text_night"] + '" '  # 晚间天气现象文字
        high = "最高温度" + ':"' + results[n - 1]["high"] + '" '  # 当天最高温度
        low = "最低温度" + ':"' + results[n - 1]["low"] + '" '  # 当天最低温度
        precip = "降水概率" + ':"' + results[n - 1]["precip"] + '" '  #  降水概率
        rainfall = "降水量" + ':"' + results[n - 1]["rainfall"] + '" '  #  降水量
        wind_direction = "风向" + ':"' + results[n - 1]["wind_direction"] + '" '  # 风向文字
        wind_speed = "风速" + ':"' + results[n - 1]["wind_speed"] + '" '  # 风速
        wind_scale = "风力等级" + ':"' + results[n - 1]["wind_scale"] + '" '  # 风力等级
        humidity = "相对湿度" + ':"' + results[n - 1]["humidity"] + '" '  # 相对湿度
        data = data+date+text_day+text_night+high+low+precip+rainfall+wind_direction+wind_speed+wind_scale+humidity
    return loca + data
    
