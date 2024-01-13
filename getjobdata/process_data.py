import pickle, csv, os, mysql.connector, time
import pandas as pd
from job104 import get_104_data
from job518 import get_518_data
from job1111 import get_1111_data
from jobyes123 import get_yes123_data

def reconnect_mysql():
    cnx = None
    try:
        cnx = mysql.connector.connect(
            host="35.185.255.1",
            user="yiline",
            password="Aa123456",
            database="linebot"
        )
        if cnx.is_connected():
            print("重新连接到数据库成功")
    except Error as e:
        print(f"重新连接数据库时发生错误：{e}")
    return cnx

def renew_job_data(keyword):
    #'''
    dic1 = get_104_data(keyword)
    for d in dic1:
        # 创建一个新的空字典来存储修改后的键值对
        new_dict = {}
    
        # 遍历字典中的键值对
        for key, value in d.items():
            # 将键中的 "@" 符号替换为空字符串，并添加到新字典中
            new_key = key.replace(" ", "")
            new_dict[new_key] = value  
        # 更新原始字典
        d.clear()
        d.update(new_dict)
    
    for d in dic1:
        new_dict = {}
        for key, value in d.items():
            new_key1 = key.replace("工作經歷", "工作經驗")
            new_dict[new_key1] = value
        d.clear()
        d.update(new_dict)
    
    df_104 = pd.DataFrame.from_records(dic1)
    #print(df_104)
    #df_104.to_csv(path_104_csv, index=False, encoding='utf_8_sig')
    #'''


    #'''
    dic1 = get_1111_data(keyword)

    for d in dic1:
        new_dict = {}
        for key, value in d.items():
            # 将键中的 "@" 符号替换为空字符串，并添加到新字典中
            new_key1 = key.replace("：", "")
            new_dict[new_key1] = value
        d.clear()
        d.update(new_dict)
    
    for d in dic1:
        new_dict = {}
        for key, value in d.items():
            new_key1 = key.replace("學歷限制", "學歷要求")
            new_dict[new_key1] = value
        d.clear()
        d.update(new_dict)
    
    for d in dic1:
        new_dict = {}
        for key, value in d.items():
            new_key1 = key.replace("工作時間", "上班時段")
            new_dict[new_key1] = value
        d.clear()
        d.update(new_dict)
    
    for d in dic1:
        new_dict = {}
        for key, value in d.items():
            new_key1 = key.replace("科系限制", "科系要求")
            new_dict[new_key1] = value
        d.clear()
        d.update(new_dict)

    for d in dic1:
        new_dict = {}
        for key, value in d.items():
            new_key1 = key.replace("工作地點", "上班地點")
            new_dict[new_key1] = value
        d.clear()
        d.update(new_dict)    
    
    for d in dic1:
        new_dict = {}
        for key, value in d.items():
            new_key1 = key.replace("打字速度", "其他條件")
            new_dict[new_key1] = value
        d.clear()
        d.update(new_dict)
    
    for d in dic1:
        new_dict = {}
        for key, value in d.items():
            new_key1 = key.replace("語言能力", "語文條件")
            new_dict[new_key1] = value
        d.clear()
        d.update(new_dict)
    
    for d in dic1:
        new_dict = {}
        for key, value in d.items():
            new_key1 = key.replace("遠距工作", "遠端工作")
            new_dict[new_key1] = value
        d.clear()
        d.update(new_dict)
    
    for d in dic1:
        new_dict = {}
        for key, value in d.items():
            new_key1 = key.replace("電腦專長", "其他條件")
            new_dict[new_key1] = value
        d.clear()
        d.update(new_dict)
    
    df_1111 = pd.DataFrame.from_records(dic1)
    #print(df_1111)
    #df_1111.to_csv(path_1111_csv, index=False, encoding='utf_8_sig')
    ##'''


    ##'''
    dic1 = get_yes123_data(keyword)

    for d in dic1:
        new_dict = {}
        for key, value in d.items():
            new_key1 = key.replace("外派說明", "出差外派")
            new_dict[new_key1] = value
        d.clear()
        d.update(new_dict)
    
    for d in dic1:
        new_dict = {}
        for key, value in d.items():
            new_key1 = key.replace("工作地點", "上班地點")
            new_dict[new_key1] = value
        d.clear()
        d.update(new_dict) 
    
    for d in dic1:
        new_dict = {}
        for key, value in d.items():
            new_key1 = key.replace("外語能力", "語文條件")
            new_dict[new_key1] = value
        d.clear()
        d.update(new_dict)
    
    for d in dic1:
        new_dict = {}
        for key, value in d.items():
            new_key1 = key.replace("取得認證", "具備證照")
            new_dict[new_key1] = value
        d.clear()
        d.update(new_dict)
    
    for d in dic1:
        new_dict = {}
        for key, value in d.items():
            new_key1 = key.replace("電腦技能", "其他條件")
            new_dict[new_key1] = value
        d.clear()
        d.update(new_dict)
        
    for d in dic1:
        new_dict = {}
        for key, value in d.items():
            new_key1 = key.replace("薪資待遇", "工作待遇")
            new_dict[new_key1] = value
        d.clear()
        d.update(new_dict)

    df_yes123 = pd.DataFrame.from_records(dic1)
    try:
        df_yes123['薪資待遇'] = df_yes123['保險福利'] + '、' + df_yes123['獎金制度'] + '、' + df_yes123['輔助津貼'] + '、' + df_yes123['休閒娛樂'] + '、' + df_yes123['福利設施'] + '、' + df_yes123['其他福利'] + '、' + df_yes123['更多福利']
        df_yes123.drop(['保險福利', '獎金制度', '輔助津貼', '休閒娛樂', '福利設施', '其他福利', '更多福利'], axis=1, inplace=True)
    except:
        pass
    #df_yes123['薪資福利'] + '、' + 
    #print(df_yes123)
    #df_yes123.to_csv(path_yes123_csv, index=False, encoding='utf_8_sig')
    ##'''


    ##'''
    dic1 = get_518_data(keyword)

    
    for d in dic1:
        new_dict = {}
        for key, value in d.items():
            new_key1 = key.replace("薪資待遇", "工作待遇")
            new_dict[new_key1] = value
        d.clear()
        d.update(new_dict)
        
    for d in dic1:
        new_dict = {}
        for key, value in d.items():
            new_key1 = key.replace("是否出差", "出差外派")
            new_dict[new_key1] = value
        d.clear()
        d.update(new_dict)    
    
    for d in dic1:
        new_dict = {}
        for key, value in d.items():
            new_key1 = key.replace("科系限制", "科系要求")
            new_dict[new_key1] = value
        d.clear()
        d.update(new_dict)    
    df_518 = pd.DataFrame.from_records(dic1)
    #print(dic1)
    #df_518.to_csv(path_518_csvcls, index=False, encoding='utf_8_sig')
    ##'''

    # pandas合併資料
    try:
        df_1 = pd.merge(df_104, df_518, how='outer')
    except:
        df_1 = pd.merge(df_104, df_518, how='outer', left_index=True, right_index=True)
   
    try:
        df_2 = pd.merge(df_yes123, df_1111, how='outer')
    except:
        df_2 = pd.merge(df_yes123, df_1111, how='outer', left_index=True, right_index=True)
   
    try:    
        df_3 = pd.merge(df_1, df_2, how='outer')
    except:
        df_3 = pd.merge(df_1, df_2, how='outer', left_index=True, right_index=True)

    selected_columns = [
    '工作內容', '網站連結', '公司名稱', '職務類別', '工作待遇',
    '其他條件', '語文條件', '遠端工作', '上班地點', '工作性質',
    '學歷要求', '科系要求', '出差外派', '工作經驗'
    ]
    available_columns = [col for col in selected_columns if col in df_3.columns]
    data = df_3[available_columns]
    return data
    
