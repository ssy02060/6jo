<%@ page contentType="text/html; charset=UTF-8" pageEncoding="UTF-8"%>
<!DOCTYPE html>
<html>
    <head>
        <meta charset="utf-8">
	<title> www.example.com </title>
    </head>
    <body>
	    등록된 내용입니다.<br/>
	    <h1> <%= request.getParameter("contents") %></h1>
    </body>
</html>
