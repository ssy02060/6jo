import subprocess

def PrintMenu():
	print("관리자 페이지입니다.")
	global menu
	menu = input('''
				--------------------
				1. 사용자 관리 페이지
				2. Log 목록
				3. Web Contents 목록
				--------------------
				*나가려면 Q를 누르세요*''')

def ChoiceMenu():
	while True:
		if menu == '1':
			subprocess.call("admin_user_manage.py")
			break
		elif menu == '2':
			subprocess.call("admin_log.py")
			break
		elif menu == '3':
			subprocess.call("admin_web_contents.py")
			break
		elif menu == 'Q' or 'q':
			exit()
		else:
			print("다시 입력하세요.")


if __name__ == "__main__":
	PrintMenu()
	ChoiceMenu()