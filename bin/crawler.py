#! /usr/bin/python
# -*- coding: utf-8 -*-

import urllib
import urllib2
import cookielib
from utils import TimeUtil

class LeaderBoard(object):

    def __init__(self):
        self.top_url = 'https://www.kaggle.com/c/6277/leaderboard.json?includeBeforeUser=false&includeAfterUser=false'
        self.all_url = 'https://www.kaggle.com/c/6277/leaderboard.json?includeBeforeUser=true&includeAfterUser=false'
        self.lb_pt = '/home/houjianpeng/kaggle-quora-question-pairs/data/leaderboard/'

        self.operate = '' # response对象(不含read)
        self.cj = cookielib.CookieJar()
        self.opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(self.cj))
        urllib2.install_opener(self.opener)

    def download_rank(self):
        self.operate = self._get_response(self.all_url)
        web_content = self.operate.read()
        self._save_data(web_content)

    def _save_data(self, data):
        f = open('%s/lb_%s.txt' % (self.lb_pt, TimeUtil.t_now_YmdH()), 'w')
        f.write('%s\n' % data)
        f.close()

    def _get_response(self, url, data=None):
        """
        获取响应
        :param url:
        :param data:
        :return:
        """
        if data is not None:
            req = urllib2.Request(url, urllib.urlencode(data))
        else:
            req = urllib2.Request(url)

        response = self.opener.open(req)
        return response

if __name__ == "__main__":
    lb = LeaderBoard()
    lb.download_rank()
