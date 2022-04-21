<%@page import="java.sql.DriverManager"%>
<%@page import="java.sql.Connection"%>
<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF8"%>
<!DOCTYPE html>
<html>
	<head>
		<meta charset="utf-8">
		<title> Main Page </title>
	</head>
	<body>
		<%
		Connection conn = null;
		String url = "jdbc:mysql://172.33.0.2:3306/cloud";
		String id = "root";                     //MySQL에 접속을 위한 계정의 ID
		String pwd = "abcd";            //MySQL에 접속을 위한 계정의 암호
		Class.forName("com.mysql.cj.jdbc.Driver");
		conn = DriverManager.getConnection(url, id, pwd);
		out.println("<h1>MySQL DB 연결 성공</h1>");
		%>
		<form method="post" action="/result.jsp">
			내용을 작성하고 버튼을 클릭해주세요. <br/>
			<textarea name="contents" rows = "7" cols = "40"
			wrap = "virtual"></textarea>
			<input name="btnSubmit" type="submit" value="제출">
		</form>

	</body>
</html>
