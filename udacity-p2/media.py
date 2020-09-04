# -*- coding: UTF-8 -*-
# movie object

# author lvguixing
# date 2018-01-06

import webbrowser

class Movie():

    # Movie 的构造方法，传入 movie_title 电影名， trailer_url  预告片地址， poster_image_url 海报地址

    def __init__(self, movie_title, trailer_url, poster_image_url):
        self.title = movie_title
        self.trailer_url = trailer_url
        self.poster_image_url = poster_image_url