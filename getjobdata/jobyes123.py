import requests, pickle, math, re
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def get_yes123_data(keyword):
    
    keyword = keyword
    url = f'https://www.yes123.com.tw/wk_index/joblist.asp?find_key2={keyword}&order_ascend=desc&strrec=0&search_key_word={keyword}&search_type=job&search_from=joblist'
    comp_url = []
    comp_name = []
    
    headers = {'user-agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36'}
    web = requests.get(url, headers=headers, timeout=(10, 20))   #timeout=(連接超過10秒, 請求超過10秒)    
    web.encoding='utf-8' 
    soup = BeautifulSoup(web.text, "lxml")
    #print(soup)   
    target_links = soup.select('div.Job_opening_item_title h5 a')
    #print(target_links)
    for link in target_links:
        comp_url.append('https://www.yes123.com.tw/wk_index/' + link.get('href'))  #取得URL加入陣列

    target_comp_links = soup.select('div.d-flex div.Job_opening_item_title h6 a')
    for tag in target_comp_links:
        comp_name.append(tag)   #取得公司名稱
            
    dic1 = [{comp_name[i]:comp_url[i]} for i in range(len(comp_url))] 
    dic1 = dic1[:20]  
    info = []
    
    for index, i in enumerate(dic1):
        url = next(iter(i.values()))
        comp_name = next(iter(i.keys()))
        new_dict = {}
        new_list1 = []
        new_list2 = []
    
        headers = {'user-agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36'}
        web = requests.get(url, headers=headers, timeout=(30, 30))       
        web.encoding='utf-8' 
        soup = BeautifulSoup(web.text, "lxml")

        degree2 = soup.select('li span.left_title')
        for j in degree2:
            new_list2.append(re.sub('：' , '',j.text).strip())
            #print('工作內容=', re.sub('：' , '',j.text))
        
        degree1 = soup.select('li span.right_main')
        for j in degree1:
            new_list1.append(re.sub('  ' , '',j.text).strip())
            #print('內容=',re.sub('  ' , '',j.text))
                
        new_list2.append('網站連結')
        new_list1.append(url)
        
        new_list2.append('公司名稱')
        new_list1.append(comp_name)

        new_dict = {new_list2[i]:new_list1[i] for i in range(len(new_list1))} 
        info.append(new_dict) 
        # print(new_dict['工作地點'])
    return info
# get_yes123_data('python')