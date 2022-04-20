from ..Page import Page
class UserManagePage(Page):
    def printManual(self):
        print("사용자 관리 페이지입니다.  (1 ~ 4 사이 번호를 입력하세요)")
        print("사용자 생성")
        print("사용자 목록 보기")
        print("사용자 정보 수정")
        print("사용자 정보 삭제")
    def inputMenu(self):
        return super().inputMenu()