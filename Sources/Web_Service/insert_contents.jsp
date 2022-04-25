<!-- insertPro.jsp -->

<%@page import="java.sql.*"%>
<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>글쓰기 성공</title>
</head>
<body>

<%
    request.setCharacterEncoding("UTF-8");

	if(request.getMethod().equals("POST")){
		Connection conn = null;
        PreparedStatement pstmt = null; 
		String url = "jdbc:mysql://172.33.0.2:3306/cloud?";
		String id = "root";                     //MySQL에 접속을 위한 계정의 ID
		String pwd = "abcd";            //MySQL에 접속을 위한 계정의 암호
		Class.forName("com.mysql.cj.jdbc.Driver");
		try{
			conn = DriverManager.getConnection(url, id, pwd);
			String userId = (String) session.getAttribute("id");
			String contents = request.getParameter("contents");
			String query = "INSERT INTO web_contents(user_id, contents) VALUES(?, ?);";
            session.setAttribute("contents", contents);
            pstmt = conn.prepareStatement(query);
            pstmt.setString(1, userId);
            pstmt.setString(2, contents);
			pstmt.executeUpdate();
			pstmt.close();
			conn.close();
		}catch(Exception e){
			out.println(e);
		}	
	}
%>
<script>
alert("저장 성공!");
location.href = 'result.jsp';
</script>
</body>
</html>