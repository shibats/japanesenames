#!/usr/bin/env python

from urllib import urlopen
import re
from time import sleep


def scrape(gender):
    print "Starting scraping for gender %d." % gender
    surl = "http://marugin.main.jp/babyname/initial.php"
    src = urlopen(surl).read()
    if gender == 0:
        pat = r'ID="tdInitialListCaptionMan"(.*)"dBInitialResult"'
    else:
        pat = r'ID="tdInitialListCaptionWoman"(.*)"dBInitialResult"'
    w_src = re.findall(pat, src, re.M | re.S)

    w_urls = re.findall(r'a href="(.+?)"', ''.join(w_src), re.M | re.S)
    d = {}
    name_list = []
    for n, u in enumerate(w_urls):
        print "Processing %d of %d" % (n+1, len(w_urls))
        src = urlopen(surl + u).read()
        sleep(1)       # wait 1 second each time after reading a url
        if gender == 0:
            pat = (r"""</TD><TR CLASS='trSearchResultList1'>(.+?)"""
                    """<DIV CLASS="dMAdsenceRectangle">""")
        else:
            pat = (r"""</TD><TR CLASS='trSearchResultList2'>(.+?)"""
                    """<DIV CLASS="dMAdsenceRectangle">""")
        s_src = re.findall(pat, src, re.M | re.S)
        s_src = unicode(''.join(s_src), 'euc-jp')
        if gender == 0:
            pat2 = (r"""<TR CLASS='trSearchResultList1'>.+?CLASS='nameLink1'>"""
                    """(.+?)</A>.+?CLASS='nameLink1'>(.+?)</A>""")
        else:
            pat2 = (r"""<TR CLASS='trSearchResultList2'>.+?CLASS='nameLink2'>"""
                    """(.+?)</A>.+?CLASS='nameLink2'>(.+?)</A>""")
        s_list = re.findall(pat2, s_src, re.M | re.S)
        for i in s_list:
            name_list.append('%s\t%s' % (i[0], i[1]))
    print "Got %d names" % len(name_list)
    return name_list
    