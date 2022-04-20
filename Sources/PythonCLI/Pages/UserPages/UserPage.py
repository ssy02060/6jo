from ..MainPage import MainPage
class UserPage(MainPage):
    def printManual(self):
        print("메인 페이지입니다. (1 ~ 4 사이 번호를 입력하세요)")
        print("1. 본인 계정 수정")
        print("2. 로그 확인")
        print("3. 작성글 확인")
        print("4. 나가기")
