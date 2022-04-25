<%@page import="java.sql.DriverManager"%>
<%@page import="java.sql.Connection"%>
<%@page import="java.sql.*"%>
<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF8"%>
<!DOCTYPE html>
<html>
	<head>
		<meta charset="utf-8">
		<title> login페이지 입니다. </title>
	</head>
	<body>

		<form method="post" action="/login.jsp">
			로그인 화면입니다. <br/>
			ID:  <input type="text" name="id"><br/>
			PW: <input type="password" name="pw"><br/>
			
			<input name="submit" type="submit" value="Login"><br/>
		</form>
		<%
		Connection conn = null;
		String url = "jdbc:mysql://172.33.0.2:3306/cloud";
		String id = "root";                     //MySQL에 접속을 위한 계정의 ID
		String pwd = "abcd";            //MySQL에 접속을 위한 계정의 암호
		Class.forName("com.mysql.cj.jdbc.Driver");
		conn = DriverManager.getConnection(url, id, pwd);
		out.println("<h1>MySQL DB 연결 성공</h1>");
		%>
	</body>
</html>