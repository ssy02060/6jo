from json.tool import main
import pymysql


def logFileSlice(log: list, prev_id, prev_ip) -> list:
    # (0 : ip, 1: requset_body, 2: 시간, 3: 메서드, 4: URI, 5: html_code, 6: etc)
    
    return_list = []
    #1 ip 출력
    end_ip_idx = log.find(' ', 0)
    current_ip = log[:end_ip_idx]
    return_list.append(current_ip)


    # $request_body 출력
    start_req_idx = log.find('[', end_ip_idx)
    end_req_idx = log.find(']', start_req_idx + 1)
    return_list.append(log[start_req_idx:end_req_idx + 1])
    # print(log[start_req_idx:end_req_idx + 1])

    # id 값 가져가기

    if 'id' in return_list[1]:
        current_id = log[log.find('id=') + 3:log.find('&')]
        if prev_ip == current_ip:
            id = current_id
        else:
            id = prev_id
    else:
        if prev_ip != current_ip:
            id = None
        else:
            id = prev_id

    return_list.insert(0, id)


    # 시간 출력
    start_time_idx = log.find('[', end_req_idx)
    end_time_idx = log.find(']', start_time_idx)
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

    #그 외(details)
    start_etc_idx = log.find('"', end_code_idx)
    return_list.append(log[start_etc_idx:-1])
    # print(log[start_etc_idx:-1])


    # ip, id 정보 갱신
    prev_ip = current_ip
    prev_id = id
    return return_list, prev_id, prev_ip


def autoSaveLog(line_cnt :int) -> None:
    # main 함수에서 total_cnt와 return 값 확인하기
    conn = pymysql.connect(host='172.33.0.2', user='root', password='abcd', db='cloud', charset='utf8')
    cursor = conn.cursor()

    prev_id, prev_ip = None, None
    _file = open("/app/cli/logs/access.log", 'r')
    _list = _file.readlines()[line_cnt:]

    for log in _list:
        # if _list != '\n':
        #     line_cnt += 1
        ret_val = logFileSlice(log, prev_id, prev_ip)
        log_file = ret_val[0]
        prev_id, prev_ip = ret_val[1], ret_val[2]
        sql = '''
                INSERT INTO agentlog (id, ipAddr, time,
                                    method, url, code, details)
                VALUES (%s, %s, %s, %s, %s, %s, %s)
            '''
        cursor.execute(sql,
                    (log_file[0], log_file[1], log_file[3],
                        log_file[4], log_file[5], log_file[6], log_file[7]))
        conn.commit()
    conn.close()
    _file.close()
   
    print(line_cnt)
    # return line_cnt


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


def insertLogForTest(id, ipAddr, time, method, url, code, details):
    conn = pymysql.connect(host='172.33.0.2', user='root', password='abcd', db='cloud', charset='utf8')
    cursor = conn.cursor()
    sql = 'INSERT INTO agentlog (id, ipAddr, time, method, url, code, details) VALUES (%s, %s, %s, %s, %s, %s, %s)'
    cursor.execute(sql, (id, ipAddr, time, method, url, code, details))
    conn.commit()
    conn.close()


def deleteAllLog():
    conn = pymysql.connect(host='172.33.0.2', user='root', password='abcd', db='cloud', charset='utf8')
    cursor = conn.cursor()
    sql = '''
        truncate agentlog;  
    '''
    cursor.execute(sql)
    conn.commit()
    conn.close()


def selectLog(id):
    id = id
    conn = pymysql.connect(host='172.33.0.2', user='root', password='abcd', db='cloud', charset='utf8')
    cursor = conn.cursor()
    sql = 'SELECT * FROM agentlog where id=%s'
    cursor.execute(sql, id)
    res = cursor.fetchall()
    log = list(res)
    conn.commit()
    conn.close()
    return log


def selectAllLog():
    conn = pymysql.connect(host='172.33.0.2', user='root', password='abcd', db='cloud', charset='utf8')
    cursor = conn.cursor()
    sql = 'SELECT * FROM agentlog'
    cursor.execute(sql)
    res = cursor.fetchall()
    log = list(res)
    conn.commit()
    conn.close()
    return log
# createAgentLogTable()
# deleteTable()
# autoSaveLog()
# insertUser('han', '1.2.2.2', '1', 'GET', '1', 200, '1')
