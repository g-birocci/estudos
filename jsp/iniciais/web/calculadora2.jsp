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
if (request.getParameter("n1") != null && request.getParameter("n2") != null && request.getParameter("op") != null) {
                // Obtém os números e a operação
                double n1 = Double.parseDouble(request.getParameter("n1"));
                double n2 = Double.parseDouble(request.getParameter("n2"));
                String op = request.getParameter("op");

                double resultado = 0;
                String operacao = "";

                // Determina a operação com if/else
                if (op.equals("som")) {
                    resultado = n1 + n2;
                    operacao = "soma";
                } else if (op.equals("dif")) {
                    resultado = n1 - n2;
                    operacao = "subtração";
                } else if (op.equals("div")) {
                    if (n2 != 0) {
                        resultado = n1 / n2;
                        operacao = "divisão";
                    } else {
                        operacao = "erroDivisao";
                    }
                } else if (op.equals("mul")) {
                    resultado = n1 * n2;
                    operacao = "multiplicação";
                } else {
                    operacao = "erroOperacao";
                }

                // Exibe o resultado
                if (operacao.equals("erroDivisao")) {
                    out.print("<h3>Erro: Divisão por zero não é permitida.</h3>");
                } else if (operacao.equals("erroOperacao")) {
                    out.print("<h3>Erro: Operação inválida.</h3>");
                } else {
                    out.print("<h3>O resultado da " + operacao + " de " + n1 + " e " + n2 + " é: " + resultado + "</h3>");
                }
            } else {
                out.print("<h3>Erro: Todos os campos devem ser preenchidos.</h3>");
            }
        %>
        <br>
        <a href="calculadora2.html">Voltar à Calculadora</a>
    </body>
</html>