#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import re
from bs4 import BeautifulSoup
f = open('simple-elements.xml').read()
soup = BeautifulSoup(f)

for page in soup.find_all('page'):
  title = page.title.string
  if (not re.search('Template', page.title.string)):
    text = page.text
    for (language, label) in re.findall('\[\[([a-z][a-z]):(.+)\]\]', text):
      print title + "\t" + language + "\t" + label
