import Utills.DBUser as DBUser
import Pages.user as user
import Pages.admin as admin
import os

def printManual():
    os.system('clear')
    while True:
        print("<로그인 해주세요. (종료: q)>")
        userID = input("ID: ")
        if userID == 'q':
            break
        userPWD = input("Password: ")
        # DBUser.login() 호출하여 ID & PWD 확인
        login(userID, userPWD)
        
def login(id, pw):
    userInfo = DBUser.login(id, pw)
    if not userInfo:
        os.system('clear')
        print("사용자 정보가 없습니다. 다시 입력해주세요.")
    else:
        checkAuth(userInfo, id, pw)
    

def checkAuth(userInfo, userID, userPWD):
    userID = userID
    userPWD = userPWD

    userInfo = list(userInfo)
    auth = userInfo[0][0]
    if auth == 0:
        adminPage = admin.AdminPage(userID)
        adminPage.printMenual()
    elif auth == 1:
        # user.py 호출 --> 메뉴 선택에 따른 처리 결과를 result에 저장
        # --> result에 따른 결과를 사용자에게 출력
        userPage = user.UserPage(userID)
        userPage.printMenual()
        # result = user.choiceMenu(userID, userPWD)
        # user.printResult(result)
    else:
        print("AUTH ERROR")