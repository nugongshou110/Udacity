# coding=utf-8
import media
import fresh_tomatoes

# 创建电影碟中谍6对象
movie1 = media.Movie('碟中谍6',
                     "《碟中谍6：全面瓦解》（Mission: Impossible - Fallout）是由派拉蒙影业公"
                     "司出品的动作电影，是《碟中谍》系列电影的第六部。由汤姆·克鲁斯、丽贝卡·弗格"
                     "森、亨利·卡维尔主演。",
                     'https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000'
                     '&sec=1518104390692&di=7753e1d458108d19c2c4a8aa48e870eb&imgtype'
                     '=0&src=http%3A%2F%2Fwww.hhyl.cc%2Fuploads%2Fhuoche35%2F14897412'
                     '83415716.jpg',
                     'XMzM4NjU5NDIzNg')
# 创建电影红海行动对象
movie2 = media.Movie('红海行动',
                     "该片讲述了中国海军“蛟龙突击队”8人小组奉命执行撤侨任务，突击队兵分两路进行救"
                     "援，但不幸遭到伏击，人员伤亡。同时，掌握核战原材料的恐怖分子首领还在密谋不"
                     "法行动，突击队必须尽快行动的故事。",
                     'https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000'
                     '&sec=1518104547076&di=622fb1848c686f243fa7e89da7859293&imgtype'
                     '=0&src=http%3A%2F%2Fimages.rednet.cn%2Farticleimage%2F2018%2F0'
                     '1%2F30%2F92949392.jpeg',
                     'XMzM4NTgwNjg0MA')
# 创建电影捉妖记2对象
movie3 = media.Movie('捉妖记2',
                     "该片讲述了天荫和小岚找回胡巴团聚一堂的合家欢故事",
                     'https://ss1.bdstatic.com/70cFuXSh_Q1YnxGkpoWK1HF6hhy/it/u=2383'
                     '667866,3207392615&fm=11&gp=0.jpg',
                     'XMzM4NjE0MDY0NA')
# 创建电影西游记女儿国对象
movie4 = media.Movie('西游记女儿国',
                     "该片讲述了唐僧师徒四人在取经路上与各路妖魔鬼怪斗智斗勇的故事",
                     'https://timgsa.baidu.com/timg?image&quality=80&size=b9999_1000'
                     '0&sec=1518104688842&di=0c2f1c021bf8dc705770142e5aa46f50&imgtyp'
                     'e=0&src=http%3A%2F%2Fimg1.gtimg.com%2Fjiangsu%2Fpics%2Fhv1%2F'
                     '214%2F153%2F2261%2F147060754.jpg',
                     'XMzM4NTc4NDc2OA')
# 创建2018春节电影盛宴对象
movie5 = media.Movie('2018春节电影盛宴',
                     "合家欢好戏连台等你来",
                     'https://timgsa.baidu.com/timg?image&quality=80&size=b9999_1000'
                     '0&sec=1518699499&di=b326e1b42ccffec4d87adf2264edf277&imgtype=jpg'
                     '&er=1&src=http%3A%2F%2Fi.ce.cn%2Fce%2Fculture%2Fzt%2F2018%2Fcj%'
                     '2Fhsddy%2F201801%2F26%2FW020180206366324285862.jpg',
                     'XMzM4NzMzMDk5Ng')
# 创建古墓丽影对象
movie6 = media.Movie('古墓丽影：源起之战',
                     "该片将讲述劳拉·克劳馥在21岁时在经历一次狂风暴雨的海难之后，劳拉漂流到一个"
                     "未知的小岛上所发生的故事。",
                     'https://timgsa.baidu.com/timg?image&quality=80&size=b9999_1000'
                     '0&sec=1518104894096&di=32f370d7bed084ede7bbf7d78639325f&imgtyp'
                     'e=0&src=http%3A%2F%2Fwww.cnr.cn%2Fent%2Fjd%2F20180205%2FW02018'
                     '0205393992126187.jpg',
                     'XMzM4NjYwODEwMA')
# 将创建好的6个电影添加到列表中
movies = [movie1, movie2, movie3, movie4, movie6, movie5]
# 使用浏览器打开网页
fresh_tomatoes.open_movies_page(movies)
