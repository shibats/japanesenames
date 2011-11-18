#!/usr/bin/env python

from urllib import urlopen
import re
import sys


def scrape(gender):
    print "Starting scraping for gender %d." % gender
    if gender == 0:
        surl = "http://babyname.ojaru.jp/man/otoko-a.htm"
    else:
        surl = "http://babyname.ojaru.jp/women/onna-a.htm"
    
    src = urlopen(surl).read()
    w_src = re.findall(r'#ffffc8">&nbsp;<A href="(.+?)" target="_self"', src,
                       re.M | re.S)
    w_urls = [surl] + w_src
    
    d = {}
    name_list = []
    
    for n, u in enumerate(w_urls):
        print "Processing %d of %d" % (n+1, len(w_urls))
        src = urlopen(u).read()
        sleep(1)       # wait 1 second each time after reading a url
        pat = (r"""<TD colspan="2" style="font-size : 14px;"""
                """font-weight : bold;color : white;.+?</TR>(.+?)</TBODY>""")
        s_src = re.findall(pat, src, re.M | re.S)
        s_src = ''.join([unicode(x, 'shift-jis') for x in s_src])
        s_list = re.findall(r'<TR>(.+?)</TR>', s_src, re.M | re.S)
        for i in s_list:
            i2 = re.findall(r'<TD.+?>(.+?)</TD>.+?<TD.+?>(.+?)</TD>', i,
                            re.M | re.S)
            try:
                furi = i2[0][0]
                k_list = i2[0][1]
                k_list2 = [x.strip() for x in k_list.split('<BR>')]
                for j in k_list2:
                    d[j] = furi
                    name_list.append('%s\t%s' % (j, furi))
            except:
                pass
    print "Got %d names" % len(name_list)
    return name_list
