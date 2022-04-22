import pymysql
import user

userID = ""
userPWD = ""

while True:
    print("<로그인 해주세요. (종료: q)>")
    userID = input("id: ")
    if userID == "q":
        break
    userPWD = input("password: ")

    # DBUser.login() 호출
    login = DBUser.login(userID, userPWD)
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
        else: print("AUTH ERROR")