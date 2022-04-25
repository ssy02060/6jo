from this import d
import pymysql
import Utills.DBUser as DBUser
import Utills.DBLog as DBLog
import Pages.login as login
import Utills.DBWebContents as DBWebContents
import os
import importlib
importlib.reload(DBLog)


class AdminPage:
    def __init__(self, id):
        self.userId = id
# 유저 메인 페이지
    def printMenual(self):
        os.system('clear')
        menu = input('''
관리자 페이지 입니다.
----------------------------
1. 사용자 관리
2. 로그 조회
3. Web Contents 목록
----------------------------
*로그아웃하려면 Q를 누르세요*
''')
        self.choice(menu)
        return menu


    def choice(self,menu):
        if menu == '1':
            self.manageUserMenu()
        elif menu == '2':
            self.logMenu()
        elif menu == '3':
            self.printWebContentsMenu()
            self.inputWebContentsMenu()
        elif menu == 'q' or menu == 'Q':
            login.printManual()
        else:
            print("옵션을 확인하세요")
            self.printMenual()


# 관리자 로그 페이지
    def logMenu(self):
        self.loadLog()
        self.printLogMenu()
        self.inputLogMenu()
        
    def printLogMenu(self):
        os.system('clear')
        print('''
----------------------------
사용자 로그를 조회합니다.
----------------------------''')        
        # 로그 출력
        self.printLogs()
        print("*나가려면 q, 새로고침하려면 r을 입력하세요*")     

    def loadLog(self):
        DB_line = len(DBLog.selectAllLog())
        DBLog.autoSaveLog(DB_line)

    def printLogs(self):
        logs = DBLog.selectAllLog()
        
        print("ID   IP      DATE            METHOD  URL              STATUS")
        for log in logs:
            userId  = log[0]
            userIP  = log[1]
            date    = log[2]
            method  = log[3]
            url     = log[4]
            status  = str(log[5])
            details = log[6]
            print(userId,userIP,date,method,url,status)

    def inputLogMenu(self):
        option = input()
        if option == 'q' or option == 'Q':
            self.printMenual()
        elif option == 'r' or option == 'R':
            self.logMenu()
        else:
            print("옵션을 확인하세요")
            self.logMenu()

# 관리자 web contents 페이지
    def webContentsMenu(self):
        self.printWebContentsMenu()
        self.inputWebContentsMenu()
    
    
    def printWebContentsMenu(self):
        os.system('clear')
        print('''
----------------------------
전체 글 목록을 조회합니다.
----------------------------''')
        DBWebContents.selectAllWebContents()
        print("*나가려면 q를 입력하세요*")


    def inputWebContentsMenu(self):
        option = input()
        if option == 'q' or option == 'Q':
            self.printMenual()
        else:
            print("옵션을 확인하세요")
            self.webContentsMenu()

# 유저 관리 page
    def manageUserMenu(self):
        self.printManageUserMenu()
        self.inputManageUserMenu()
        return


    def printManageUserMenu(self):
        os.system('clear')
        print('''
사용자 관리항목을 선택해주세요.
----------------------------
1. 사용자 생성
2. 사용자 목록 보기
3. 사용자 정보 수정
4. 사용자 정보 삭제
----------------------------
*나가려면 Q를 입력하세요*''')


    def inputManageUserMenu(self):
        option = input()
        if option == '1':
            self.insertUserMenu()
        elif option == '2':
            self.selectAllUserMenu()
        elif option == '3':
            self.updateUser()
        elif option == '4':
            self.deleteUser()
        elif option == 'q' or option ==  'Q':
            self.printMenual()
        else:
            os.system('clear')
            print("옵션을 확인하세요")
            self.manageUserMenu()


# 유저 생성
    def insertUserMenu(self):
        self.printInsertMenu()
        self.inputUserInfo()
    

    def printInsertMenu(self):
        os.system("clear")
        print('''
사용자 생성 메뉴입니다. 사용자 정보를 입력하세요.
----------------------------''')

    def inputUserInfo(self):
        userId    = input("ID             : ")
        pw = self.inputPw()
        name      = input("이름           : ")
        auth      = input("권한           : ")
        self.insertUser(auth, userId, pw, name)


    def inputPw(self):
        pw        = input("PASSWORD       : ")
        confirmPw = input("PASSWORD 확인  : ")
        while(pw != confirmPw):
            print("비밀번호가 일치하지 않습니다. 다시 입력하세요")
            pw        = input("PASSWORD       : ")
            confirmPw = input("PASSWORD 확인  : ")
        return pw


    def insertUser(self, auth, userId, pw, name):
        DBUser.insertUser(auth,userId,pw,name)
        print("%s 님이 추가되었습니다. 나가려면 아무 키나 입력하세요." % userId)
        self.quitToUserManagePage()

        
