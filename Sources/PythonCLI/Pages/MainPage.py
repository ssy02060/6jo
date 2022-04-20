from .Page import Page
class MainPage(Page):
    def printManual(self):
        print("메인 페이지입니다. (1 ~ 4 사이 번호를 입력하세요)")
        print("1. 사용자 관리")
        print("2. 로그 확인")
        print("3. 웹 컨텐츠 확인")
        print("4. 사용자 관리")
