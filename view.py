from os import link
import parser

from requests.api import head
import config
import models
import parser
import json
import utils
import os
import time
from telegraph import Telegraph
import telebot

bot = telebot.TeleBot(
    os.getenv("USTECH_API_TOKEN"), parse_mode="Markdown")


def get_sites():
    sites = []
    for site in config.sites_catalog:
        model = models.Site.parse_raw(
            json.dumps(site))
        sites.append(model)
    return sites


def get_news():
    sites = get_sites()
    links = []
    for site in sites:
        links.append(site.get_today_articles())
    return links

def check_and_send():
    last_date = 0
    while True:
        links = get_news()
        for link in links:
            for i in reversed(link):
                if i['date'] > last_date:
                    last_date = i['date']
                    bot.send_message("@PendosiVIT", "*{0}*\n\n{1}".format(i['title'], i['link']))
        time.sleep(60*60)

check_and_send()

bot.polling()
