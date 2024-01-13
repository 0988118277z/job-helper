import requests, time, re, pickle, os, random
from bs4 import BeautifulSoup

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def get_page(keyword, url):
    headers = {'user-agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36'}
    web = requests.get(url, headers=headers, timeout=(120, 120))   #timeout=(連接超過10秒, 請求超過10秒)    
    web.encoding='utf-8' 
    soup = BeautifulSoup(web.text, "lxml")

    totalpage_filter = r'"totalPage":(\d+)'  #設定過濾條件
    totalpage = int(re.findall(totalpage_filter, str(soup))[0])  #偵測這個類型有幾頁
    try:
        return random.randint(1,totalpage)
    except:
        return 1
    
def get_104_data(keyword):
    jobcat = [
        2001000000, 2002000000, 2003000000, 2004000000, 2005000000, 
        2006000000, 2007000000, 2008000000, 2009000000, 2010000000, 
        2011000000, 2012000000, 2013000000, 2014000000, 2015000000, 
        2016000000, 2017000000, 2018000000
    ]
    jobcat_r = random.choice(jobcat)
    area = [
        6001001000,6001002000,6001003000,6001004000,6001005000,
        6001006000,6001007000,6001008000,6001010000,6001011000,
        6001012000,6001013000,6001014000,6001016000,6001018000,
        6001019000,6001022000,6001021000,6001022000,6001023000
    ]
    area_r = random.choice(area)
    '''
        {'臺北市':6001001000}, {'新北市':6001002000}, {'宜蘭縣':6001003000}, {'基隆市':6001004000}, {'桃園市':6001005000},
        {'新竹縣市':6001006000}, {'苗栗縣':6001007000}, {'臺中市':6001008000}, {'彰化縣':6001010000}, {'南投縣':6001011000},
        {'雲林縣':6001012000}, {'嘉義縣市':6001013000}, {'臺南市':6001014000}, {'高雄市':6001016000}, {'屏東縣':6001018000},
        {'臺東縣':6001019000}, {'花蓮縣':6001022000}, {'澎湖縣':6001021000}, {'金門縣':6001022000}, {'連江縣':6001023000}
    '''
    # jobxp = [1, 3, 5, 10, 99]  #104的工作經驗[1年,1-3年 , 3-5年, 5-10年, 10年以上]
    jobxp = [1, 3, 5, 10]
    jobxp_r = random.choice(jobxp)
    s5 = [0, 256] #[輪班, 不用輪班]
    s5_r = random.choice(s5)
    edu = [1, 2, 3, 4, 5, 6]  #高中職以下  高中職  專科  大學  碩士  博士 
    edu_r = random.choice(edu)
    #公司類別
    indcat = [
        1003000000, 1005000000, 1006000000, 1007000000, 1009000000,
        1001000000, 1002000000, 1014000000, 1010000000, 1013000000,
        1004000000, 1008000000, 1011000000, 1012000000, 1015000000, 1016000000
    ]  
    indcat_r = random.choice(indcat)
    '''    
    批發零售:1003000000, 文教業:1005000000, 大眾傳播:1006000000, 旅遊休閒運動:1007000000, 服務業:1009000000
    墊子軟體半導體:1001000000, 製造業:1002000000, 農林漁牧水電:1014000000, 物流倉儲:1010000000, 政治社福:1013000000
    金融保險:1004000000, 法律會計顧問:1008000000, 營造不動產:1011000000, 醫療:1012000000, 礦石土木:1015000000, 住宿餐飲:1016000000
    '''

    keyword = keyword
    # url_before = f'https://www.104.com.tw/jobs/search/?ro=0&jobcat={jobcat_r}&keyword={keyword}&area={area_r}&indcat={indcat_r}&edu={edu_r}&s5={s5_r}&jobexp={jobxp_r}'
    url_before = f'https://www.104.com.tw/jobs/search/?ro=0&keyword={keyword}&area={area_r}&jobexp={jobxp_r}'
    # url = f'https://www.104.com.tw/jobs/search/?ro=0&keyword={keyword}'
    page = get_page(keyword, url_before)
    # url = f'https://www.104.com.tw/jobs/search/?ro=0&jobcat={jobcat_r}&keyword={keyword}&area={area_r}&indcat={indcat_r}&edu={edu_r}&s5={s5_r}&page={page}&jobexp={jobxp_r}'
    url = f'https://www.104.com.tw/jobs/search/?ro=0&keyword={keyword}&area={area_r}&page={page}&jobexp={jobxp_r}'
    print(url)
    
    comp_url = []
    comp_name = []
    
    headers = {'user-agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36'}
    web = requests.get(url, headers=headers, timeout=(60, 60))   #timeout=(連接超過10秒, 請求超過10秒)    
    web.encoding='utf-8' 
    soup = BeautifulSoup(web.text, "lxml")

    target_links = soup.select('div.b-block__left h2.b-tit a[href]')
    for link in target_links:
        comp_url.append(link.get('href'))  #取得URL加入陣列

    ul_tag = soup.select('div.b-block__left ul.b-list-inline a')
    for tag in ul_tag:
        comp_name.append(tag.text)  #取得公司名加入陣列
        
    try:
        dic1 = [{comp_name[i]:comp_url[i]} for i in range(len(comp_url))] 
    except:
        print('comp_url=',comp_url)
        print('comp_name=',comp_name)
 

    #dic1 = [{'XX公司':'https://www.104.com.tw/job/7aqew?jobsource=jolist_a_date'},{'YY公司':'https://www.104.com.tw/job/7qclf?jobsource=jolist_a_date'}]
    dic1 = dic1[-20:]  #前兩筆是垃圾廣告
    info = []
    
    for index, i in enumerate(dic1):
        url = 'https:' + next(iter(i.values()))
        comp_name = next(iter(i.keys()))
        new_dict = {}
        new_list1 = []
        new_list2 = []
        work_content = ''

        firefox_driver_path  = 'G:\我的雲端硬碟\OO學院專案\工作分析器\py\geckodriver.exe'
        options = webdriver.FirefoxOptions()
        options.headless = True  #不開啟瀏覽器
        options.add_argument('--disable-gpu')  #不開啟GPU加速
        service = webdriver.firefox.service.Service(firefox_driver_path)
        driver = webdriver.Firefox(service=service , options=options)
        driver.get(url)  
        wait = WebDriverWait(driver, 10)  #設定等待時間
        wait.until(EC.presence_of_element_located((By.TAG_NAME, 'body')))  #等到'body'加載完成在動作  
        page_content = driver.page_source  #儲存爬下來的內容
        soup = BeautifulSoup(page_content, 'lxml')  #用BS4 lxml 解析
        #with open('bs4.txt','a+',encoding='utf-8') as txt:
            #txt.write(str(soup))
        driver.quit()  #關閉動態爬蟲

        job_description = soup.select('p.mb-5')
        for i in job_description:
            work_content += i.text
        degree1 = soup.select('div.list-row__data')  #<div class="t3 mb-0" data-v-1392b104="">
        degree2 = soup.select('div.list-row__head')  #<h3 class="h3" data-v-1392b104="">           
        for i in degree1:
            new_list1.append(re.sub(' ' , '',i.text))  #獲取其他要求的內容，存到陣列
        
        for i in degree2:
            new_list2.append(i.text)  #獲取其他要求的標題，存到陣列

        new_list2.append('工作內容')
        new_list1.append(work_content)
        
        new_list2.append('網站連結')
        new_list1.append(url)
        
        new_list2.append('公司名稱')
        new_list1.append(comp_name)
        
        new_list2.append('工作待遇')
        new_list1.append(soup.select_one('div.text-primary span.align-baseline').text)
 
        new_dict = {new_list2[i]:new_list1[i] for i in range(len(new_list1))} 
        info.append(new_dict)
    #print('work_content=',job_description)  #檢查 工作內容 是否有取得
    #print(len(new_dict) > 0)  #檢查 工作條件 是否有取得
        
        # print(len(info),'/',len(dic1), end='\r')
        # print(new_dict.keys())
    return info

get_104_data('python')

