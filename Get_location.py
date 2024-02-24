import requests

def get_location():
    response = requests.get("https://ip.cn/api/index?ip&type=0")
    return response.json()["ip"] + response.json()["address"]