import pymysql

def createUserTable():
    conn = pymysql.connect(host='172.33.0.2', user='root', password='abcd', db='cloud', charset='utf8')
    cursor = conn.cursor()
    sql ='''
        CREATE TABLE user ( 
            auth int(2),
            id varchar(32) NOT NULL PRIMARY KEY,
            passwd  varchar(32),
            name varchar(32)
        ) 
    '''
    cursor.execute(sql) 
    print("created user table successfully")
    conn.commit()
    conn.close()

def insertUser(auth, id, pw, name):
    conn = pymysql.connect(host='172.33.0.2', user='root', password='abcd', db='cloud', charset='utf8')
    cursor = conn.cursor()

    # 사용자를 추가하기 전에 일치하는 사용자가 있는지 확인
    validationSQL = "SELECT * FROM user where id=%s"
    cursor.execute(validationSQL, id)
    validation = cursor.fetchall()
    if not validation:
        sql = 'INSERT INTO user (auth, id, passwd, name) VALUES (%s, %s, md5(%s), %s)'
        cursor.execute(sql, (auth, id, pw, name))
        conn.commit()
        conn.close()
        return 1
    else:
        conn.close()
        return 0


    # sql = 'INSERT INTO user (auth, id, passwd, name) VALUES (%s, %s, md5(%s), %s)'
    # cursor.execute(sql, (auth, id, pw, name))
    # conn.commit()
    # conn.close()

def selectAllUser():
    conn = pymysql.connect(host='172.33.0.2', user='root', password='abcd', db='cloud', charset='utf8')
    cursor = conn.cursor()
    sql = "SELECT * FROM user"
    cursor.execute(sql)
    res = cursor.fetchall()
    users = res
    print("ID       PW      NAME        AUTH")
    for user in users:
        print(user[1],user[2], user[3], user[0], sep="\t")
    conn.commit()
    conn.close()
    return len(users)

def selectUser(userID):
    conn = pymysql.connect(host='172.33.0.2', user='root', password='abcd', db='cloud', charset='utf8')
    cursor = conn.cursor()
    sql = "SELECT * FROM user where id=%s"
    cursor.execute(sql,userID)
    res = cursor.fetchall()
    user = res
    conn.commit()
    conn.close()
    return user

def deleteUser(userID):
    conn = pymysql.connect(host='172.33.0.2', user='root', password='abcd', db='cloud', charset='utf8')
    cursor = conn.cursor()

    sql = "DELETE FROM user where id=%s"
    cursor.execute(sql,userID)

    conn.commit()
    conn.close()

def selectAllUserWithIndex():
    conn = pymysql.connect(host='172.33.0.2', user='root', password='abcd', db='cloud', charset='utf8')
    cursor = conn.cursor()
    sql = "SELECT * FROM user"
    cursor.execute(sql)
    res = cursor.fetchall()
    users = res
    i = 0
    print("INDEX  ID       PW      NAME        AUTH")
    for user in users:
        print(i,user[1],user[2], user[3], user[0], sep="\t")
        i+=1
    conn.commit()
    conn.close()
    return len(users)

def updateUser(menu, edit, id, pw):
    menu = menu
    edit = edit
    id = id
    pw = pw
    
    conn = pymysql.connect(host='172.33.0.2', user='root', password='abcd', db='cloud', charset='utf8')
    cursor = conn.cursor()
    
    # 사용자 정보를 수정하기 전에 일치하는 사용자가 있는지 확인
    # validationSQL = "SELECT * FROM user where id=%s and passwd=md5(%s)"
    # cursor.execute(validationSQL, (id, pw))
    # validation = cursor.fetchall()
    # if not validation:
    #     print("사용자 정보가 없습니다.")
    #     return ""
    
    # 사용자 정보 수정
    if menu == '1':
        sql = "UPDATE user set passwd=md5('"+edit+"') where id=%s and passwd=md5(%s)"
    elif menu == '2':
        sql = "UPDATE user set name='"+edit+"' where id=%s and passwd=md5(%s)"

    cursor.execute(sql, (id, pw))
    res = cursor.fetchall()
    conn.commit()
    conn.close()
    return res

def updatePassword(id, editPassword):
    conn = pymysql.connect(host='172.33.0.2', user='root', password='abcd', db='cloud', charset='utf8')
    cursor = conn.cursor()
    sql = "UPDATE user set passwd=md5(%s) where id=%s"
    cursor.execute(sql, (editPassword, id))
    res = cursor.fetchall()
    conn.commit()
    conn.close()
    return res

def updateName(id, editName):
    conn = pymysql.connect(host='172.33.0.2', user='root', password='abcd', db='cloud', charset='utf8')
    cursor = conn.cursor()
    sql = "UPDATE user set name=%s where id=%s"
    cursor.execute(sql, (editName, id))
    res = cursor.fetchall()
    conn.commit()
    conn.close()
    return res

def updateAuth(id, editAuth):
    conn = pymysql.connect(host='172.33.0.2', user='root', password='abcd', db='cloud', charset='utf8')
    cursor = conn.cursor()
    sql = "UPDATE user set auth=%s where id=%s"
    cursor.execute(sql, (editAuth, id))
    res = cursor.fetchall()
    conn.commit()
    conn.close()
    return res

def login(id, pw):
    id = id
    pw = pw

    conn = pymysql.connect(host='172.33.0.2', user='root', password='abcd', db='cloud', charset='utf8')
    cursor = conn.cursor()
    sql = "SELECT * FROM user where id=%s and passwd=md5(%s)"
    cursor.execute(sql, (id, pw))
    userInfo = cursor.fetchall()
    conn.commit()
    conn.close()
    return userInfo

# createUserTable()
#insertUser("1","han","0000","seunghun")
#insertUser("1","ddd","0000","seunghun")
#insertUser("1","hbban","0000","seunghun")
#insertUser("1","yyy","0000","seunghun")
#selectAllUser()
#print("")
#login('dd(d', '0000')
#updateUser('2', 'han', 'han', '1111')
#print("")
#selectAllUser()
