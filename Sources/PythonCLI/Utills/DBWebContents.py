import pymysql

# def createUserTable():
#     conn = pymysql.connect(host='172.33.0.2', user='root', password='abcd', db='cloud', charset='utf8')
#     cursor = conn.cursor()
#     sql ='''
#         CREATE TABLE user ( 
#             auth int(2)
#             account varchar(32) NOT NULL PRIMARY KEY,
#             passwd  varchar(32),
#             name varchar(32), 
#         ) 
#     '''
#     cursor.execute(sql) 
#     print("created user table successfully")
#     conn.commit()
#     conn.close()

# def insertUser(id, pw, name, auth):
#     conn = pymysql.connect(host='172.33.0.2', user='root', password='abcd', db='cloud', charset='utf8')
#     cursor = conn.cursor()
#     sql = 'INSERT INTO user (account, passwd, name, auth) VALUES (%s, %s, %s, %s)'
#     cursor.execute(sql, (id, pw, name, auth))
#     conn.commit()
#     conn.close()
def selectWebContentsFromId(userId):
    conn = pymysql.connect(host='172.33.0.2', user='root', password='abcd', db='cloud', charset='utf8')
    cursor = conn.cursor()
    sql = "SELECT * FROM web_contents where user_id=%s"
    cursor.execute(sql, (userId))
    res = cursor.fetchall()
    webContents = res
    print("ID       CONTENTS")
    for webContent in webContents:
        print(webContent[1], webContent[2], sep='\t')
    conn.close()

def selectAllWebContents():
    conn = pymysql.connect(host='172.33.0.2', user='root', password='abcd', db='cloud', charset='utf8')
    cursor = conn.cursor()
    sql = "SELECT * FROM web_contents"
    cursor.execute(sql)
    res = cursor.fetchall()
    webContents = res
    print("INDEX    ID       CONTENTS")
    for webContent in webContents:
        print(webContent[0], webContent[1], webContent[2], sep='\t')
    conn.close()

def createWebContentsTable():
    conn = pymysql.connect(host='172.33.0.2', user='root', password='abcd', db='cloud', charset='utf8')
    cursor = conn.cursor()
    sql = ''' 
         CREATE TABLE web_contents ( 
            idx int(10) NOT NULL AUTO_INCREMENT PRIMARY KEY,
            user_id varchar(32),
            contents TEXT,
            FOREIGN KEY (user_id) REFERENCES user (id)
            )
            '''

    cursor.execute(sql)
    print("created AgnetLog table successfully")
    conn.commit()
    conn.close()

# createUserTable()
# insertUser("han","0000","seunghun","1")
# insertUser("ddd","0000","seunghun","1")
# insertUser("hbban","0000","seunghun","1")
# insertUser("yyy","0000","seunghun","1")

