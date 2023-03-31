#!/usr/bin/env python
# -*- coding:utf-8 -*-
# !/usr/bin/env python
# -*- coding:utf-8 -*-
# 历史上的今天api

import re
import requests
import textwrap


def history_get():
    url = 'https://www.ipip5.com/today/api.php?type=json'
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Safari/537.36"}
    response = requests.get(url, headers=headers)
    res = response.json()
    data = res.get('result')
    history_text = ''
    score = 0
    for i in range(len(data[:-1])):
        text = data[i]['year'] + '年' + res['today'] + '，' + data[i]['title']
        if score > 5:
            return history_text
        if len(text) <= 28:
            score += 1
            history_text += text + '\n\n'


if __name__ == '__main__':
    history_get()
