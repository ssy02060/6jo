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
	</body>
</html>