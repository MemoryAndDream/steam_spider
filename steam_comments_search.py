# -*- coding: utf-8 -*-
"""
File Name：     steam_comments
Description :
Author :       meng_zhihao
mail :       312141830@qq.com
date：          2020/7/4
"""
from crawl_tool_for_py3 import crawlerTool as ct

import csv

FOUT= open('steam_comments.csv', 'w', encoding='utf_8_sig', newline='', )
csv_writer = csv.writer(FOUT)
csv_writer.writerow(['AuthorName','title','hours','date','comment_content','helpfuls','funnys'])

def extractor(page_buf):
    comments = []

    segs = ct.getXpath('//div[contains(@class,"apphub_Card ")]',page_buf)
    for seg in segs:
        helpfuls = ct.getRegex('(\d+) people found this review helpful',seg)
        funnys = ct.getRegex('(\d+) people found this review funny',seg)
        title = ct.getXpath1('//div[@class="title"]/text()',seg)
        hours =  ct.getXpath1('//div[@class="hours"]/text()',seg)
        comment_content_and_date = ct.getXpath('//div[@class="apphub_CardTextContent"]/text()',seg)
        date = ct.getXpath1('//div[@class="date_posted"]/text()',seg)
        comment_content= ' '.join(comment_content_and_date[1:])
        apphub_CardContentAuthorName = ct.getXpath1('//div[contains(@class,"apphub_CardContentAuthorName")]/a/text()',seg)

        comments.append([apphub_CardContentAuthorName,title,hours,date,comment_content,helpfuls,funnys])
    for comment in comments:
        csv_writer.writerow(comment)
        FOUT.flush()
    return comments


def main(app_id):
    app_id = str(app_id)
    ct_obj = ct()
    entry_url = 'https://store.steampowered.com/app/%s'%app_id
    rs = ct_obj.sget(entry_url,cookies={"Steam_Language":"english","birthtime":"725817601","lastagecheckage":"1-January-1993"}) # 语言和18周岁限制
    review_url = 'https://steamcommunity.com/app/%s/reviews/?browsefilter=toprated&snr=1_5_100010_&filterLanguage=english'% app_id
    # review_url = 'https://steamcommunity.com/app/394360/homecontent/?userreviewscursor=AoIIPvnRs3yBhKkB&userreviewsoffset=11428&p=1144&workshopitemspage=1144&readytouseitemspage=1144&mtxitemspage=1144&itemspage=1144&screenshotspage=1144&videospage=1144&artpage=1144&allguidepage=1144&webguidepage=1144&integratedguidepage=1144&discussionspage=1144&numperpage=10&browsefilter=toprated&browsefilter=toprated&appid=394360&appHubSubSection=10&appHubSubSection=10&l=english&filterLanguage=english&searchText=&forceanon=1'
    while True: # 最后会页面空白
        results = []
        for retry_times in range(3): # 异常重试
            page_buf = ct_obj.sget(review_url)
            results = extractor(page_buf)
            if results:break
        if not results:
            break
        userreviewscursor = ct.getXpath1('//input[@name="userreviewscursor"]/@value',page_buf)
        userreviewsoffset = ct.getXpath1('//input[@name="userreviewsoffset"]/@value',page_buf)
        workshopitemspage = ct.getXpath1('//input[@name="workshopitemspage"]/@value',page_buf)
        readytouseitemspage  = ct.getXpath1('//input[@name="readytouseitemspage"]/@value',page_buf)
        p = ct.getXpath1('//input[@name="p"]/@value',page_buf)
        mtxitemspage = ct.getXpath1('//input[@name="mtxitemspage"]/@value',page_buf)
        itemspage =  ct.getXpath1('//input[@name="itemspage"]/@value',page_buf)
        screenshotspage =  ct.getXpath1('//input[@name="screenshotspage"]/@value',page_buf)
        videospage = ct.getXpath1('//input[@name="videospage"]/@value',page_buf)
        artpage = ct.getXpath1('//input[@name="artpage"]/@value',page_buf)
        allguidepage = ct.getXpath1('//input[@name="allguidepage"]/@value',page_buf)
        webguidepage = ct.getXpath1('//input[@name="webguidepage"]/@value',page_buf)
        integratedguidepage = ct.getXpath1('//input[@name="integratedguidepage"]/@value',page_buf)
        discussionspage = ct.getXpath1('//input[@name="discussionspage"]/@value',page_buf)
        numperpage = ct.getXpath1('//input[@name="numperpage"]/@value',page_buf)
        browsefilter = ct.getXpath1('//input[@name="browsefilter"]/@value',page_buf)
        l = ct.getXpath1('//input[@name="l"]/@value',page_buf)
        appHubSubSection = ct.getXpath1('//input[@name="appHubSubSection"]/@value',page_buf)
        browsefilter = ct.getXpath1('//input[@name="browsefilter"]/@value',page_buf)
        filterLanguage = ct.getXpath1('//input[@name="filterLanguage"]/@value',page_buf)
        searchText =  ct.getXpath1('//input[@name="searchText"]/@value',page_buf)
        forceanon = ct.getXpath1('//input[@name="forceanon"]/@value',page_buf)

        review_url =  'https://steamcommunity.com/app/'+app_id+'/homecontent/?userreviewscursor='+ct.quote(userreviewscursor)+'&userreviewsoffset='+userreviewsoffset\
                      +'&p='+p+'&workshopitemspage='+workshopitemspage+'&readytouseitemspage='+readytouseitemspage+\
                      '&mtxitemspage='+mtxitemspage+'&itemspage='+itemspage+'&screenshotspage='+screenshotspage+'&videospage='+videospage+'&artpage='+artpage+'&allguidepage='+allguidepage+\
                          '&webguidepage='+webguidepage+'&integratedguidepage='+integratedguidepage+'&discussionspage='+discussionspage+'&numperpage='+numperpage+'&browsefilter='+browsefilter+'&browsefilter='+browsefilter+\
                          '&appid='+app_id+'&appHubSubSection='+appHubSubSection+'&appHubSubSection='+appHubSubSection+'&l='+l+'&filterLanguage='+filterLanguage+'&searchText='+searchText+'&forceanon='+forceanon
        print(review_url)


if __name__ == '__main__':
    app_id = 394360
    main(app_id)