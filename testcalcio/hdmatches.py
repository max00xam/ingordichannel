# -*- coding: utf-8 -*-
# ------------------------------------------------------------
# Canale per cinemastreaming
# ------------------------------------------------------------
import re

from channels import filtertools
from core import scrapertools, servertools, httptools
from core.item import Item
from platformcode import config
host = 'https://hdmatches.com/'
headers = [['Referer', host]]
def mainlist(item):
      itemlist = [Item(channel = item.channel,
                       contentType = 'movie',
                       title = 'Film',
                       url = host + '/category/serie-a/',
                       action = 'peliculas',
                       thumbnail = '',
                       fanart = ''
                       ),
      ]
      return itemlist
from channels.support import log
def mainlist(item):
log()
      itemlist = [Item(channel = item.channel,
                       contentType = 'movie',
                       title = 'Film',
                       url = host + '/category/serie-a/',
                       action = 'peliculas',
                       thumbnail = '',
                       fanart = ''
      ),
      ]
return itemlist
def peliculas(item):
    log()
    itemlist = []
    data = httptools.downloadpage(item.url, headers=headers).data
    block = scrapertools.find_single_match(data, r'<main>(.*?)<\/main>')
