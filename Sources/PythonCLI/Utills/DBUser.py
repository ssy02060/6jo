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
    sql = 'INSERT INTO user (auth, id, passwd, name) VALUES (%s, %s, md5(%s), %s)'
    cursor.execute(sql, (auth, id, pw, name))
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

def updateUser(menu, edit, id, pw):
    menu = menu
    edit = edit
    id = id
    pw = pw
    
    conn = pymysql.connect(host='172.33.0.2', user='root', password='abcd', db='cloud', charset='utf8')
    cursor = conn.cursor()
    
    # 사용자 정보를 수정하기 전에 일치하는 사용자가 있는지 확인
    validationSQL = "SELECT * FROM user where id=%s and passwd=md5(%s)"
    cursor.execute(validationSQL, (id, pw))
    validation = cursor.fetchall()
    if not validation:
        print("사용자 정보가 없습니다.")
        return ""
    
    # 사용자 정보 수정
    if menu == '1':
        sql = "UPDATE user set id='"+edit+"' where id=%s and passwd=md5(%s)"
    elif menu == '2':
        sql = "UPDATE user set passwd=md5('"+edit+"') where id=%s and passwd=md5(%s)"
    elif menu == '3':
        sql = "UPDATE user set name='"+edit+"' where id=%s and passwd=md5(%s)"
    elif menu == 'q':
        return ''
    
    cursor.execute(sql, (id, pw))
    res = cursor.fetchall()
    conn.commit()
    conn.close()
    print("변경 되었습니다.")
    return res

def login(id, pw):
    id = id
    pw = pw

    conn = pymysql.connect(host='172.33.0.2', user='root', password='abcd', db='cloud', charset='utf8')
    cursor = conn.cursor()
    sql = "SELECT * FROM user where id=%s and passwd=md5(%s)"
    cursor.execute(sql, (id, pw))
    res = cursor.fetchall()
    conn.commit()
    conn.close()
    return res


#createUserTable()
#insertUser("1","han","0000","seunghun")
#insertUser("1","ddd","0000","seunghun")
#insertUser("1","hbban","0000","seunghun")
#insertUser("1","yyy","0000","seunghun")
selectAllUser()
print("")
#login('dd(d', '0000')
#updateUser('3', 'han', 'aaa', '1111')
#print("")
#selectAllUser()