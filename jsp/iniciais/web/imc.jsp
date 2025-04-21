<%@page contentType="text/html" pageEncoding="UTF-8"%>
<!DOCTYPE html>
<html>
    <head>
        <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
        <title>Calculadora do IMC</title>
    </head>
    <body>
        <%
        if (request.getParameter("peso") != null && request.getParameter("altura") != null && request.getParameter("op") != null) {
            try {
                float peso = Float.parseFloat(request.getParameter("peso"));
                float altura = Float.parseFloat(request.getParameter("altura"));
                String op = request.getParameter("op");

                if (peso > 0 && altura > 0) {
                    float imc = peso / (altura * altura);

                    String categoria = "";
                    if (op.equals("m")) { // Homem
                        if (imc < 20) {
                            categoria = "Abaixo do peso";
                        } else if (imc >= 20 && imc < 25) {
                            categoria = "Peso normal";
                        } else if (imc >= 25 && imc < 30) {
                            categoria = "Acima do peso";
                        } else {
                            categoria = "Obesidade";
                        }
                    } else if (op.equals("f")) { // Mulher
                        if (imc < 19) {
                            categoria = "Abaixo do peso";
                        } else if (imc >= 19 && imc < 24) {
                            categoria = "Peso normal";
                        } else if (imc >= 24 && imc < 29) {
                            categoria = "Acima do peso";
                        } else {
                            categoria = "Obesidade";
                        }
                    } else {
                        out.print("<p style='color:red;'>Erro: Opção inválida. Escolha 'm' para homem ou 'f' para mulher.</p>");
                    }

                    if (!categoria.isEmpty()) {
                        out.print(String.format("<p>Seu IMC é: %.2f</p>", imc));
                        out.print(String.format("<p>Categoria: %s</p>", categoria));
                    }
                } else {
                    out.print("<p style='color:red;'>Por favor, insira valores positivos para peso e altura.</p>");
                }
            } catch (NumberFormatException e) {
                out.print("<p style='color:red;'>Erro: Insira números válidos para peso e altura.</p>");
            }
        } else {
            out.print("<p style='color:red;'>Por favor, preencha todos os campos.</p>");
        }
        %>
        <br>
        <a href="imc.html">Voltar</a>
    </body>
</html>
