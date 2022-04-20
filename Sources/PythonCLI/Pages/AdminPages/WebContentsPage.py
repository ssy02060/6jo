from ..Page import Page
class WebContentsPage(Page):
    def printLogs(self):
        print("doraemong - [2022-04-21:03:16] - hello world")
        print("cream - [2022-04-21:03:16] - 집에 가자")
        print("water - [2022-04-21:03:16] - 재밌다~")
        
    def printManual(self):
        print("웹 컨텐츠 페이지입니다. (종료하려면 q / Q 를 입력하세요.")
        self.printLogs()