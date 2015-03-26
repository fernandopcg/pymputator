#!/usr/bin/env python
from lxml import html
import requests
url = 'http://www.morse.es/gsp/asp/Maqueta2.asp' 
user = 'jln'
pwd = 'jlnpl8'

with requests.Session() as s:
    s.auth = (user, pwd)
    tree = html.fromstring(s.get(url).text)
    inputs = tree.xpath('//input')
    msg = 'Input {input_}: {value}'
    for input_ in inputs:
        print(msg.format(input_=input_, value=input_.items()))
    select = tree.xpath('//select')
    for selections in select:
        print selections.name
        for option in selections.getchildren():
            txt = option.text
            values = option.values()
            if 'selected' in values:
                print 'values = {values}'.format(values=values)
                print 'txt = {txt}'.format(txt=txt.encode('utf-8'))
