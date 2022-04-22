import pymysql



def createUserTable():
    conn = pymysql.connect(host='172.33.0.2', user='root', password='abcd', db='cloud', charset='utf8')
    cursor = conn.cursor()
    sql ='''
        CREATE TABLE user ( 
            auth int(2)
            account varchar(32) NOT NULL PRIMARY KEY,
            passwd  varchar(32),
            name varchar(32), 
        ) 
    '''
    cursor.execute(sql) 
    print("created user table successfully")
    conn.commit()
    conn.close()

def insertUser(id, pw, name, auth):
    conn = pymysql.connect(host='172.33.0.2', user='root', password='abcd', db='cloud', charset='utf8')
    cursor = conn.cursor()
    sql = 'INSERT INTO user (account, passwd, name, auth) VALUES (%s, %s, %s, %s)'
    cursor.execute(sql, (id, pw, name, auth))
    conn.commit()
    conn.close()

def selectAllUser():
    conn = pymysql.connect(host='172.33.0.2', user='root', password='abcd', db='cloud', charset='utf8')
    cursor = conn.cursor()
    sql = "SELECT * FROM user"
    cursor.execute(sql)
    res = cursor.fetchall()
    users = res
    print(users[0][3])
    for user in users:
        print(user)
    conn.commit()
    conn.close()

# createUserTable()
# insertUser("han","0000","seunghun","1")
# insertUser("ddd","0000","seunghun","1")
# insertUser("hbban","0000","seunghun","1")
# insertUser("yyy","0000","seunghun","1")
selectAllUser()

