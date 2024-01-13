import re, mysql.connector, json
from config import channel_access_token, channel_secret, reconnect_mysql
from analysis import main_ana
from analysis_webapi import main_ana_webapi
import pandas as pd

def mysql_select(content,keyword=None):
    cnx = reconnect_mysql()
    cursor = cnx.cursor()  # 創建db連線
    cursor.execute(content,keyword)  # 執行SQL
    result = cursor.fetchall()  # 顯示sql回傳結果
    cnx.close()
    cursor.close()
    return (result)

def mysql_insert(content,keyword=None):
    cnx = reconnect_mysql()
    cursor = cnx.cursor()  # 創建db連線
    cursor.execute(content,keyword)  # 執行SQL
    cnx.commit()
    cnx.close()
    cursor.close()
    return 'ok'

def job(emt,api=None):
    sult = emt.replace('#','').replace(' ','')    # 過濾'#'

    try:
        query = f'select status from keyword_status where keyword= %s'
        results = mysql_select(query,[sult])[0][0]
    except:
        query = "insert into keyword_status (keyword,status) value (%s, %s);"
        mysql_insert(query, [sult.lower(), 0])
        
        if api == None:
            return f'資料庫中未有此關鍵字資料，已將{sult}加入查詢清單'
        else: 
            return {'status':f'資料庫中未有此關鍵字資料，已將{sult}加入查詢清單'}

    if results == 0 or results == 2 :
        
        if api == None:
            return '資料查詢中'
        else: 
            return {'status':'資料查詢中'}
    elif results == 1:
        query = f"SELECT * FROM {sult}"
        cnx = reconnect_mysql()
        df = pd.read_sql(query,cnx)
        cnx.close()
        if api == None:
            return main_ana(df)
        else: 
            return main_ana_webapi(df)


def update_job(emt,api=None):
    sult = emt.replace('^','').replace(' ','')
    try:
        query = f'UPDATE keyword_status set status = 2 where keyword = %s'
        mysql_insert(query,[sult])[0][0]
        
        if api == None:
            return f'已將{sult}加入更新清單'
        else: 
            return {'status':f'已將{sult}加入更新清單'}
        
    except:
        if api == None:
            return f'資料庫中未有此關鍵字資料'
        else: 
            return {'status':f'資料庫中未有此關鍵字資料'}
