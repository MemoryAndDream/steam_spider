# steam_spider
steam_spider is a simple spider to crawl steam's game or comments.

## install 
require enviroment python3 and dependency lxml

pip install lxml

## info 
This project is used to search steam game info,and now it has two main entry:
- steam_comments_search.py
- steam_tag_search.py  

steam_comments_search is get a single game's comments

steam_comments_search is used to get game info by one tag ,such as [Indie] games. You should change 
the url and max_page in the steam_tag_search.py  to search for your own entry.

## 项目说明
这个项目是用来爬取steam的tag标签下的游戏信息和游戏评论的。
程序入口
- steam_comments_search.py
- steam_tag_search.py  
运行环境python3，需要安装lxml依赖。
有什么问题可以去我的博客里留言 
https://blog.csdn.net/Memory_and_Dream/article/details/84773965
这个是平时接的付费定制的爬虫代码，有需要改动的可以付费修改或者指导哈。