def updata_data(keyword, data):
    cnx = reconnect_mysql()
    cursor = cnx.cursor()

    create_table_query = f"""
        CREATE TABLE {keyword} (
            工作內容 TEXT DEFAULT NULL,
            網站連結 TEXT DEFAULT NULL,
            公司名稱 TEXT DEFAULT NULL,
            職務類別 TEXT DEFAULT NULL,
            工作待遇 TEXT DEFAULT NULL,
            其他條件 TEXT DEFAULT NULL,
            語文條件 TEXT DEFAULT NULL,
            遠端工作 TEXT DEFAULT NULL,
            上班地點 TEXT DEFAULT NULL,
            工作性質 TEXT DEFAULT NULL,
            學歷要求 TEXT DEFAULT NULL,
            科系要求 TEXT DEFAULT NULL,
            出差外派 TEXT DEFAULT NULL,
            工作經驗 TEXT DEFAULT NULL
        );
        """
    cursor.execute(create_table_query)
    cnx.commit()

    # insert_query = f'INSERT INTO {keyword} ({columns_str}) VALUES ({", ".join(["%s"] * len(data_columns))})'

    # for i, row in data.iterrows():
        # try:
            # cursor.execute(insert_query, tuple(row))
            # cnx.commit()
        # except mysql.connector.Error as err:
            # print("錯誤: ", err)
    
    # ------------Pandas轉SQL------------------
    data = data.where(pd.notnull(data), None)
    data_columns = list(data.columns)
    columns_str = ', '.join(data_columns)
    for i, row in data.iterrows():
        placeholders = ', '.join(['%s'] * len(row))
        insert_query = f'INSERT INTO {keyword} ({columns_str}) VALUES ({placeholders})'
        processed_row = [str(item) if not isinstance(item, (str, int, float, type(None))) else item for item in row]
        with cnx.cursor() as cursor:
            cursor.execute(insert_query, tuple(processed_row))
            cnx.commit()        
    # ---------------------------------------------
    cursor = cnx.cursor()  #不知道為啥斷了
    update_query = 'UPDATE keyword_status set status = 1 where keyword = %s'
    cursor.execute(update_query, [keyword])
    cnx.commit()
    
    cursor.close()
    cnx.close()
    
def main(): 
    cnx = reconnect_mysql()
    cursor = cnx.cursor()  # 創建db連線
    query = 'select keyword from keyword_status where status = 0'
    cursor.execute(query)  # 執行SQL
    result = cursor.fetchall()  # 顯示sql回傳結果
    cnx.close()
    cursor.close()
    if len(result) > 0:
        for i in range(len(result)):
            updata_data(result[i][0],renew_job_data(result[i][0]))
    else:
        pass

while True:
    main()
    time.sleep(60)

