# -*- coding: UTF-8 -*-
import media
import fresh_tomatoes

dunkirk = media.Movie("Dunkirk", "https://www.youtube.com/watch?v=F-eMt3SrfFU",
                      "https://images-na.ssl-images-amazon.com/images/M/MV5BN2YyZjQ0NTEtNzU5MS00NGZkLTg0MTEtYzJmMWY3MWRhZjM2XkEyXkFqcGdeQXVyMDA4NzMyOA@@._V1_SY1000_CR0,0,674,1000_AL_.jpg")

the_shawshank_redemption = media.Movie("The Shawshank Redemption",
                                       "http://v.youku.com/v_show/id_XMzgzNjY2Njky.html?spm=a2h0k.8191407.0.0&from=s1.8-3-1.1",
                                       "https://images-na.ssl-images-amazon.com/images/M/MV5BMDFkYTc0MGEtZmNhMC00ZDIzLWFmNTEtODM1ZmRlYWMwMWFmXkEyXkFqcGdeQXVyMTMxODk2OTU@._V1_.jpg")

the_pursuit_of_happyness = media.Movie("The Pursuit of Happyness",
                                       "http://v.youku.com/v_show/id_XMTUxNzIxODQ=.html?spm=a2h0k.8191407.0.0&from=s1.8-3-1.1",
                                       "https://images-na.ssl-images-amazon.com/images/M/MV5BMTQ5NjQ0NDI3NF5BMl5BanBnXkFtZTcwNDI0MjEzMw@@._V1_SY1000_CR0,0,672,1000_AL_.jpg")

your_name = media.Movie("Your Name", "https://www.youtube.com/watch?v=k4xGqY5IDBE",
                        "https://images-na.ssl-images-amazon.com/images/M/MV5BODRmZDVmNzUtZDA4ZC00NjhkLWI2M2UtN2M0ZDIzNDcxYThjL2ltYWdlXkEyXkFqcGdeQXVyNTk0MzMzODA@._V1_SY1000_SX675_AL_.jpg")

gintama = media.Movie("Gintama",
                      "http://v.youku.com/v_show/id_XMjgyMjE4NTA4MA==.html?spm=a2h0k.8191407.0.0&from=s1.8-3-1.1",
                      "https://images-na.ssl-images-amazon.com/images/M/MV5BMzkxNGZjMDQtYTEzNi00OTdkLWJkMTYtZmIwYjQ2NWFiY2M1XkEyXkFqcGdeQXVyNDQxNjcxNQ@@._V1_SY1000_CR0,0,706,1000_AL_.jpg")

tonari_no_totoro = media.Movie("Tonari no Totoro", "https://www.youtube.com/watch?v=B6B_nuHksvs",
                               "https://images-na.ssl-images-amazon.com/images/M/MV5BNTdiOTQ0YmUtOGE3YS00NDg5LWI3YTEtNDAxZmE0MzRmZWM5L2ltYWdlXkEyXkFqcGdeQXVyNTAyODkwOQ@@._V1_SY1000_CR0,0,724,1000_AL_.jpg")

# 定义movies集合
movies = [dunkirk, the_shawshank_redemption, your_name, gintama, tonari_no_totoro, the_pursuit_of_happyness]

# 调用fresh_tomatoes.py里的open_movies_page方法，生成html页面并调用浏览器打开
fresh_tomatoes.open_movies_page(movies)
