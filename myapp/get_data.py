import requests
import re


class MusicRequest:
    url_num = {
        '飙升榜': '62',
        '热歌榜': '26',
        '新歌榜': '27',
        '流行指数榜': '4',
        '喜力电音榜': '57',
        '腾讯音乐人原创榜': '52',
        '听歌识区榜': '67',
        '内地榜': '5',
        '香港地区榜': '59',
        '台湾地区榜': '61',
        '欧美榜': '3',
        '韩国榜': '16',
        '日本榜': '17'
    }
    song_title_re = r'<a title="(.*?)".*?</li>'
    hot_re = r'<div class="songlist__rank">.*?/i>(.*?)</div>'
    author_re = r'<div class="songlist__artist".*?<a class="playlist__author".*?>(.*?)</a>'
    time_re = r'<div class="songlist__time">(.*?)</div>'

    def get_data(self, num):
        url = f'https://y.qq.com/n/ryqq/toplist/{num}'
        return requests.get(url).text

    def print_data(self, name):
        response = self.get_data(self.url_num[name])

        result = re.findall(self.song_title_re, response)
        hot = re.findall(self.hot_re, response)
        author = re.findall(self.author_re, response)
        time = re.findall(self.time_re, response)

        data1 = {name:
                     [{'songtitle': a, 'hot': b, 'author': c, 'time': d, 'rank': f}
                      for a, b, c, d, f in zip(result, hot, author, time, range(1, 21))]}
        return data1


music = MusicRequest()
