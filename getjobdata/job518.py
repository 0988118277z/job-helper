import requests, pickle, re
from bs4 import BeautifulSoup

def get_518_data(keyword):
    keyword = keyword
    url = f'https://www.518.com.tw/job-index-P-1.html?ad={keyword}'
    comp_url = []
    comp_name = []
    
    headers = {'user-agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36'}
    web = requests.get(url, headers=headers, timeout=(10, 20))   #timeout=(連接超過10秒, 請求超過10秒)    
    web.encoding='utf-8' 
    soup = BeautifulSoup(web.text, "lxml")
    
    target_links = soup.select('div.job__card div.job__title__wrapper h2.job__title__inner a')
    for link in target_links:
        comp_url.append(link.get('href'))  #加入陣列

    target_comp_links = soup.select('div.job__card div.job__title__wrapper a')
    for tag in target_comp_links:
        comp_name.append(tag.text)
        
    url_list = [{comp_name[i]:comp_url[i]} for i in range(len(comp_url))] 

    info = []  
    for i in url_list:
        url = next(iter(i.values()))
        comp_name = next(iter(i.keys()))
        new_dict = {}
        new_list1 = []
        new_list2 = []
        new_list3 = []
    
        headers = {'user-agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36'}
        web = requests.get(url, headers=headers, timeout=(30, 30))       
        web.encoding='utf-8' 
        soup = BeautifulSoup(web.text, "lxml")

        degree1 = soup.select('div.jobItem div.wrapper div') 
        
        for index, i in enumerate(degree1):
            # print(f'{index}={i.text}')
            new_list3.append(re.sub(r'[\n|\u3000]' , '',i.text).replace(' ',''))  #獲取其他要求的內容，存到陣列
        # del new_list3[4]
        new_list2 = [ new_list3[i] for i in range(0,len(new_list3),2) ]
        new_list1 = [ new_list3[i] for i in range(1,len(new_list3),2) ]
        # for i in range(len(new_list2)):
            # print(f'{new_list2[i]}={new_list1[i]}')


        new_list2.append('網站連結')
        new_list1.append(url)
        
        new_list2.append('公司名稱')
        new_list1.append(comp_name) 

        new_list2.append('工作內容')
        work_content = soup.select('div.jobnewDetail div.job-detail-box div.JobDescription p')
        for j in work_content:
            new_list1.append(re.sub('  |[\r\n]' , '',j.text))
            #print('內容=',re.sub('  ' , '',j.text))
            
        new_dict = {new_list2[i]:new_list1[i] for i in range(len(new_list1))} 
        info.append(new_dict) 
        print(new_dict['上班地點'])
    return info

get_518_data('python')