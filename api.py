#!/usr/bin/env python
# -*- coding:utf-8 -*-
# !/usr/bin/env python
# -*- coding:utf-8 -*-

import requests
import textwrap


def history_get():
    """ 历史上的今天api """
    url = 'https://www.ipip5.com/today/api.php?type=json'
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Safari/537.36"}
    response = requests.get(url, headers=headers)
    res = response.json()
    data = res.get('result')[:-1]
    history_text = ''
    score = 0
    for i in range(len(data)):
        text = data[i]['year'] + '年' + res['today'] + '，' + data[i]['title']
        if len(text) <= 28:
            if score > 5:
                break
            score += 1
            history_text += text + '\n\n'
    return history_text


def news_get():
    """
    知乎每日60s读懂世界内容爬虫
    :return:
    """
    url = 'https://60s.viki.moe/60s?v2=1'
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Safari/537.36"}
    response = requests.get(url, headers=headers)
    res = response.json()
    news_list = res['data']['news']
    verse = res['data']['tip']
    content = ''
    for index, news in enumerate(news_list):
        wrapped_text = textwrap.wrap(f'{index + 1}、{news}', width=28)
        title = '\n\n'.join(wrapped_text)
        content += title + '\n\n'
    wrapped_verse = textwrap.wrap(verse, 28)

    return content, wrapped_verse


def verse_get():
    """
    金山每日一言api
    :return:
    """
    url = 'https://open.iciba.com/dsapi/'
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Safari/537.36"}
    response = requests.get(url, headers=headers)
    res = response.json()
    verse = res['note']
    return [verse]


if __name__ == '__main__':
    print(news_get())
