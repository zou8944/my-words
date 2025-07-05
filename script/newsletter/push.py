import httpx

import config


def push_deer(msg: str):
    url = f"https://api2.pushdeer.com/message/push?pushkey={config.settings.push_deer_key}&text={msg}"
    res = httpx.get(url, timeout=10)
    if res.status_code != 200:
        raise Exception(f"PushDeer推送失败: {res.status_code} - {res.text}")
    data = res.json()
    if data.get("code") != 0:
        raise Exception(f"PushDeer推送失败: {data.get('code')} - {data.get('message')}")
