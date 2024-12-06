-- In this SQL file, write (and comment!) the typical SQL queries users will run on your database

--Coamando pra criar as tabelas no banco birocci_food

-- Comando para inserir os dados no banco de dados

--esta tabela insere os dados do cliente no banco (dados não verdadeiro)

INSERT INTO client (nome, telefone) VALUES 
('Ana Clara', '(11) 99999-1234'), --nome sempre Usar dentro de " " por ser uma string 
('Carlos Eduardo', '(21) 98888-5678'),
('Mariana Silva', '(31) 98765-4321'),
('João Pereira', '(41) 97654-3210'),
('Luiza Fernandes', '(51) 96543-2109');

--Esta tabela insere os dados do funcionarios

INSERT INTO staff (nome, cargo, telefone) VALUES 
('Roberto Lopes', 'Garçom', '(11) 91234-5678'),
('Fernanda Costa', 'Garçonete', '(21) 92345-6789'),
('Paulo Henrique', 'Cozinheiro', '(31) 93456-7890'),
('Clara Almeida', 'Chef', '(41) 94567-8901'),
('Juliana Moura', 'Auxiliar de Cozinha', '(51) 95678-9012');

--Esta tabela insere os pratos do menu

INSERT INTO dishes (nome, preco, categoria) VALUES 
('Spaghetti Carbonara', 32.90, 'Massas'),
('Filé à Parmegiana', 45.50, 'Carnes'),
('Salmão Grelhado', 52.00, 'Peixes'),
('Hambúrguer Artesanal', 28.90, 'Lanches'),
('Risoto de Camarão', 49.90, 'Massas'),
('Salada Caesar', 22.90, 'Saladas'),
('Pizza Margherita', 39.90, 'Pizzas'),
('Sopa de Legumes', 19.90, 'Entradas'),
('Tiramisu', 18.90, 'Sobremesas'),
('Brownie com Sorvete', 20.90, 'Sobremesas');

--Esta tabela mostra os pedidos, que neste caso os dados inseridos é uma sumulação que vai acontecer no dia a dia.

INSERT INTO orders (client_id, funcionario_id, data, total) VALUES 
(2, 1, '2024-12-01', 95.70),
(3, 2, '2024-12-02', 102.40),
(4, 3, '2024-12-03', 75.30),
(5, 4, '2024-12-04', 89.90),
(6, 5, '2024-12-05', 125.60);

--esta tabela junta os pedidos com o cliente

INSERT INTO Itens_orders (order_id, dish_id, quantidade, subtotal) VALUES 
(1, 1, 2, 65.80), -- Spaghetti Carbonara
(1, 6, 1, 22.90), -- Salada Caesar
(2, 2, 1, 45.50), -- Filé à Parmegiana
(2, 10, 2, 40.90), -- Brownie com Sorvete
(3, 3, 1, 52.00), -- Salmão Grelhado
(3, 8, 1, 19.90), -- Sopa de Legumes
(4, 4, 2, 57.80), -- Hambúrguer Artesanal
(4, 9, 1, 18.90), -- Tiramisu
(5, 5, 1, 49.90), -- Risoto de Camarão
(5, 7, 1, 39.90); -- Pizza Margherita

-- Este select vai listar todos os cliente que foi cadastrado na base de dados.

SELECT * FROM client 

-- Este select vai ser usado pra encontrar um cliente atravez do seu nome.

SELECT FROM client WHERE = "gabriel" 

--este select mostra os historicos de update

SELECT * FROM historico_precos;

--Este select mostra quem mais atendeu cliente. 

SELECT 
    s.nome AS funcionario,
    COUNT(o.id) AS total_atendimentos
FROM orders o
JOIN staff s ON o.funcionario_id = s.id --Faz a junção entre a tabela orders e staff para identificar o funcionário que atendeu.
GROUP BY s.nome
ORDER BY total_atendimentos DESC

--Este select é usado pra pesquisar por data. 

SELECT 
    d.nome AS prato,
    SUM(io.quantidade) AS total_vendido
FROM Itens_orders io
JOIN dishes d ON io.dish_id = d.id
JOIN orders o ON io.order_id = o.id
WHERE strftime('%Y-%m', o.data) = '2024-12'-- Substitua pelo mês/ano desejado --WHERE strftime('%Y', o.data) = '2024' -- Substitua pelo ano.
GROUP BY d.nome                             --strftime('%Y-%m', o.data).ele extrai o ano e o mês da data do pedido no formato YYYY-MM.
ORDER BY total_vendido DESC
LIMIT 1;

--Este select é usado pra pesquisar os produto mais vendidos no geral.

SELECT d.nome, SUM(io.quantidade) AS total_vendido
FROM Itens_orders io
JOIN dishes d ON io.dish_id = d.id
GROUP BY d.nome
ORDER BY total_vendido DESC
LIMIT 1; --Se tirar está linha ele vai listar todos os produtos por orden decrescente.

--Este select é usado pra pesquisar os produto mais vendidos por categoria

SELECT * FROM view_vendas_categoria;

--Este select é usado pra pesquisar os produto mais vendidos por categoria específica.

SELECT *
FROM view_vendas_categoria
WHERE categoria = 'Massas' --basta trocar o nome da categoria. (massas,pizzas, carne ...).
LIMIT 1;

--Este select é usado pra pesquisar os produto mais vendidos por categoria específica em ordem.

SELECT *
FROM view_vendas_categoria
WHERE categoria = 'Carnes' --basta trocar o nome da categoria. (massas,pizzas, carne ...).
ORDER BY total_vendido DESC;
