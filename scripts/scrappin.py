# -*- coding: utf-8 -*-
"""
Created on Sun Dec 18 14:48:39 2016

@author: Milind Kabariya
"""

import urllib2
from lxml import html
import json

def getbasicInformation_mainURL(tree):
    titles = tree.xpath('//div[@class="row"]/div[@class="column col3"]/a/h3/text()')
    url = tree.xpath('//div[@class="row"]/div[@class="column col3"]/a[@href]')
    price = tree.xpath('//div[@class="row"]/div[@class="column col3"]/a/div[@class="prd_p_section"]/div[@class="ori_price"]/span[@class="p_price"]/text()')
    i=0
    scraplen = len(titles)
    monitorDict={}
    while i<scraplen:
        itemInformationList = []
        itemInformationList.append(titles[i])
        itemInformationList.append(url[2*i+1].values()[0])
        itemInformationList.append(price[i])
        monitorDict["monitor"+str(i)]= itemInformationList
        i+=1
#basic_info.json file conains 
    json.dump(monitorDict,open('../output/basic_info.json',"wb"))
    return url

#this function scrape the internal urls(items) and scape the titles and specifications
def getInternalUrlScraped(url):
    i=0
    ItemSpecificationDict={}
    while i<10:
        new_url = url[2*i+1].values()[0]
        req = urllib2.Request(new_url)
        response = urllib2.urlopen(req)
        the_page = response.read()
        tree = html.fromstring(the_page)
        specification_dictionary={}
    #print tree.xpath('////div[@class="selected_product_tabbing"]/div[@class="tabbing_info"]/div[@id="specification"]/h3[@class="active"]/text()')       
        specificationList = tree.xpath('////div[@class="selected_product_tabbing"]/div[@class="tabbing_info"]/div[@class="pd_tabs active"]/div[@class="specification_row"]/div[@class="row"]/span/text()')
        if  len(specificationList)>=2:       
            specification_dictionary=dict(specificationList[j:j+2] for j in range(0, len(specificationList)-1, 2))
        title = tree.xpath('////div[@class="container"]/div[@class="wrapper maxStWrap"]/div[@class="pdp_info wrapper "]/div[@class="prd_mid_info"]/h1/text()')
        if len(title)>0:    
            ItemSpecificationDict[title[0].strip()]=specification_dictionary
        else: 
            title = "No title for this monitor"
            ItemSpecificationDict[title]=specification_dictionary
        i+=1
    
    json.dump(ItemSpecificationDict,open('../output/item_specification.json',"wb"))


if __name__ == "__main__":
    url = 'http://www.shopclues.com/computers/desktops-and-monitors/monitors.html'
    req = urllib2.Request(url)
    response = urllib2.urlopen(req)
    the_page = response.read()
    tree = html.fromstring(the_page)
    url = getbasicInformation_mainURL(tree)
    getInternalUrlScraped(url)