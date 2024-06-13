<!DOCTYPE html>
<html>
    <head>
        <meta charset="utf-8">
        <title>Gestão de Clientes</title>
    </head>
    <body>
    <h1>Eliminação de clientes</h1>
    <br/>
    <?php
        // 1º ip do servidor; 2º nome do utilizador, 3º senha, 4º nome da bd
        $ligacao =mysqli_connect("localhost","id22302135_gbirocci","Brasil2021@","id22302135_bd01");
        // tento efetuar a ligação á base de dados
        if ($ligacao->connect_error){
            die(mysqli_error($ligacao));
        }
        $sql="DELETE FROM t_cliente WHERE id=". $_POST['cliente'];
        if (mysqli_query($ligacao, $sql))
            echo "<h3>Cliente eliminado com sucesso!";
        mysqli_close ($ligacao); 
        echo"<br/>";
    ?>
    <a href="index.html">Voltar</a>
    </body>    
</html>