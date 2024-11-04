-- add os cliente na tabela

INSERT INTO Cliente (nome, email, telefone) VALUES ('Maria Silva', 'maria@example.com', '1234-5678');
INSERT INTO Cliente (nome, email, telefone) VALUES ('João Souza', 'joao@example.com', '9876-5432');
INSERT INTO Cliente (nome, email, telefone) VALUES ('Ana Oliveira', 'ana@example.com', '5555-6666');

-- add os modelos de acessórios que ira encontrar no banco
/*
INSERT INTO Modelo_aparelho (nome_modelo, marca) VALUES ('iPhone 11', 'Apple');
INSERT INTO Modelo_aparelho (nome_modelo, marca) VALUES ('iPhone 12', 'Apple');
INSERT INTO Modelo_aparelho (nome_modelo, marca) VALUES ('iPhone 13', 'Apple');
INSERT INTO Modelo_aparelho (nome_modelo, marca) VALUES ('Galaxy S20', 'Samsung');
INSERT INTO Modelo_aparelho (nome_modelo, marca) VALUES ('Galaxy S21', 'Samsung');
INSERT INTO Modelo_aparelho (nome_modelo, marca) VALUES ('Galaxy A52', 'Samsung');

-- add os produtos na base

INSERT INTO Produto (nome, tipo_produto, preco, estoque) VALUES ('Capa de Silicone', 'Acessório', 29.90, 100);
INSERT INTO Produto (nome, tipo_produto, preco, estoque) VALUES ('Película de Vidro', 'Acessório', 39.90, 50);
INSERT INTO Produto (nome, tipo_produto, preco, estoque) VALUES ('Carregador Rápido', 'Carregador', 89.90, 30);
INSERT INTO Produto (nome, tipo_produto, preco, estoque) VALUES ('Fones de Ouvido Bluetooth', 'Acessório', 199.90, 25);
INSERT INTO Produto (nome, tipo_produto, preco, estoque) VALUES ('Power Bank', 'Carregador', 149.90, 15);

-- add as expecificação do produto (facilitar a leitura com menos colunas)

INSERT INTO Especificacao_Produto (produto_id, material, potencia) VALUES (1, 'Silicone', 'N/A');
INSERT INTO Especificacao_Produto (produto_id, material, potencia) VALUES (2, 'Vidro Temperado', 'N/A');
INSERT INTO Especificacao_Produto (produto_id, material, potencia) VALUES (3, 'Plástico', '18W');
INSERT INTO Especificacao_Produto (produto_id, material, potencia) VALUES (4, 'Plástico', 'N/A');
INSERT INTO Especificacao_Produto (produto_id, material, potencia) VALUES (5, 'Alumínio', 'N/A');

-- add os dados de venda para poder fazes as pesquisas

INSERT INTO Venda (data_venda, cliente_id) VALUES ('2024-10-01', 1);
INSERT INTO Venda (data_venda, cliente_id) VALUES ('2024-10-02', 2);
INSERT INTO Venda (data_venda, cliente_id) VALUES ('2024-10-03', 3);

-- add os itens da venda

INSERT INTO Item_venda (venda_id, produto_id, quantidade, preco_unitario) VALUES (1, 1, 2, 29.90);
INSERT INTO Item_venda (venda_id, produto_id, quantidade, preco_unitario) VALUES (1, 3, 1, 89.90);
INSERT INTO Item_venda (venda_id, produto_id, quantidade, preco_unitario) VALUES (2, 2, 1, 39.90);
INSERT INTO Item_venda (venda_id, produto_id, quantidade, preco_unitario) VALUES (2, 4, 1, 199.90);
INSERT INTO Item_venda (venda_id, produto_id, quantidade, preco_unitario) VALUES (3, 5, 1, 149.90);
*/