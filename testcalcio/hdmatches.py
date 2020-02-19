# -*- coding: utf-8 -*-
# ------------------------------------------------------------
# Canale per hdmatches
# ------------------------------------------------------------
import re

from specials import filtertools
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
from core.support import log
def peliculas(item):
      log()
      itemlist = []
      data = httptools.downloadpage(item.url, headers=headers).data
log(data)
