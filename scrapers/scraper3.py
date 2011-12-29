#!/usr/bin/env python

from urllib import urlopen
import re
import sys
from time import sleep


def scrape(gender):
    print "Starting scraping for gender %d." % gender
    surl = "http://babyname.bj-town.com/babyname/list_a.html"
    
    src = urlopen(surl).read()
    w_src = re.findall(r'<div id="image_.+?"><a href="(.+?)" target="_self"', src,
                       re.M | re.S)
    w_urls = [surl] + w_src
    
    d = {}
    name_list = []
    
    for n, u in enumerate(w_urls):
        print "Processing %d of %d" % (n+1, len(w_urls))
        src = unicode(urlopen(u).read(), 'utf-8', 'replace')
        sleep(1)       # wait 1 second each time after reading a url
        if gender == 0:
            pat = r"""<table class="boy">.+?</table>"""
        else:
            pat = r"""<table class="girl">.+?</table>"""
        s_src = ''.join(re.findall(pat, src, re.M | re.S))
        if gender == 0:
            pat2 = (r"""<td class="boy_kana">(.+?)<.+?"""
                     """<td class="boy_kanji">(.+?)</td>""")
        else:
            pat2 = (r"""<td class="girl_kana">(.+?)<.+?"""
                     """<td class="girl_kanji">(.+?)</td>""")
        s_list = re.findall(pat2, s_src, re.M | re.S)
        for furi, kanji in s_list:
            try:
                if gender == 0:
                    if '<BR>' in kanji:
                        k_list = [x.strip() for x in kanji.split('<BR>')]
                    else:
                        k_list = [x.strip() for x in kanji.split('<br />')]
                else:
                    if '<BR>' in kanji:
                        k_list = [x.strip() for x in kanji.split('<BR>')]
                    else:
                        k_list = [x.strip() for x in kanji.split('<br />')]
                for k in k_list:
                    name_list.append('%s\t%s' % (k, furi))
            except:
                pass
    print "Got %d names" % len(name_list)
    return name_list

if __name__ == '__main__':
    l = scrape(0)
    for i in l:
        print i