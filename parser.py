import models
import requests
import config
import json
from bs4 import BeautifulSoup as bs
from telegraph import Telegraph
from datetime import datetime
import datetime as dt


def main_page_parse(site):
    url = site.url
    headers = {'User-Agent': config.user_agent}
    response = requests.get(url, headers=headers)
    soup = bs(response.text, 'html.parser')
    main_container = soup.find(
        site.container_tag, {"class": site.container_class})
    article_links = []
    for link in main_container.find_all(site.block_tag, {'class': site.block_class}):
        today = str(datetime.today()).split(' ')[0]
        article_date = str(datetime.fromtimestamp(
            int(link.find(site.time_format[0])[site.time_format[1]]))).split(' ')[0]
        if today == article_date:
            article_links.append({"link": link.find(site.block_link).get('href'), "title": link.find(site.block_text).get_text(), "date": int(link.find(site.time_format[0])[site.time_format[1]])})

    return article_links
