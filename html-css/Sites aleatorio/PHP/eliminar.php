<!DOCTYPE html>
<html>
    <head>
        <meta charset="utf-8">
        <title>Gestão de Clientes</title>
    </head>
    <body>
    <h1>Eliminação de clientes</h1>
    <br/>
        <form action="eliminar2.php" method="post">
            <label for="cliente">Cliente:</label>
            <select name="cliente" id="nome">
    <?php
        // 1º ip do servidor; 2º nome do utilizador, 3º senha, 4º nome da bd
        $ligacao =mysqli_connect("localhost","id22302135_gbirocci","Brasil2021@","id22302135_bd01");
        // tento efetuar a ligação á base de dados
        if ($ligacao->connect_error){
            die(mysqli_error($ligacao));
        }
        $sql="SELECT * FROM t_cliente order by nome";
        $resultado=mysqli_query($ligacao, $sql) or die (mysqli_error($ligacao));

        while ($linha = mysli_fetch_assoc($resultado))
            {
                echo"<option value'" . $linha['id'] "'>" . $linha['nome'];
                echo "</option>";
            }

        mysqli_close ($ligacao);
    ?> 
        <input type="submit" value="Eliminar">
    </select>
        </form>
         <br/> 
        <input type="button" onclick="windons.history.go(-1);" value="Voltar">
    </body>
        
</html>