import pymysql

conn = pymysql.connect(host='172.33.0.2', user='root', password='abcd', db='cloud', charset='utf8')
cursor = conn.cursor()

def createUserTable():
    sql ='''
        CREATE TABLE user ( 
            account varchar(32) NOT NULL PRIMARY KEY,
            passwd  varchar(32),
            name varchar(32), 
            auth int(2)
        ) 
    '''
    cursor.execute(sql) 
    print("created user table successfully")
    conn.commit()

def insertUser(id, pw, name, auth):
    sql = 'INSERT INTO user (account, passwd, name, auth) VALUES (%s, %s, %s, %s)'
    cursor.execute(sql, (id, pw, name, auth))
    conn.commit()

def selectAllUser():
    sql = "SELECT * FROM user"
    cursor.execute(sql)
    res = cursor.fetchall()
    users = res
    print(users[0][3])
    for user in users:
        print(user)
    conn.commit()

# createUserTable()
# insertUser("han","0000","seunghun","1")
# insertUser("ddd","0000","seunghun","1")
# insertUser("hbban","0000","seunghun","1")
# insertUser("yyy","0000","seunghun","1")
selectAllUser()

conn.close()