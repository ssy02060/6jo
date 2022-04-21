import pymysql
import user
import admin

# !TODO DB 정보 맞춰서 입력하기
conn = pymysql.connect(host='172.19.0.2', user='root', password='abcd', db='test', charset='utf8')
cursor = conn.cursor()

userID = ""
userPWD = ""

# !TODO DB  생성하는 코드 추가하기
# sql = "CREATE DATABASE test"
# cursor.execute(sql)

# !TODO DB 테이블 생성하는 코드 추가하기
# !TODO 필드 - 타입 맞춰서 입력하기
# sql = "CREATE TABLE user ( auth int(2), idx int(11) NOT NULL AUTO_INCREMENT PRIMARY KEY, account varchar(255), passwd varchar(255), name varchar(255) )"


# 로그인 --> 사용자 권한 확인
sql = "SELECT auth FROM user where account = %s and passwd = md5(%s)"
sql2 = "SELECT * FROM AgentLog"

while True:
    print("<로그인 해주세요. (종료: q)>")
    userID = input("id: ")
    if userID == "q":
        break
    userPWD = input("password: ")

    cursor.execute(sql, (userID, userPWD))
    login = cursor.fetchall()

    if not login:
        print("사용자 정보가 없습니다. 다시 입력해주세요.\n")
    else:
        login = list(login)
        auth = login[0][0]
        if auth == 0:
            print("관리자입니다.\n")
            admin.choiceMenu()
        elif auth == 1:
            print("사용자입니다.\n")
            userSQL = user.choiceMenu()
            cursor.execute(userSQL, (userID, userPWD))
            result = cursor.fetchall()
            conn.commit()
            print("완료되었습니다. 시스템을 종료합니다.")
            break

        else:
            print("DEBUG >>>>> AUTH ERROR")


    conn.commit()

conn.close()
