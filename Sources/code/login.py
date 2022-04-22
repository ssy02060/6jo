import DBUser
import user

def printManual():
    while True:
        print("<로그인 해주세요. (종료: q)>")
        userID = input("ID: ")
        if userID == 'q':
            break
        userPWD = input("Password: ")

        # DBUser.login() 호출하여 ID & PWD 확인
        userInfo = DBUser.login(userID, userPWD)
        if not userInfo:
            print("사용자 정보가 없습니다. 다시 입력해주세요.\n")
        else:
            checkAuth(userInfo, userID, userPWD)

def checkAuth(userInfo, userID, userPWD):
    userID = userID
    userPWD = userPWD

    userInfo = list(userInfo)
    auth = userInfo[0][0]
    if auth == 0:
        print("관리자입니다.\n")
    elif auth == 1:
        print("사용자입니다.\n")
        # user.py 호출 --> 메뉴 선택에 따른 처리 결과를 result에 저장
        # --> result에 따른 결과를 사용자에게 출력
        result = user.choiceMenu(userID, userPWD)
        user.printResult(result)
    else:
        print("AUTH ERROR")

printManual()