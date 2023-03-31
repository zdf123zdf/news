#!/usr/bin/env python
# -*- coding:utf-8 -*-

import datetime
import os
from PIL import Image, ImageFont, ImageDraw
from time import time, localtime, strftime
from ZhNews import news_get
from HistoryToday import history_get
from zhdate import ZhDate

news_text = news_get()[0]
verse = news_get()[1]
history_text = history_get()

# 字体
font_path = "./font/SIMYOU.TTF"
font_path1 = "./font/GB2312.ttf"
font_path2 = "./font/SourceHanSerifSC-Bold.otf"


def background():
    """ 布局背景生成 """
    bg_size = (1, 1)
    bg_small = (980, 330)
    img = Image.new("RGBA", bg_size, (245, 245, 245))
    draw = ImageDraw.Draw(img)
    # 根据文字内容高度来调整图片高度
    font_news = ImageFont.truetype(font_path, 35)
    text_bbox = draw.textbbox((0, 0), news_text, font=font_news)
    text_height = text_bbox[3] - text_bbox[1]

    pic_height = 980 + text_height + 80
    bg_size = (1080, pic_height)
    img = Image.new("RGBA", bg_size, (245, 245, 245))
    draw = ImageDraw.Draw(img)

    w, h = bg_small
    # 左上角坐标
    x, y = (50, 50)
    # 圆角直径
    r = 30
    # Rounds
    draw.ellipse((x, y, x + r, y + r), fill=(234, 98, 40))
    draw.ellipse((x + w - r, y, x + w, y + r), fill=(234, 98, 40))
    draw.ellipse((x, y + h - r, x + r, y + h), fill=(234, 98, 40))
    draw.ellipse((x + w - r, y + h - r, x + w, y + h), fill=(234, 98, 40))
    # rec.s
    draw.rectangle((x + r / 2, y, x + w - (r / 2), y + h), fill=(234, 98, 40))
    draw.rectangle((x, y + r / 2, x + w, y + h - (r / 2)), fill=(234, 98, 40))

    # 画线
    draw.line((50, 440, 1030, 440), (66, 66, 65), width=5)  # 线的起点和终点，线宽
    draw.line((50, 580, 1030, 580), (189, 192, 200), width=3)

    draw.line((25, 25, 25, pic_height - 40), (189, 192, 200), width=3)
    draw.line((25, 25, 1055, 25), (189, 192, 200), width=3)
    draw.line((1055, 25, 1055, pic_height - 40), (189, 192, 200), width=3)
    draw.line((25, pic_height - 40, 1055, pic_height - 40), (189, 192, 200), width=3)

    draw_text(draw)
    return img


def draw_text(draw):
    """ 图片内容 """
    today = int(strftime("%w"))
    # 英文星期几
    weeks = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']
    text = weeks[today]
    font = ImageFont.truetype(font_path2, 35, encoding="utf-8")
    text_bbox = draw.textbbox((0, 0), text, font=font)
    text_width = text_bbox[2] - text_bbox[0]
    x = (1080 - text_width) // 2
    draw.text((x, 100), text, font=font, spacing=1000, fill=(255, 255, 255))

    # 中文星期几
    weeks_cn = ['星期日', '星期一', '星期二', '星期三', '星期四', '星期五', '星期六']
    text = weeks_cn[today]
    font = ImageFont.truetype(font_path1, 120, encoding="utf-8")
    text_bbox = draw.textbbox((0, 0), text, font=font)
    text_width = text_bbox[2] - text_bbox[0]
    # 计算文本绘制的起始坐标
    x = (1080 - text_width) // 2
    draw.text((x, 150), text, font=font, fill=(255, 255, 255))

    # 微语
    # 计算文本所需的宽度和高度
    text = verse
    font = ImageFont.truetype(font_path1, 30, encoding="utf-8")
    text_bbox = draw.textbbox((0, 0), text, font=font)
    text_width = text_bbox[2] - text_bbox[0]
    # 计算文本绘制的起始坐标
    x = (1080 - text_width) // 2
    # 绘制文本
    draw.text((x, 280), text, font=font, fill=(255, 255, 255))

    font = ImageFont.truetype(font_path2, 30, encoding="utf-8")
    draw.text((50, 390), 'NEWS', font=font, fill=(220, 99, 98))

    font_small = ImageFont.truetype(font_path1, 35)
    draw.text((50, 470), "农历", font=font_small, fill=(0, 0, 0))
    draw.text((50, 520), lunar_calendar(), font=font_small, fill=(0, 0, 0))
    draw.text((910, 470), strftime("%Y年", localtime(time())), font=font_small, fill=(0, 0, 0))
    draw.text((870, 520), strftime("%m月%d日", localtime(time())), font=font_small, fill=(0, 0, 0))

    font = ImageFont.truetype(font_path1, 50, encoding="utf-8")
    draw.text((320, 485), '每天60秒读懂世界', font=font, fill=(220, 99, 98))

    font_news = ImageFont.truetype(font_path, 35)

    # 历史上的今天部分
    draw.text((50, 600), history_get(), font=font_news, fill=(0, 0, 0))

    draw.line((50, 990, 1030, 990), (189, 192, 200), width=3)

    # 60s新闻部分
    draw.text((50, 1020), news_text, font=font_news, fill=(0, 0, 0))

    return draw


def lunar_calendar():
    """ 农历转换 """
    day = str(ZhDate.today())
    day = day[7:]
    return day


def save_img(img):
    """ 保存图片 """
    # 时间戳生成
    datetime_dt = datetime.datetime.today()
    datetime_str = datetime_dt.strftime("%m-%d")

    img_path = os.path.join(f'news-{datetime_str}.png')
    img.save(img_path)
    print('保存成功 at {}'.format(img_path))


if __name__ == '__main__':
    save_img(background())
