<%@page import="java.sql.DriverManager"%>
<%@page import="java.sql.Connection"%>
<%@ page import="java.sql.Statement"%>
<%@ page import="java.sql.PreparedStatement" %>
<%@ page import="java.sql.ResultSet"%>
<%@ page import="java.sql.SQLException"%>
<%@ page import="java.security.MessageDigest;"%>

<% request.setCharacterEncoding("utf-8"); %>
<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF8"%>
<!DOCTYPE html>
<html>
	<head>
		<meta charset="utf-8">
		<title> www.example.com </title>
	</head>
	<body>

        <form method="post" action="<%=request.getContextPath()%>/login_test.jsp">

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
		// out.println("<h1>MySQL DB 연결 성공</h1>");
        
        // 변수 초기화
        PreparedStatement pstmt = null; 
        Statement stmt = null;
        ResultSet rs = null;
       
        // 페이지에서 파라미터 값 가져오기
        String page_id = request.getParameter("id");
        String page_pw = request.getParameter("pw");

        // SQL 문
        String sql = "select * from user where id = ?;";
        pstmt = conn.prepareStatement(sql);
        pstmt.setString(1, page_id);
        
        rs = pstmt.executeQuery();
        

        while (rs.next()) {
            // id 확인 (미완성)
            <!-- String isNull = rs.getString("id");
            if (rs.wasNull()){
            %>
            <script>
                alert("아이디 없다")
                location.href="/login_test.jsp";
            </script>
        <%
        } -->
            // passwd 확인 (-MD5 된 암호를 사용해야함)
            if(page_pw.equals(rs.getString("passwd"))) {
               session.setAttribute("page_id", rs.getString("id"));
               response.sendRedirect(request.getContextPath() + "/test_ok.jsp");
           }else{
        %>
            <script>
                alert("비밀번호가 틀립니다!")
                location.href="/login_test.jsp";
            </script>
        <%
           }
       
        }
        


        rs.close();
        pstmt.close();
        conn.close();
        %>

    


	</body>
</html>