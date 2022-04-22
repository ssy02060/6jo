<%@ page contentType="text/html; charset=UTF-8" pageEncoding="UTF-8"%>
<!DOCTYPE html>
<html>
	<head>
		<meta charset="utf-8">
		<title> www.example.com </title>
	</head>
	<body>
		<form method="post" action="/result.jsp">
			<%= request.getParameter("id") %>님, 환영합니다.<br/>
			내용 <br/>
			<textarea name="contents" rows="7" cols="40" wrap="virtual"></textarea>
			<input name="btn" type="submit" value="등록">
		</form>
	</body>
</html>

