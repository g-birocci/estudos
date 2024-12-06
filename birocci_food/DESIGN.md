# Design Document

By YOUR NAME HERE: Gabriel Birocci Freire

Video overview: <URL HERE>

## Scope

In this section you should answer the following questions:

* What is the purpose of your database?
    O objetivo deste banco é armazernar todas infomação de vendas de um restaurante.
* Which people, places, things, etc. are you including in the scope of your database?
    O banco contem informação dos cliente e dos funcionarios que fazem parte da equipe contratada.
* Which people, places, things, etc. are *outside* the scope of your database?
    A pessoas que estão fora deste banco são os free lance que podem trabalhar em dias mais corrido do restaurante.

## Functional Requirements

In this section you should answer the following questions:

* What should a user be able to do with your database?
    O utilizador vai ser capaz de saber quais pratos são mais vendidos, e quais funcionarios estão atendendo mais cliente.
* What's beyond the scope of what a user should be able to do with your database?
    Ele pode vereficar atravez das datas quais meses teve mais vendas. e assim ter uma base se precisa ter mais funcionarios naquele determinado tempo e também ter um stock mais de ingredientes.

## Representation

### Entities

In this section you should answer the following questions:

### client

A tabela client representa a frequancia dos cliente no restaurante.

* ´id´, O ID foi declarado como INTEGER, e dalcarado como uma chave primaria(identificador unico)
* ´nome´ O nome foi declado como text, para armazenar o nome do cliente, e optei por usar NOT NULL pra não ter o nome como uma campo vazio.
* ´telefone´ O telefone foi declarado como TEXT e o motivo desta escolha é pra ter uma flexibilidade de armazernar numeros quando ter caracterer especial como por exe: (+351 999-000888)

### staff

A tabela staff representa os empregados do restaurante.

* ´id´, O ID foi declarado como INTEGER, pra identificador unico.
* ´nome´ O nome foi declado como text, para armazenar o nome do cliente, e optei por usar NOT NULL pra não ter o nome como uma campo vazio.
* ´cargo´ o cargo foi declarado como TEXT, para receber a função de cada colaborador, e NOT NULL para que cada função fique em branco, e pra discrimirar a liderança.
* ´telefone´ O telefone foi declarado como TEXT e o motivo desta escolha é pra ter uma flexibilidade de armazernar numeros quando ter caracterer especial como por exe: (+351 999-000888)

### orders

A tabela orders representa os pedidos realizado no restaurante.

* ´id´, O ID foi declarado como INTEGER, pra identificador unico de cada pedido.
* ´client_id´, está cheve estrageira tem como referencia a tabela client.
* ´funcionario_id´, está chave estrageira que tem como referencia a tabela staff.
* ´data´, este campo foi definido como DATE, este campo contem as datas dos pedidos.
* ´total´, este campo mostra o total dos pedidos (em valor).

### dishes

a tabela dishes representa todos os pratos que tem no menu do restaurante.

* ´id´, O ID foi declarado como INTEGER, pra identificador unico de cada prato.
* ´order_id´, está chave estrageira tem como referencia a tabela orders.
* ´dish_id´, está chave estrageira tem como relação a tabela dishes.
* ´quantidade´, este campo foi definido como INTEGER, e com atributo NOT NULL, por que neste campo que vai ter a quantidade de pratos vendidos.
* ´subtotal´, este campo foi declarado como REAL e NOT NULL, o objetico é mostrar o valor de quanto o cliente gastou (quantidade * preço unitário).
* 

### Relationships

In this section you should include your entity relationship diagram and describe the relationships between the entities in your database.

* birocci_food

Este banco contem 5 tabelas então resumindo pra simplificar, a primeira client, um cliente pode fazer muito pedidos (client » orders).
A segunda tabela staff, um funcionario pode ser associado a muito pedidos. (staff » orders).
A tabela de pedido pode ter muito pratos, e um prato pode estar em varios pedidos em como essa relação de muitos para muitos nasce a tabela itens_orders. (orders «» itens_orders «» dishes)

                Cliente (1) --- (N) Pedido (1) --- (N) Itens_Pedido (N) --- (1) Prato
                                      |
                                      |
                                Funcionário (1)

## Optimizations

In this section you should answer the following questions:

* Which optimizations (e.g., indexes, views) did you create? Why?

As otimizações feitas foi dois index, um view e um triger, a ideia disto é deixa mais rapido as pesquisas mais frequentes, essss pesquisa um crie um index idx_dishes_categoria, pra melhorar a velocidade de pesquisa, caso eu queira lista todos os pratos de uma determinada categoria, o outro index foi idx_itens_orders_dish_id que faz a busca melhoras o desempenho na busca de resgistro, se eu consultar quais pedidos incluie uma prato específico.
A view criada foi a para mostras "geral" do dia pra mostras as vendas todas organizadas por categoria e prato.
O triger foi criado pra ficar registrado as alteração nos preços do menu.

## Limitations

In this section you should answer the following questions:

* What are the limitations of your design?

Neste projeto foi desenvolvido no sqlite3, no caso do projeto ter uma grande escala o ideal seria migrar pra sistema de base de dados mais robustas como MySQL ou PostgreSQL.
Este sistema não tem um gerenciamento de estoque.

* What might your database not be able to represent very well?

No caso de eventos como black friday, náo é possivel adiconar descontos no pratos idividual ou por categorias.