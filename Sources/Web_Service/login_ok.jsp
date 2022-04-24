<%@page import="java.sql.DriverManager"%>
<%@page import="java.sql.Connection"%>
<%@page import="java.sql.*"%>
<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF8"%>

<!DOCTYPE html>
<html>
	<head>
		<meta charset="utf-8">
		<title>로그인 성공</title>
	</head>
	<body>
		<form method="post" action="/insert_contents.jsp">
			<%= request.getParameter("id") %>님, 환영합니다.<br/>
			<%
				session.setAttribute("id", request.getParameter("id"));
			%>
			
			내용 <br/>
			<textarea name="contents" rows="7" cols="40" wrap="virtual"></textarea>
			<input name="btn" type="submit" value="등록">
		</form>
	</body>
</html>

