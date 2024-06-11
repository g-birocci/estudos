<!DOCTYPE html>
<html>
    <head>
        <meta charset="utf-8">
        <title>Gestão de Clientes</title>
    </head>
    <body>
    <h1>Listagem de clientes</h1>
    <br/>
    <?php
        // 1º ip do servidor; 2º nome do utilizador, 3º senha, 4º nome da bd
        $ligacao =mysqli_connect("localhost","id22302135_gbirocci","Brasil2021@","id22302135_bd01");
        // tento efetuar a ligação á base de dados
        if ($ligacao->connect_error){
            die(mysqli_error($ligacao));
        }
        $sql ="INSERT INTO t_cliente (nome, morada, zona, nif, vol_fatur) 
        values ('$_POST[name]','$_POST[morada]','$_POST[zona]','$_POST[nif]', $_POST[vol_fatur])";

        if (mysqli_query($ligacao, $sql))
            echo " <h3>Cliente inserido com sucesso</h3>";
        mysqli_close($ligacao); echo "<br>"
    ?>  <br/> 
        <h4>Aguarde ser redirecionado</h4>
        <a href="index.html" target="_self">Voltar ao menu</a>
    </body>
        
</html>