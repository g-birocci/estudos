<%-- 
    Document   : listar
    Created on : Apr 21, 2025, 5:56:30 PM
    Author     : gabri
--%>

<%@page language="java" contentType="text/html" pageEncoding="UTF-8"%>
<%@page import="java.sql.*" %>
<!DOCTYPE html>
<html>
    <head>
        <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
        <title>Listagem de Clientes</title>
    </head>
    <body>
        <h1>Listagens dos Dados</h1>
        
        <table border="1">
            <tr>
                <th>ID</th>
                <th>Nome</th>
                <th>Morada</th>
                <th>Zona</th>
                <th>NIF</th><!--  -->
                <th>Volume de Faturação</th>
            </tr>
    <% 
        int num = 0;
        float media = 0;
        
        try {
            Class.forName("com.mysql.jdbc.Driver");
            
            Connection conn = DriverManager.getConnection("jdbc:mysql://localhost:3306/db_clientes","root","");
            Statement stmt = conn.createStatement();
            
            ResultSet rs = stmt.executeQuery("SELECT * FROM t_cliente");
        
                while (rs.next()) {
                %>
                <tr>
                    <td><%= rs.getInt("id") %></td>
                    <td><%= rs.getString("nome") %></td>
                    <td><%= rs.getString("morada") %></td>
                    <td><%= rs.getString("zona") %></td>
                    <td><%= rs.getString("NIF") %></td>
                    <td><%= rs.getFloat("vol_fatur") %></td>
                    <% num ++;
                    media = media + rs.getFloat("vol_fatur"); %>    
                </tr>
                <%   
        }
        %>
        <tr><th colspan="5">Numero de Registro na DB</th>
            <th><%= num %></th></tr>
        <tr><th colspan="5">Média de Faturação</th>
            <th><%= media / num %></th></tr>
        <% 
            rs.close();
            stmt.close();
            conn.close();
        } catch (Exception e) {
            out.print("An error occurred" + e.getMessage());
}
        %>
        </body>
</html>