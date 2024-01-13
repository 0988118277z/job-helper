import mysql.connector
def reconnect_mysql():
    cnx = None
    try:
        cnx = mysql.connector.connect(
            host="host",
            user="user",
            password="password",
            database="database"
        )
        if cnx.is_connected():
            print("重新连接到数据库成功")
    except Error as e:
        print(f"重新连接数据库时发生错误：{e}")
    return cnx
    

channel_access_token = r'channel_access_token'

channel_secret =  r'channel_secret'

access_token = r'access_token' 
