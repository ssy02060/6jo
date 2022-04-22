import pymysql
import string


def PrintMenu():
	global menu
	menu = input('''
				-------------------
				1. 사용자 생성
				2. 사용자 목록 보기
				3. 사용자 정보 수정
				4. 사용자 정보 삭제
				-------------------
				나가려면 Q를 누르세요
				''')


def ChoiceMenu():
	while True:
		if menu == '1':
			AddUser()
			break
		elif menu == '2':
			print(UserList())
			break
		elif menu == '3':
			ModifyUser()
			break
		elif menu == '4':
			DeleteUser()
			break
		elif menu == 'Q' or 'q':
			exit()
		else:
			print("다시 입력하세요.")



def AddUser()):
	conn = pymysql.connect(host='localhost', user='root', password='rootPassword', db='dbName', charset='utf8')
	cur = conn.cursor()

	userID = input("ID: ")
	pw = input("PW: ")
	name = input("NAME: ")
	permission = int(input('''PERMISSION: 
							1. ALL 
							2. SELECT(조회)
							'''))

	query1 = "create user {userID} identify by {pw}; insert into userTable('NAME') values('{name}')".format(userID=userID, pw=pw, name=name) # 계정생성
	cur.execute(query1)

	if permission == 1:	
		query2 = 'grant all privileges on dbName.* to {userID}@localhost'.format(userID=userID) # userID에게 dbName 데이터베이스에 모든 권한 부여
		cur.execute(query2)
	elif permission == 2:
		query3 = 'grant select on dbName.* {userID}@localhost'.format(userID=userID)
		cur.execute(query3)

	cur.commit()
	conn.close()


def UserList():
	conn = pymysql.connect(host='localhost', user='root', password='rootPassword', db='dbName', charset='utf8')
	cur = conn.cursor()

	query = 'select * from userTable'
	cur.execute(query)
	cur.commit()
	result = cur.fetchall()

	userLists = []
	for data in result:
		userLists.append(data)
	conn.close()
	#print(userLists)

	return userLists


def ModifyUser():
	conn = pymysql.connect(host='localhost', user='root', password='rootPassword', db='dbName', charset='utf8')
	cur = conn.cursor()

	userName = input("수정할 ID: ")

	if userName not in UserList():
		print("없는 사용자입니다.")
	else:
		while True:
			modList = input("수정할 정보를 선택하세요: ")
			print("1. PW")
			print("2. NAME")
			print("3. PERMISSION")
			print("4. 전부")

			if modList == 1:
				pw = input("수정할 PW: ")
				query1 = "alter user '{userName}'@'localhost' identified with mysql_native_password by {pw}".format(userName=userName, pw=pw)
				cur.execute(query1)
				cur.commit()

			elif modList == 2:
				name = input("수정할 NAME: ")
				query2 = "update userTable set NAME={name} where id={userName}".format(name=name, userName=userName)
				cur.execute(query2)
				cur.commit()

			elif modList == 3:
				permission = input("수정할 PERMISSION: ")
				query3 = "update userTable set PERMISSION={permission} where id={userName}".format(permission=permission, userName=userName)
				cur.execute(query3)
				cur.commit()

			elif modList == 4:
				pw = input("수정할 PW: ")
				name = input("수정할 NAME: ")
				permission = input("수정할 PERMISSION: ")
				query4 = '''
					alter user '{userName}'@'localhost' identified with mysql_native_password by {pw}
					update userTable set NAME={name} where id={userName}
					update userTable set PERMISSION={permission} where id={userName}
					'''.format(userName=userName, pw=pw, name=name, userName=userName, permission=permission, userName=userName)
				cur.execute(query3)
				cur.commit()

			else:
				break

	conn.close()			


def DeleteUser():
	conn = pymysql.connect(host='localhost', user='root', password='rootPassword', db='dbName', charset='utf8')
	cur = conn.cursor()

	userName = input("삭제할 사용자: ")

	if userName not in UserList():
		print("없는 사용자입니다.")
	else:
		query = "delete from userTable where id={userName}".format(userName=userName)
		cur.execute(query)
		cur.commit()

	conn.close()
		

if __name__ == "main":
	PrintMenu()
	ChoiceMenu()


