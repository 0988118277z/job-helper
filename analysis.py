import pandas as pd
import re

def value_ana(df):
    value_counts = df['工作性質'].value_counts()
    #print(value_counts)
    # 计算百分比
    percentage = ((value_counts / len(df)) * 100).round(1)
    value_df = pd.DataFrame({'Count': value_counts, 'Percentage': percentage})
    return value_df[:3].to_string()
    # return value_df

def location_ana(df):
    df['上班地點'] = [ re.sub(r'[\n\r|\t| ]' , '', str(df['上班地點'][i]))[:3] if isinstance(df['上班地點'][i], str) else '' for i in range(len(df['上班地點'])) ]
    work_location = df['上班地點'].value_counts()
    percentage = ((work_location / len(df)) * 100).round(1)
    location_df = pd.DataFrame({'Count': work_location, 'Percentage': percentage})
    return location_df[:3].to_string()

def wfh_ana(df):
    df['遠端工作'] = [i.replace(' ','') if i is not None and i != '' else '無' for i in df['遠端工作']]
    df['遠端工作'].fillna('無', inplace=True)
    wfh_counts = df['遠端工作'].value_counts()
    # print(wfh_counts)
    percentage = ((wfh_counts / len(df)) * 100).round(1)
    wfh_df = pd.DataFrame({'Count': wfh_counts, 'Percentage': percentage})
    return wfh_df[:3].to_string()
    
def exp_ana(df):
    df['工作經驗'].fillna('不拘', inplace=True)
    exp_counts = df['工作經驗'].value_counts()
    # print(wfh_counts)
    percentage = ((exp_counts / len(df)) * 100).round(1)
    exp_df = pd.DataFrame({'Count': exp_counts, 'Percentage': percentage})
    return exp_df[:3].to_string()

def educational_ana(df):
    df['學歷要求'].fillna('不拘', inplace=True)
    educational_counts = df['學歷要求'].value_counts()
    percentage = ((educational_counts / len(df)) * 100).round(1)
    educational_df = pd.DataFrame({'Count': educational_counts, 'Percentage': percentage})
    return educational_df[:3].to_string()

def department_ana(df):
    df['科系要求'].fillna('不拘', inplace=True)
    department_counts = df['科系要求'].value_counts()
    percentage = ((department_counts / len(df)) * 100).round(1)
    department_df = pd.DataFrame({'Count': department_counts, 'Percentage': percentage})
    return department_df[:3].to_string()

def leanguage_ana(df):
    df['語文條件'] = [ re.sub('略通', '略懂', re.sub(r'[\n\r|\t|→|-|\xa0|\u3000 ]' , '', str(df['語文條件'][i]))) if isinstance(df['語文條件'][i], str) else '' for i in range(len(df['語文條件'])) ]
    language_data = [ df['語文條件'][i] for i in range(len(df['語文條件']))]
    # language_info = {
        # '不拘':0, 
        # '英文':{'聽':{'略懂':0, '普通':0, '中等':0, '精通':0, }, 
                # '說':{'略懂':0, '普通':0, '中等':0, '精通':0, }, 
                # '讀':{'略懂':0, '普通':0, '中等':0, '精通':0, }, 
                # '寫':{'略懂':0, '普通':0, '中等':0, '精通':0, }, }, 
        # '中文':{'聽':{'略懂':0, '普通':0, '中等':0, '精通':0, }, 
                # '說':{'略懂':0, '普通':0, '中等':0, '精通':0, }, 
                # '讀':{'略懂':0, '普通':0, '中等':0, '精通':0, }, 
                # '寫':{'略懂':0, '普通':0, '中等':0, '精通':0, }, },}
    for i in range(len(language_data)):
        if language_data[i] == '' or language_data[i] == '不拘' or '不拘' in language_data[i]:
            df['語文條件'][i] = '不拘'
        elif '英文' in language_data[i] and '中文' in language_data[i]:
            if '英文' == language_data[i][:2]:
                index_cn = language_data[i].index('中文')
                index_lsrw = language_data[i].index(j)
                df['語文條件'][i] = ''
                # for j in ['聽', '說', '讀', '寫']:
                for j in ['聽']:
                    for k in ['略懂', '普通', '中等', '精通']:
                        if re.sub(r'[^\w\s]', '', language_data[i][:index_cn][index_lsrw:index_lsrw+4])[1:3] == k:
                            # language_info['英文'][j][k] += 1
                            df['語文條件'][i] += '英文 ' + k
                            if '中文 ' not in df['語文條件'][i]:
                                df['語文條件'][i] += ' & ' 
                        if re.sub(r'[^\w\s]', '', language_data[i][index_cn:][index_lsrw:index_lsrw+4])[1:3] == k:
                            # language_info['中文'][j][k] += 1
                            df['語文條件'][i] += '中文 ' + k
                            if '英文 ' not in df['語文條件'][i]:
                                df['語文條件'][i] += ' & '          
            else:
                index_en = language_data[i].index('英文')
                index_lsrw = language_data[i].index(j)
                df['語文條件'][i] = ''
                # for j in ['聽', '說', '讀', '寫']:
                for j in ['聽']:
                    for k in ['略懂', '普通', '中等', '精通']:
                        if re.sub(r'[^\w\s]', '', language_data[i][:index_en][index_lsrw:index_lsrw+4])[1:3] == k:
                            # language_info['中文'][j][k] += 1
                            df['語文條件'][i] += '中文 ' + k
                            if '英文 ' not in df['語文條件'][i]:
                                df['語文條件'][i] += ' & '
                        if re.sub(r'[^\w\s]', '', language_data[i][index_en:][index_lsrw:index_lsrw+4])[1:3] == k:
                            # language_info['英文'][j][k] += 1
                            df['語文條件'][i] += '英文 ' + k
                            if '中文 ' not in df['語文條件'][i]:
                                df['語文條件'][i] += ' & '
        elif '英文' in language_data[i]:
            for j in ['聽', '說', '讀', '寫']:
                index_lsrw = language_data[i].index(j)
                for k in ['略懂', '普通', '中等', '精通']:
                    if re.sub(r'[^\w\s]', '', language_data[i][index_lsrw:index_lsrw+4])[1:3] == k:
                        # language_info['英文'][j][k] += 1
                        df['語文條件'][i] = '英文 ' + k                    
        elif '中文' in language_data[i]:
            for j in ['聽', '說', '讀', '寫']:
                index_lsrw = language_data[i].index(j)
                for k in ['略懂', '普通', '中等', '精通']:
                    if re.sub(r'[^\w\s]', '', language_data[i][index_lsrw:index_lsrw+4])[1:3] == k:
                        # language_info['中文'][j][k] += 1 
                        df['語文條件'][i] = '中文 ' + k
                    
    language_counts = df['語文條件'].value_counts()
    percentage = ((language_counts / len(df)) * 100).round(1)
    language_df = pd.DataFrame({'Count': language_counts, 'Percentage': percentage})
    return language_df[:3].to_string ()

