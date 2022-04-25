import pymysql
import Utills.DBUser as DBUser
import Utills.DBLog as DBLog
import Pages.login as login
import Utills.DBWebContents as DBWebContents
import os

class UserPage:
    def __init__(self, id):
        self.userId = id
# 유저 메인 페이지
    def printMenual(self):
        os.system('clear')
        menu = input('''
사용자 페이지 입니다.
----------------------------
1. 사용자 수정
2. 사용자 로그 조회
3. 작성한 Web Contents 확인
----------------------------
*로그아웃하려면 Q를 누르세요*
''')
        self.choice(menu)
        return menu

    def choice(self,menu):
        if menu == '1':
            self.updateUserMenu()
        elif menu == '2':
            self.logMenu()
            pass
        elif menu == '3':
            self.printWebContentsMenu()
            self.inputWebContentsMenu()
        elif menu == 'q' or menu == 'Q':
            login.printManual()
        else:
            print("옵션을 확인하세요")
            self.printMenual()
# 유저 로그 페이지
    def logMenu(self):
        self.printLogMenu()
        self.inputLogMenu()
        
    def printLogMenu(self):
        os.system('clear')
        print('''
        ----------------------------
        사용자 로그를 조회합니다.
        ----------------------------
        ''')
        DB_line = len(DBLog.selectLog(self.userId))
        DBLog.autoSaveLog(DB_line)

        logs = DBLog.selectLog(self.userId)
        print("ID   IP      DATE            METHOD  URL              STATUS  DETAILS")
        for log in logs:
            userId  = log[0]
            userIP  = log[1]
            date    = log[2]
            method  = log[3]
            url     = log[4]
            status  = str(log[5])
            details = log[6]
            print(userId,userIP,date,method,url,status)
        print("*나가려면 q, 새로고침하려면 r을 입력하세요*")     

    def inputLogMenu(self):
        option = input()
        if option == 'q' or option == 'Q':
            self.printMenual()
        elif option == 'r' or option == 'R':
            self.logMenu()
        else:
            print("옵션을 확인하세요")
            self.logMenu()

# user web contents 페이지
    def webContentsMenu(self):
        self.printWebContentsMenu()
        self.inputWebContentsMenu()
    def printWebContentsMenu(self):
        os.system('clear')
        print('''
----------------------------
%s님의 글 목록을 조회합니다.
----------------------------''' % (self.userId))
        DBWebContents.selectWebContentsFromId(self.userId)
        print("*나가려면 q를 입력하세요*")

    def inputWebContentsMenu(self):
        option = input()
        if option == 'q' or option == 'Q':
            self.printMenual()
        else:
            print("옵션을 확인하세요")
            self.webContentsMenu()

# user my page 페이지
    def updateUserMenu(self):
        self.printUpdateUserMenu()
        self.inputUpdateUserMenu()

    def printUpdateUserMenu(self):
        os.system('clear')
        print('''
수정할 항목을 선택해주세요.
----------------------------
1. Password
2. Name
----------------------------
*나가려면 Q를 입력하세요*

    ''')

    def inputUpdateUserMenu(self):
        updateOption = input()
        if updateOption == '1':
            self.updateUserPassword()
        elif updateOption == '2':
            self.updateUserName()
        elif updateOption == 'q' or updateOption ==  'Q':
            self.printMenual()
        else:
            os.system('clear')
            print("옵션을 확인하세요")
            self.updateUserMenu()


    def updateUserName(self):
        os.system('clear')
        print("수정할 Name을 입력해주세요 : ") 
        editName = input()
        res = DBUser.updateName(self.userId, editName)
        print("수정이 완료되었습니다. 다시 로그인 하세요.")
        login.printManual()

    def updateUserPassword(self):
        os.system('clear')
        print("수정할 Password를 입력해주세요 : ")
        editPassword = input()
        res = DBUser.updatePassword(self.userId, editPassword)
        print("수정이 완료되었습니다. 다시 로그인 하세요.")
        login.printManual()
