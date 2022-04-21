def printMenu():
    print("메뉴를 선택해주세요")
    print("----------------------")
    print("1) 사용자 수정")
    print("2) 사용자 로그 조회")
    print("3) 작성한 Web Contents 확인")
    print("4) 로그아웃")
    menu = input("-----------------------\n")

    return menu

def choiceMenu():
    while True:
        menu = printMenu()
        if menu == '1':
            print("수정할 항목을 선택해주세요")
            print("--------------------------")
            print("1) ID 수정")
            print("2) Password 수정")
            print("3) name 수정")
            subMenu = input("--------------------------\n")

            if subMenu == '1':
                edit = input("수정할 ID를 입력해주세요: ")
                sql = "UPDATE user set account='"+edit+"' where account=%s and passwd=md5(%s)"
                return sql
            elif subMenu == '2':
                edit = input("수정할 Password를 입력해주세요: ")
                sql = "UPDATE user set passwd=md5('"+edit+"') where account=%s and passwd=md5(%s)"
                return sql
            elif subMenu == '3':
                edit = input("수정할 사용자 이름을 입력해주세요: ")
                sql = "UPDATE user set name='"+edit+"' where account=%s and passwd=md5(%s)"
                return sql
            else:
                pass

            
        elif menu == '2':
            print("사용자 로그 조회\n")
        elif menu == '3':
            print("작성한 Web Contents 확인\n")
            break
        elif menu == '4':
            print("로그아웃\n")
            break
        else:
            print("잘못된 입력값입니다.\n")
            continue


