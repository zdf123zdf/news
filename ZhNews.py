#!/usr/bin/env python
# -*- coding:utf-8 -*-
# 知乎每日60s读懂世界内容爬虫

import re
import requests
import textwrap


def news_get():
    url = 'https://www.zhihu.com/api/v4/columns/c_1261258401923026944/items'
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Safari/537.36"}
    response = requests.get(url, headers=headers)
    res = response.json()
    content = res['data'][0]['content']
    pat = r'>(.*?)<'
    rst = re.compile(pat, re.S).findall(content)
    rst = [i for i in rst if i != '']
    news_list = rst[2:-1]
    verse = rst[-1].lstrip('【微语】')
    news = ''
    for index in range(len(news_list)):
        if index > 14:
            return news, verse
        title = news_list[index]
        wrapped_text = textwrap.wrap(title, width=28)
        title = '\n\n'.join(wrapped_text)
        news += title + '\n\n'


if __name__ == '__main__':
    news_get()
