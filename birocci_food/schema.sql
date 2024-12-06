-- In this SQL file, write (and comment!) the schema of your database, including the CREATE TABLE, CREATE INDEX, CREATE VIEW, etc. statements that compose it

--Tabelas birocci_food

CREATE TABLE client ( --tabela client
    id INTEGER PRIMARY KEY AUTOINCREMENT, --Só vai funcionar no sqlite3 (ori) vscode não funciona
    nome TEXT NOT NULL, 
    telefone TEXT
);

CREATE TABLE staff ( --tabela staff
    id INTEGER PRIMARY KEY AUTOINCREMENT, --Só vai funcionar no sqlite3 (ori) vscode não funciona.
    nome TEXT NOT NULL, -- NOT NULL pra não exitis funcionario fantasma na empresa.
    cargo TEXT NOT NULL, -- Exemplo: Garçom ou Cozinheiro, é NOT NULL para saber o seu cargo.
    telefone TEXT --está no formato TEXT pra ter uma melhor manipulação para numeros internacional, por conta do caracter especial como (- ou +55).
);

CREATE TABLE orders ( --tabela orders, contas todos os pediso realizado no restaurante
    id INTEGER PRIMARY KEY AUTOINCREMENT, --Só vai funcionar no sqlite3 (ori) vscode não funciona.
    client_id INTEGER NOT NULL,            -- Referência para client.
    funcionario_id INTEGER NOT NULL,       -- Referência para staff.
    data DATE NOT NULL, -- NOT NULL por conta de ser um campo muito importante para consultar futuras.
    total REAL DEFAULT 0.0, -- real por conta de ser um campo preço, e tem casas decimal antes da virgula.
    FOREIGN KEY (client_id) REFERENCES client(id),
    FOREIGN KEY (funcionario_id) REFERENCES staff(id)
);

CREATE TABLE dishes ( --tabela dishes, consta todos o pratos do menu.
    id INTEGER PRIMARY KEY AUTOINCREMENT, --Só vai funcionar no sqlite3 (ori) vscode não funciona desta forma.
    nome TEXT NOT NULL, --Nome dos pratos
    preco REAL NOT NULL,--valor de cada pratos (unidade)
    categoria TEXT --O campo categoria serva pra separa o que é entrada, prato principal e sobremesa.
);

CREATE TABLE Itens_orders ( --tabela itens_orders foi contruida após uma relação muitos para muitos.
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    order_id INTEGER NOT NULL, -- Referência para orders.
    dish_id INTEGER NOT NULL, -- Referência para dishes.
    quantidade INTEGER NOT NULL,
    subtotal REAL NOT NULL, --para saber o que cada cliente gastou.
    FOREIGN KEY (order_id) REFERENCES orders(id),
    FOREIGN KEY (dish_id) REFERENCES dishes(id)
);

PRAGMA foreign_keys = ON; --por ter usado o DB browser o SQLite exige que as chaves estrangeiras sejam explicitamente ativadas para garantir todas as referncias.

--Agora foi feito index para melhorar a perfomace de pesquisa

CREATE INDEX idx_itens_orders_dish_id ON Itens_orders (dish_id); --este index vai buscar na tabela de
CREATE INDEX idx_dishes_categoria ON dishes (categoria);

--Aqui foi criado a view pra uma melhor visualição do banco
--Está view vai buscar venda por categoria e o prato. 

CREATE VIEW view_vendas_categoria AS
SELECT 
    d.categoria,
    d.nome AS prato,
    SUM(io.quantidade) AS total_vendido
FROM Itens_orders io
JOIN dishes d ON io.dish_id = d.id
GROUP BY d.categoria, d.nome
ORDER BY d.categoria, total_vendido DESC;




--Foi criado um triger pra resgistrar as alteção de preço. 

CREATE TABLE historico_precos (
    id INTEGER PRIMARY KEY AUTOINCREMENT, -- Identificador único do histórico
    dish_id INTEGER,                     -- Referência ao prato alterado
    preco_antigo REAL,                   -- Preço antigo do prato
    preco_novo REAL,                     -- Novo preço do prato
    data_alteracao DATETIME DEFAULT CURRENT_TIMESTAMP, -- Data da alteração
    FOREIGN KEY (dish_id) REFERENCES dishes (id)       -- Garantir integridade
);

CREATE TRIGGER trigger_registrar_alteracao_preco
AFTER UPDATE ON dishes -- Aciona após um UPDATE na tabela `dishes`
FOR EACH ROW
WHEN OLD.preco != NEW.preco -- Só executa quando o preço é alterado
BEGIN
    INSERT INTO historico_precos (dish_id, preco_antigo, preco_novo)
    VALUES (OLD.id, OLD.preco, NEW.preco); -- contem os valores do histórico
END;
