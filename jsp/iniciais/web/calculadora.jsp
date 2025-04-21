<%-- 
    Document   : calculadora
    Created on : Apr 21, 2025, 2:37:44 PM
    Author     : gabri
--%>

<%@page contentType="text/html" pageEncoding="UTF-8"%>
<!DOCTYPE html>
<html>
    <head>
        <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
        <title>Calculadora</title>
    </head>
    <body>
        <%
            int n1 = Integer.parseInt(request.getParameter("n1"));
            int n2 = Integer.parseInt(request.getParameter("n2"));
            int resultado = n1+n2;
            out.print("<h1>Calculadora<h1>");
            out.print("<h3>A soma de " + n1 + "com" + n2 + " = " + resultado +"<h3>");
 
        %>
    </body>
</html>