# 유저 조회
    def selectAllUserMenu(self):
        self.printAllUserMenu()
        self.selectAllUser()
    
    def printAllUserMenu(self):
        os.system("clear")
        print('''
전체 사용자 목록을 조회합니다.
----------------------------''')

    def selectAllUser(self):
        DBUser.selectAllUser()
        self.quitToUserManagePage()
    

    def quitToUserManagePage(self):
        print("*나가려면 아무 키나 입력하세요*")
        input()
        self.manageUserMenu()
        return

# 사용자 수정
    def updateUser(self):
        self.updateWithUserList()
        self.quitToUserManagePage()
        return

    def updateWithUserList(self):
        self.printUserListForUpdate()
        self.inputUserNameForUpdate()
        return
    
    def printUserListForUpdate(self):
        os.system("clear")
        print('''
사용자 수정 페이지입니다. (사용자 목록)
----------------------------''')
        DBUser.selectAllUser()
        print("수정할 유저 ID를 입력하세요. (나가려면 q를 입력하세요)")
        return
    
    def inputUserNameForUpdate(self):
        userId = input("ID : ")
        if(userId == 'q'):
            self.manageUserMenu()
            return
        user = DBUser.selectUser(userId)
        
        while not user:
            self.printUserListForUpdate()
            print(user)
            print("해당 유저는 존재하지 않습니다. ID를 확인해 주세요")
            userId = input("ID : ")
            if(userId == 'q'):
                self.manageUserMenu()
                return
            user = DBUser.selectUser(userId)
        self.updateWithUserID(userId)
        return

    def updateWithUserID(self, updateUserID):
        self.printUpdateUserMenuWithUserID()
        self.inputUpdateUserMenu(updateUserID)
        return

    def printUpdateUserMenuWithUserID(self):
        os.system('clear')
        print('''
수정할 항목을 선택해주세요.
----------------------------
1. Password
2. Name
3. Permission
----------------------------
*나가려면 Q를 입력하세요*''')
        return

    def inputUpdateUserMenu(self, updateUserID):
        updateOption = input()
        if updateOption == '1':
            self.updateUserPassword(updateUserID)
        elif updateOption == '2':
            self.updateUserName(updateUserID)
        elif updateOption == '3':
            self.updateUserAuth(updateUserID)
        elif updateOption == 'q' or updateOption ==  'Q':
            self.manageUserMenu()
        else:
            os.system('clear')
            print("옵션을 확인하세요")
            self.updateWithUserID(updateUserID)
        return
    

    def quitToUpdateUserPage(self):
        print("*나가려면 아무 키나 입력하세요*")
        input()
        self.updateUser()
        return


    def updateUserAuth(self, targetId):
        os.system('clear')
        editAuth = self.inputAuth()
        DBUser.updateAuth(targetId, int(editAuth))
        print("수정이 완료되었습니다.")
        self.quitToUserManagePage()
        return
    

    def inputAuth(self):
        auth = input("권한을 입력하세요 (0 또는 1) : ")
        while(not(auth == '0' or auth == '1')):
            print("---------AUTH ERROR---------")
            auth = input("권한을 입력하세요 (0 또는 1) : ")
        return auth


    def updateUserName(self, targetId):
        os.system('clear')
        print("수정할 Name을 입력해주세요 : ") 
        editName = input()
        res = DBUser.updateName(targetId, editName)
        print("수정이 완료되었습니다.")
        self.quitToUserManagePage()
        return


    def updateUserPassword(self, targetId):
        os.system('clear')
        print("수정할 Password를 입력해주세요 : ")
        editPassword = input()
        res = DBUser.updatePassword(targetId, editPassword)
        self.quitToUserManagePage()
        return

# 사용자 삭제 페이지
    def deleteUser(self):
        self.printUserListForDelete()
        self.inputUserNameForDelete()

        
    def printUserListForDelete(self):
        os.system("clear")
        print('''
사용자 삭제 페이지입니다. (사용자 목록)
----------------------------''')
        DBUser.selectAllUser()
        print("수정할 유저 ID를 입력하세요. (나가려면 q를 입력하세요)")
        return

    def inputUserNameForDelete(self):
        userId = input("ID : ")
        if(userId == 'q'):
            self.manageUserMenu()
            return
        user = DBUser.selectUser(userId)
        
        while not user:
            self.printUserListForDelete()
            print(user)
            print("해당 유저는 존재하지 않습니다. ID를 확인해 주세요")
            userId = input("ID : ")
            if(userId == 'q'):
                self.manageUserMenu()
                return
            user = DBUser.selectUser(userId)
        self.deleteWithUserId(userId)
        return
    
    def deleteWithUserId(self, userID):
        os.system("clear")
        print(userID+ "님을 삭제 하시겠습니까? (y/n)")
        yn = input()
        if(yn == 'y'):
            DBUser.deleteUser(userID)
            print(userID + "님이 삭제되었습니다.")
            self.quitToUserManagePage()
        else:
            print(userID + "님을 삭제하지 않습니다.")
            self.quitToUserManagePage()
