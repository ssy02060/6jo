import pymysql
import user

# !TODO DB 정보 맞춰서 입력하기
conn = pymysql.connect(host='172.19.0.2', user='root', password='abcd', db='test', charset='utf8')
cursor = conn.cursor()

userID = ""
userPWD = ""

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
        elif auth == 1:
            print("사용자입니다.\n")
            result = user.choiceMenu(userID, userPWD)

            if not result:
                break
            elif result == '':
                break
            else:
                print(result)
                break

        else:
            print("DEBUG >>>>> AUTH ERROR")


    conn.commit()

conn.close()
