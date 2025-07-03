-- Criar banco de dados se não existir
CREATE DATABASE IF NOT EXISTS contatos_java;

-- Usar o banco de dados
USE contatos_java;

-- Criar tabela de contatos se não existir
CREATE TABLE IF NOT EXISTS contatos (
    id BIGINT PRIMARY KEY AUTO_INCREMENT,
    nome VARCHAR(100) NOT NULL,
    telefone VARCHAR(20),
    email VARCHAR(100)
); 