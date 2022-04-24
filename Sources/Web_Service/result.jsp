<%@page import="java.sql.DriverManager"%>
<%@page import="java.sql.Connection"%>
<%@page import="java.sql.*"%>
<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF8"%>
<!DOCTYPE html>
<html>
    <head>
        <meta charset="utf-8">
	<title></title>
    </head>
    <body>
	    <%= session.getAttribute("id") %>님이 등록한 내용입니다.<br/>
	    <h1> <%= session.getAttribute("contents") %></h1>
    </body>
</html>
