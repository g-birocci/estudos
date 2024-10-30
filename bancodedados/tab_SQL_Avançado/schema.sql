-- Tabela Modelo_Aparelho
CREATE TABLE Modelo_Aparelho (
    modelo_id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome_modelo TEXT NOT NULL,
    marca TEXT NOT NULL
);

-- Tabela Produto
CREATE TABLE Produto (
    produto_id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    tipo_produto TEXT NOT NULL,
    preco REAL NOT NULL,
    estoque INTEGER NOT NULL
);

-- Tabela Especificacao_Produto
CREATE TABLE Especificacao_Produto (
    produto_id INTEGER PRIMARY KEY,
    material TEXT,
    potencia TEXT,
    FOREIGN KEY (produto_id) REFERENCES Produto(produto_id)
);

-- Tabela Produto_Modelo (associação entre Produto e Modelo_Aparelho)
CREATE TABLE Produto_Modelo (
    produto_modelo_id INTEGER PRIMARY KEY AUTOINCREMENT,
    produto_id INTEGER NOT NULL,
    modelo_id INTEGER NOT NULL,
    compatibilidade TEXT,
    FOREIGN KEY (produto_id) REFERENCES Produto(produto_id),
    FOREIGN KEY (modelo_id) REFERENCES Modelo_Aparelho(modelo_id)
);

-- Tabela Cliente
CREATE TABLE Cliente (
    cliente_id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    email TEXT UNIQUE,
    telefone TEXT
);

-- Tabela Venda
CREATE TABLE Venda (
    venda_id INTEGER PRIMARY KEY AUTOINCREMENT,
    data_venda DATE NOT NULL,
    cliente_id INTEGER NOT NULL,
    FOREIGN KEY (cliente_id) REFERENCES Cliente(cliente_id)
);

-- Tabela Item_Venda (associação entre Venda e Produto)
CREATE TABLE Item_Venda (
    item_venda_id INTEGER PRIMARY KEY AUTOINCREMENT,
    venda_id INTEGER NOT NULL,
    produto_id INTEGER NOT NULL,
    quantidade INTEGER NOT NULL,
    preco_unitario REAL NOT NULL,
    FOREIGN KEY (venda_id) REFERENCES Venda(venda_id),
    FOREIGN KEY (produto_id) REFERENCES Produto(produto_id)
);
