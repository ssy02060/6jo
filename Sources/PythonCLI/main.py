import Pages.login as login
import os
import Utills.DBUser as DBUser
import Utills.DBLog as DBLog
import Utills.DBWebContents as DBWebContents
def main():
    login.printManual()
    # DBUser.createUserTable()
    # DBUser.insertUser(0,'admin', 'admin', 'admin')
    # DBUser.insertUser(1,'seo', '0000', 'sy')
    # DBUser.insertUser(1,'han', '0000', 'sh')
    # DBUser.insertUser(1,'yoo', '0000', 'ds')
    # DBUser.insertUser(1,'oh', '0000', 'sh')
    # DBLog.createAgentLogTable()
    # DBWebContents.createWebContentsTable()

if __name__ == "__main__":
	main()