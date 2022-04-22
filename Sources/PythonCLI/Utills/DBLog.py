from json.tool import main
import pymysql


def logFileSlice(log: list) -> list:
    return_list = []
    # ip 출력
    end_ip_idx = log.find(' ', 0)
    return_list.append(log[:end_ip_idx])

    # $request_body 출력
    start_req_idx = log.find('[', end_ip_idx)
    end_req_idx = log.find(']', start_req_idx + 1)
    return_list.append(log[start_req_idx:end_req_idx + 1])
    # print(log[start_req_idx:end_req_idx + 1])

    # 시간 출력
    start_time_idx = log.find('[', end_req_idx)
    end_time_idx = log.find(']', start_time_idx)
    return_list.append(log[start_time_idx:end_time_idx + 1])
    return_list.append(log[start_time_idx:end_time_idx + 1])
    # print(log[start_time_idx:end_time_idx + 1])

    # 메서드 출력 (GET, POST)
    method = ''
    if log.find('POST'):
        method = 'POST'
    elif log.find('GET'):
        method = 'GET'
    else:
        method = 'ETC'
    return_list.append(method)
    # print(method)

    # URL 찾기
    start_URL_idx = log.find(method[-1], start_req_idx) + 2
    end_URL_idx = log.find('1.1', start_URL_idx) + 3
    return_list.append(log[start_URL_idx:end_URL_idx])
    # print(log[start_URL_idx:end_URL_idx])

    # code 찾기
    start_code_idx = end_URL_idx + 2
    end_code_idx = start_code_idx + 3
    html_code = log[start_code_idx:end_code_idx]
    body_bytes = log[end_code_idx + 1:log.find('"', end_code_idx)]
    return_list.append(html_code)
    # print(html_code, body_bytes)

    # 그 외
    start_etc_idx = log.find('"', end_code_idx)
    return_list.append(log[start_etc_idx:-1])
    # print(log[start_etc_idx:-1])

    return return_list


def autoSaveLog() -> int:
    # main 함수에서 total_cnt와 return 값 확인하기
    conn = pymysql.connect(host='172.33.0.2', user='root', password='abcd', db='cloud', charset='utf8')
    cursor = conn.cursor()

    line_cnt = 0
    _file = open("/home/yoo/test_log", 'r')
    _list = _file.readlines()

    for log in _list:
        if _list != '\n':
            line_cnt += 1
    log_file = logFileSlice(log)

    sql = 'INSERT INTO user (id, ipAddr, time, method, url, code, etc)' \
          'VALUES (%s, %s, %s, %s, %s, %s)'
    cursor.execute(sql,
                   (log_file[0], log_file[1], log_file[2],
                    log_file[3], log_file[4], log_file[5]))
    conn.commit()
    conn.close()

    return line_cnt


def createAgentLogTable():
    conn = pymysql.connect(host='172.33.0.2', user='root', password='abcd', db='cloud', charset='utf8')
    cursor = conn.cursor()
    sql = ''' 
         CREATE TABLE agentlog ( 
            id varchar(32),
            ipAddr VARCHAR(32),
            time varchar(255),
            method varchar(32),
            url varchar(255),
            code int(20),
            details varchar(255),
            FOREIGN KEY (id) REFERENCES user (id)
            )
            '''

    cursor.execute(sql)
    print("created AgnetLog table successfully")
    conn.commit()
    conn.close()


def insertUser(id, ipAddr, time, method, url, code, details):
    conn = pymysql.connect(host='172.33.0.2', user='root', password='abcd', db='cloud', charset='utf8')
    cursor = conn.cursor()
    sql = 'INSERT INTO agentlog (id, ipAddr, time, method, url, code, details) VALUES (%s, %s, %s, %s, %s, %s, %s)'
    cursor.execute(sql, (id, ipAddr, time, method, url, code, details))
    conn.commit()
    conn.close()


'''def searchUserLog(id, pw, name, auth):
    conn = pymysql.connect(host='172.33.0.2', user='root', password='abcd', db='cloud', charset='utf8')
    cursor = conn.cursor()
    sql = 'INSERT INTO user (account, passwd, name, auth) VALUES (%s, %s, %s, %s)'
    cursor.execute(sql, (id, pw, name, auth))
    conn.commit()
    conn.close()


def selectAllUser():
    conn = pymysql.connect(host='172.33.0.2', user='root', password='abcd', db='cloud', charset='utf8')
    cursor = conn.cursor()
    sql = "SELECT * FROM user"
    cursor.execute(sql)
    res = cursor.fetchall()
    users = res
    print(users[0][3])
    for user in users:
        print(user)
    conn.commit()
    conn.close()

# createUserTable()
# insertUser("han","0000","seunghun","1")
# insertUser("ddd","0000","seunghun","1")
# insertUser("hbban","0000","seunghun","1")
# insertUser("yyy","0000","seunghun","1")
selectAllUser()
'''
# createAgentLogTable()
insertUser('ddd', '1.2.2.2', '1', 'GET', '1', 200, '1')
