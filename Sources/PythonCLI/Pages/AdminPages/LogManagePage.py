from ..Page import Page
class LogManagePage(Page):
    def printLogs(self):
        print("[0.0.0.0] - [2022-04-21:03:16] - http ~~~")
        print("[0.0.0.0] - [2022-04-21:03:16] - http ~~~")
        print("[0.0.0.0] - [2022-04-21:03:16] - http ~~~")
        print("[0.0.0.0] - [2022-04-21:03:16] - http ~~~")

    def printManual(self):
        print("로그 확인 페이지입니다. (종료하려면 q / Q 를 입력하세요.")
        self.printLogs()