import mysql.connector
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
    

channel_access_token = r'snCGTjFnKDwbUEWhpUSAXfZ1S3BZhb0lNDlv372AoKLQSbHaxI2Z3OIZnhuvbg0Ta8SAJBDsjXlImBDTta3fh5vAiwJjhcYhca0AEWK1ZQJHYpd1G/0h5vA6Eq00y5UWhvVjzHVK3gwkD7q1WgNCeQdB04t89/1O/w1cDnyilFU='

channel_secret =  r'16cd7a066350f98b11dc1b784b6844bf'

access_token = r'sjia8Xi4KOtfLB69PM06CjMG5lE7UaO5vOgqPmXhwXn' 
