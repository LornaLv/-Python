# Date: 2023/2/20 上午11:00
# 豆瓣top250排行，使用列表存储电影信息，要求输入名字，在屏幕上显示xxx出演了哪部电影
lst = [{'rating': [9.7, 50], 'id': '1292052', 'type': ['犯罪', '剧情'], 'title': '肖申克的救赎',
        'actors': ['蒂姆.罗宾汉', '摩根.弗里曼']},
       {'rating': [9.6, 50], 'id': '1291546', 'type': ['爱情', '剧情', '同性'], 'title': '霸王别姬',
        'actors': ['张国荣', '张丰毅', '巩俐', '葛优']},
       {'rating': [9.6, 50], 'id': '1296141', 'type': ['犯罪', '剧情', '悬疑'], 'title': '控方证人',
        'actors': ['泰隆.鲍华', '玛琳.黛德丽']}]

name = input('请输入你要查询的演员：')
for item in lst:  # 遍历列表   ---->{ }
    act_lst = item['actors']
    # for actor in act_lst:
    if name in act_lst:
        print(name + '出演了' + item['title'])
# for movie in item:  #遍历字典，得到movie 是字典中的key
#     print(movie)
# actors=movie['actors']
#
# if name in actors:
#     print(name+'演出了'+movie)
