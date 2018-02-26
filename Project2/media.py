# coding=utf-8
import webbrowser

# Movie类
# movie_title 电影名
# movie_storyline 电影简介
# poster_image 电影海报
# trailer_youku_id 电影url
class Movie():
    # 构造函数，对属性进行初始化赋值
    def __init__(self, movie_title, movie_storyline, poster_image, trailer_youku_id):
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youku_id = trailer_youku_id

    # 通过调用webbrowser打开浏览器播放视频
    def show_trailer(self):
        webbrowser.open(self.trailer_url)
