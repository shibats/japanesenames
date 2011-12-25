#!/usr/bin/env python
# -*- coding: utf-8 -*-

from urllib import urlopen
import re
import sys
from time import sleep


def scrape(gender):
    print "Starting scraping for gender %d." % gender
    if gender == 0:
        surl = "http://www.seimeihandan.net/guide/name-boy.asp"
    else:
        surl = "http://www.seimeihandan.net/guide/name-girl.asp"
    src = urlopen(surl).read()
    w_src = re.findall(r'bgcolor="#cccccc">(.+?)width="1" height="10">', src,
                       re.M | re.S)
    w_urls = re.findall(r'<td.+?><a href="(.+?)">', w_src[0],
                       re.M | re.S)
    base = 'http://www.seimeihandan.net/guide/'
    w_urls = [base+x for x in w_urls]
    d = {}
    name_list = []
    
    for n, u in enumerate(w_urls):
        print "Processing %d of %d" % (n+1, len(w_urls))
        src = urlopen(u).read()
        sleep(1)       # wait 1 second each time after reading a url
        pat = r'<font class="text36-40">(.+?)</font><br>'
        yomil = ''.join(re.findall(pat, src))
        pat1 = ur'<tr bgcolor=#ffffff>(.+?)cellpadding="3" width="510">'
        p_src = ''.join(re.findall(pat1, src, re.M | re.S))
        s_list = []
        if yomil:
            yomi = unicode(yomil, 'shift-jis')
            pat2 = r"""^<td>(.+?)<br></td>"""
            s_list = re.findall(pat2, p_src, re.M | re.S)
            for i in s_list:
                name_list.append('%s\t%s' % (unicode(i, 'shift-jis'), yomi))
    print "Got %d names" % len(name_list)
    return name_list

if __name__ == '__main__':
    l = scrape(0)
    for i in l:
        print i
