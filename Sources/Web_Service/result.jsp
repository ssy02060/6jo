<%@ page contentType="text/html; charset=UTF-8" pageEncoding="UTF-8"%>
<!DOCTYPE html>
<html>
    <head>
        <meta charset="utf-8">
    </head>
    <body>
        <h1>작성한 내용</h1>
        <ul>
            <li>Contents: <%= request.getParameter("contents") %></li>
        </ul>
    </body>
</html>
