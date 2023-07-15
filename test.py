# coding: utf-8
import json
import random
import re
import time

import requests


class KuaiShou:

    def __init__(self, rid):
        self.rid = rid

    def get_real_url(self):
        # headers = {
        #     'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36',
        #     'cookie': 'did=web_2b287dc0746444518284d6cebe074883',
        #     'Referer': 'https://live.kuaishou.com',
        # }
        user_agent_list = [
            "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36",
            "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36",
            "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36",
            "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.62 Safari/537.36",
            "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.101 Safari/537.36",
            "Mozilla/5.0 (Macintosh; U; PPC Mac OS X 10.5; en-US; rv:1.9.2.15) Gecko/20110303 Firefox/3.6.15",
        ]
        headers = {'User-Agent': random.choice(user_agent_list),
                   'cookie': 'did=web_2b287dc0746444518284d6cebe074883',
                   'Referer': 'https://live.kuaishou.com/u/'+self.rid,
                   }
        print(headers)
        with requests.Session() as s:
            url = 'https://live.kuaishou.com/u/{}'.format(self.rid)
            res = s.get(url, headers=headers)
            print(res.text)
            livestream = re.search(r'liveStream":(.*),"author', res.text)
            print(livestream)
            if livestream:
                livestream = json.loads(livestream.group(1))
                print(livestream)
                *_, hlsplayurls = livestream['playUrls']
                url = hlsplayurls['adaptationSet']['representation'][-1]['url']

                return url
            else:
                raise Exception('直播间不存在或未开播')


def get_real_url(rid):
    try:
        ks = KuaiShou(rid)
        return ks.get_real_url()
    except Exception as e:
        print('Exception：', e)
        return False


if __name__ == '__main__':
    # KPL704668133
    r = 'hrj20011221'  # input('请输入快手直播房间ID：\n')
    print(get_real_url(r))
    # while 1:
    #     print(get_real_url(r))
    #
    #     time.sleep(30)