def pay_ana(df):
    def process_pay(row):
        row = str(row)
        if '面議' in row or '經常性' in row:
            return 40000
        else:
            numbers = re.findall(r'[0-9]+', row)
            # print(numbers)
            if numbers:
                if len(numbers) < 2:
                    pays = int(''.join(numbers[0:2]))
                    # print(f'{pays} = {len(pays)}')
                    return pays
                    # elif len(pays) == 4:
                        # return ( int(pays[0] + pays[1]) + int(pays[2] + pays[3]) / 2 )
                else:
                    two_pays = int(len(numbers) / 2)
                    pays_1 = int(''.join(numbers[:two_pays]))
                    pays_2 = int(''.join(numbers[two_pays:]))
                    # print(f'{pays_1} ~ {pays_2}')
                    pays = (pays_1 + pays_2) / 2
                    if '年薪' in row:
                        return pays / 12
                    elif '月薪' in row:
                        return pays
                    elif '時薪' in row:
                        return pays * 22
                    else:
                        return 0
            return 0
    df['工作待遇'] = df['工作待遇'].apply(process_pay)
    pay_list = [ i for i in df['工作待遇'] if i > 200 ]
    max_pay = int(max(pay_list))
    min_pay = int(min(pay_list))
    avg_pay = int(sum(pay_list) / len(pay_list))
    df_pay = f'最高薪水    {max_pay}\n最低薪水    {min_pay}\n平均薪水    {avg_pay}'
    return df_pay

def main_ana(df): 
    # df_1 = pd.concat([value_ana(), wfh_ana()], ignore_index=True)
    # df_2 = pd.concat([leanguage_ana(), location_ana()], ignore_index=True)
    # df_3 = pd.concat([pay_ana(), department_ana()], ignore_index=True)
    # df_4 = pd.concat([exp_ana(), educational_ana()], ignore_index=True)
    # df_5 = pd.concat([df_1, df_2], ignore_index=True, axis=1)
    # df_6 = pd.concat([df_3, df_4], ignore_index=True)
    # df_end = pd.concat([df_5, df_6], ignore_index=True)
    # return df_end
    ana = value_ana(df) +'\n\n'+ wfh_ana(df) +'\n\n'+ leanguage_ana(df) +'\n\n'+ location_ana(df) +'\n\n'+ department_ana(df) +'\n\n'+ exp_ana(df) +'\n\n'+ educational_ana(df) +'\n\n'+ pay_ana(df)
    return ana
  
# print(main_ana())

def content_ana():
    import re
    from collections import Counter
    
    content = []
    separators = ['。', '.', ',', '，', '\r\n', '\n']
    temp = [ re.split('|'.join(map(re.escape, separators)), str(i)) for i in df['工作內容'] ]
    
    #print(value_counts)
    # 计算百分比
    # percentage = ((content_counts / len(df)) * 100).round(1)
    # value_df = pd.DataFrame({'Count': content_counts, 'Percentage': percentage})
    for i in temp:
        for j in i:
            if len(j) > 3:
                if j[-1].isdigit():
                    content.append(re.sub(' ' , '',j[:-1]))
                else:
                    content.append(re.sub(' ' , '',j))
                    
    counts = Counter(content)
    # for value, count in counts.items():
        # print(f"{value}: {count} 次")   
    return content
# content_ana()