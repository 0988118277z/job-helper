import requests, re, pickle
from bs4 import BeautifulSoup

def get_1111_data(keyword):

    location = [
        100100,100200,100300,100400,100500,
        100600,100700,100800,100900,101000,
        101100,101200,101300,101400,101500,
        101600,101700,101800,101900,102000,
        102100,102200,102300,102400,102500
    ]
    location_r = random.choice(location)

    keyword = keyword
    url = f'https://www.1111.com.tw/search/job?ks={keyword}&c0={location_r}'

    comp_url = []
    comp_name = []

    headers = {'user-agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36'}
    web = requests.get(url, headers=headers, timeout=(5, 10))       
    web.encoding='utf-8' 
    soup = BeautifulSoup(web.text, "lxml")

    a_tag = soup.select('div.job_item_info a')
           
    for i in a_tag:
        href_url = i.get('href')
        target = i.get('target')
        title_tag = i.get('title')
        
        if href_url is not None and title_tag is None and '?' not in href_url:
            comp_url.append(r'https://www.1111.com.tw' + href_url)     #取得工作URL  
        if href_url is not None and title_tag is not None and '搜尋' not in title_tag :
            comp_name.append(title_tag)   #取得公司名稱
    
    dic1 = [{comp_name[i]:comp_url[i]} for i in range(len(comp_url[:20]))]  #限縮20筆資料  
   
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
      
        work_content = ''   
        work_content_list = soup.select('div.content_items.job_description div.body_2.description_info')
        for j in work_content_list:
            work_content += str(re.sub(r'[\n|\xa0]' , '',j.text))  #工作內容
    
        degree2 = soup.select('span.job_info_title')
        for j in degree2:
                if '鄰近捷運' in j.text:
                    continue
                new_list2.append(re.sub(r'[:]' , '',j.text))
            
        degree1 = soup.select('span.job_info_content')
        for j in degree1:
                new_list1.append(re.sub(r'\xa0', '、', re.sub(r'[\n\r|\u3000| ]' , '',j.text)))
            
        new_list2.append('工作內容')
        new_list1.append(work_content)
        
        new_list2.append('網站連結')
        new_list1.append(url)
        
        new_list2.append('公司名稱')
        new_list1.append(comp_name)        
            
        new_dict = {new_list2[i]:new_list1[i] for i in range(len(new_list1))} 
        info.append(new_dict)  
        #print(len(new_list2))
        #print(len(new_list1))
        # print(new_dict['工作地點：'])
        
    return info
# get_1111_data('python')
