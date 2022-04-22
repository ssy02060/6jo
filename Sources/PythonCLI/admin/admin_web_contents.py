import pymysql
import string

def Web_contents_List():
	conn = pymysql.connect(host='localhost', user='root', password='rootPassword', db='dbName', charset='utf8')
	cur = conn.cursor()
	query = "select * from webContentsDB"

	cur.execute(query)
	cur.commit()
	result = cur.fetchall()
	conn.close()

	print(result)

if __name__ == "__main__":
	Web_contents_List()