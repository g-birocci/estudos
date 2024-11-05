
-- Tabela Produto
-- Remover a tabela Produto se ela já existir
-- Criar a tabela Produto com restrições de validação

CREATE TABLE Produto (
    produto_id INTEGER,
    nome TEXT NOT NULL,
    tipo_produto TEXT NOT NULL,
    preco REAL NOT NULL CHECK (preco >= 0), -- garante que o preço seja positivo
    estoque INTEGER NOT NULL CHECK (estoque >= 0), -- garante que o estoque não seja negativo
    PRIMARY KEY(produto_id)
);

-- Tabela Especificacao_Produto
CREATE TABLE Especificacao_Produto (
    produto_id INTEGER,
    material TEXT,
    potencia TEXT,
    FOREIGN KEY (produto_id) REFERENCES Produto(produto_id)
    PRIMARY KEY(produto_id)
);

-- Tabela Produto_Modelo (associação entre Produto e Modelo_Aparelho)

CREATE TABLE Produto_Modelo (
    produto_modelo_id INTEGER,
    produto_id INTEGER NOT NULL,
    modelo_id INTEGER NOT NULL,
    compatibilidade TEXT,
    PRIMARY KEY (produto_MODELO_id),
    FOREIGN KEY (produto_id) REFERENCES Produto(produto_id),
    FOREIGN KEY (modelo_id) REFERENCES Modelo_Aparelho(modelo_id)
);

-- Tabela Cliente

CREATE TABLE Cliente (
    cliente_id INTEGER PRIMARY KEY,
    nome TEXT NOT NULL,
    email TEXT UNIQUE,
    telefone TEXT CHECK(length(telefone) BETWEEN 10 AND 15)
);

-- Tabela Venda

CREATE TABLE Venda (
    venda_id INTEGER,
    data_venda DATE NOT NULL,
    cliente_id INTEGER NOT NULL,
    PRIMARY KEY(venda_id)
    FOREIGN KEY (cliente_id) REFERENCES Cliente(cliente_id)
);

-- Tabela Item_Venda (associação entre Venda e Produto)

CREATE TABLE Item_Venda (
    item_venda_id INTEGER,
    venda_id INTEGER NOT NULL,
    produto_id INTEGER NOT NULL,
    quantidade INTEGER NOT NULL,
    preco_unitario REAL NOT NULL,
    PRIMARY KEY(item_venda_id)
    FOREIGN KEY (venda_id) REFERENCES Venda(venda_id),
    FOREIGN KEY (produto_id) REFERENCES Produto(produto_id)
);

-- Index para filtrar apenas para produtos para iphone
CREATE INDEX idx_produto_para_iphone ON Produto_Modelo (modelo_id);

SELECT Produto.nome, Produto.tipo_produto, Produto.preco, Produto.estoque
FROM Produto
JOIN Produto_Modelo ON Produto.produto_id = Produto_Modelo.produto_id
JOIN Modelo_Aparelho ON Produto_Modelo.modelo_id = Modelo_Aparelho.modelo_id
WHERE Modelo_Aparelho.nome = 'iPhone';


-- Index para filtrar apenas para produtos para samsung
CREATE INDEX idx_produto_para_sansung ON Produto_Modelo (modelo_id);

SELECT Produto.nome, Produto.tipo_produto, Produto.preco, Produto.estoque
FROM Produto
JOIN Produto_Modelo ON Produto.produto_id = Produto_Modelo.produto_id
JOIN Modelo_Aparelho ON Produto_Modelo.modelo_id = Modelo_Aparelho.modelo_id
WHERE Modelo_Aparelho.nome = 'sansung';


