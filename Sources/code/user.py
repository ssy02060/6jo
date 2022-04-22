import pymysql
import DBUser

def printMenu():
    print("메뉴를 선택해주세요")
    print("----------------------")
    print("1) 사용자 수정")
    print("2) 사용자 로그 조회")
    print("3) 작성한 Web Contents 확인")
    print("4) 로그아웃")
    menu = input("-----------------------\n")

    return menu

def choiceMenu(userID, userPWD):
    ID = userID
    PWD = userPWD

    while True:
        menu = printMenu()
        if menu == '1':
            print("수정할 항목을 선택해주세요 (종료: q)")
            print("--------------------------")
            print("1) ID 수정")
            print("2) Password 수정")
            print("3) name 수정")
            subMenu = input("--------------------------\n")

            if subMenu == 'q':
                return ''
            
            if subMenu == '1':
                edit = input("수정할 ID를 입력해주세요: ")
            elif subMenu == '2':
                edit = input("수정할 password를 입력해주세요: ")
            elif subMenu == '3':
                edit = input("수정할 사용자 이름을 입력해주세요: ")
            
            # DBUser.updateUser() 호출
            res = DBUser.updateUser(subMenu, edit, ID, PWD)
            return res
            
        elif menu == '2':

            conn = pymysql.connect(host='172.19.0.2', user='root', password='abcd', db='test', charset='utf8')
            cursor = conn.cursor()

            print("사용자 로그를 조회합니다.")
            sql = "SELECT * FROM AgentLog"
            cursor.execute(sql)
            result = cursor.fetchall()
            conn.commit()
            conn.close()
            return result
        elif menu == '3':
            print("작성한 Web Contents 확인\n")
            return ''
            break
        elif menu == '4':
            print("로그아웃\n")
            return ''
            break
        else:
            print("잘못된 입력값입니다.\n")
            continue

