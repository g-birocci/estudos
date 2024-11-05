-- add os cliente na tabela

INSERT INTO Cliente (nome, email, telefone) VALUES 
('Ana Souza', 'ana.souza@email.com', '11987654321'),
('Carlos Lima', 'carlos.lima@email.com', '21987654322'),
('Beatriz Santos', 'beatriz.santos@email.com', '31987654323'),
('João Pereira', 'joao.pereira@email.com', '41987654324'),
('Mariana Oliveira', 'mariana.oliveira@email.com', '51987654325');


INSERT INTO Produto (produto_id, nome, tipo_produto, preco, estoque) VALUES 
(1, 'Capa Protetora', 'Acessório', 29.99, 50),
(2, 'Película de Vidro', 'Acessório', 19.99, 100),
(3, 'Carregador Rápido', 'Carregador', 39.99, 30),
(4, 'Fone de Ouvido Bluetooth', 'Acessório', 89.99, 20),
(5, 'Bateria Externa', 'Acessório', 99.99, 15);


INSERT INTO Especificacao_Produto (produto_id, material, potencia) VALUES 
(1, 'Silicone', 'N/A'),
(2, 'Vidro Temperado', 'N/A'),
(3, '5V/2A', 'Rápido'),
(4, 'Plástico ABS', 'Bluetooth'),
(5, 'Polímero', '10000mAh');


INSERT INTO Produto_Modelo (produto_modelo_id, produto_id, modelo_id, compatibilidade) VALUES 
(1, 1, 1, 'Compatível com iPhone 12'),
(2, 2, 1, 'Compatível com Samsung Galaxy S21'),
(3, 3, 2, 'Compatível com a maioria dos dispositivos USB-C'),
(4, 4, 3, 'Compatível com dispositivos Bluetooth'),
(5, 5, 4, 'Compatível com smartphones e tablets');


INSERT INTO Venda (venda_id, data_venda, cliente_id) VALUES 
(1, '2024-11-01', 1),
(2, '2024-11-02', 2),
(3, '2024-11-03', 3),
(4, '2024-11-04', 4),
(5, '2024-11-05', 5);


INSERT INTO Item_Venda (item_venda_id, venda_id, produto_id, quantidade, preco_unitario) VALUES 
(1, 1, 1, 2, 29.99),
(2, 1, 2, 1, 19.99),
(3, 2, 3, 1, 39.99),
(4, 3, 4, 1, 89.99),
(5, 4, 5, 1, 99.99);

