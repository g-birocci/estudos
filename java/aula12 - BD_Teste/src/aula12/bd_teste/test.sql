-- phpMyAdmin SQL Dump
-- version 5.1.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Tempo de geração: 01-Abr-2025 às 16:04
-- Versão do servidor: 10.4.22-MariaDB
-- versão do PHP: 8.0.14                                                                                                                                         

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Banco de dados: `test`
--
CREATE DATABASE IF NOT EXISTS `test` DEFAULT CHARACTER SET latin1 COLLATE latin1_swedish_ci;
USE `test`;

-- --------------------------------------------------------

--
-- Estrutura da tabela `departamento`
--

CREATE TABLE `departamento` (
  `ID_DPT` int(6) NOT NULL,
  `Nome_DPT` varchar(50) NOT NULL,
  `Local` varchar(50) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Extraindo dados da tabela `departamento`
--

INSERT INTO `departamento` (`ID_DPT`, `Nome_DPT`, `Local`) VALUES
(1, 'comercial', 'Porto'),
(2, 'Recursos Humanos', 'Lisboa');

-- --------------------------------------------------------

--
-- Estrutura da tabela `funcao`
--

CREATE TABLE `funcao` (
  `ID_Funcao` int(6) NOT NULL,
  `desc_Funcao` varchar(50) NOT NULL,
  `Vencimento` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Extraindo dados da tabela `funcao`
--

INSERT INTO `funcao` (`ID_Funcao`, `desc_Funcao`, `Vencimento`) VALUES
(1, 'Vendedor', '1000'),
(2, 'Director', '1800'),
(3, 'Assistente Administrativo', '1000');

-- --------------------------------------------------------

--
-- Estrutura da tabela `funcionario`
--

CREATE TABLE `funcionario` (
  `ID_Funcionario` int(6) NOT NULL,
  `Nome` varchar(50) NOT NULL,
  `Morada` varchar(50) DEFAULT NULL,
  `Telefone` int(9) DEFAULT NULL,
  `Email` varchar(50) DEFAULT NULL,
  `ID_DPT` int(6) NOT NULL,
  `ID_Funcao` int(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Extraindo dados da tabela `funcionario`
--

INSERT INTO `funcionario` (`ID_Funcionario`, `Nome`, `Morada`, `Telefone`, `Email`, `ID_DPT`, `ID_Funcao`) VALUES
(2, 'Alexandre Gois', 'Rua da Saudade', 912345678, 'AG@teste.com', 1, 2),
(3, 'Ricardo Duarte', 'Rua das ervas', 918765432, 'RD@teste.com', 2, 3);

--
-- Índices para tabelas despejadas
--

--
-- Índices para tabela `departamento`
--
ALTER TABLE `departamento`
  ADD PRIMARY KEY (`ID_DPT`);

--
-- Índices para tabela `funcao`
--
ALTER TABLE `funcao`
  ADD PRIMARY KEY (`ID_Funcao`);

--
-- Índices para tabela `funcionario`
--
ALTER TABLE `funcionario`
  ADD PRIMARY KEY (`ID_Funcionario`),
  ADD KEY `fk_DPT` (`ID_DPT`),
  ADD KEY `fk_funcao` (`ID_Funcao`);

--
-- AUTO_INCREMENT de tabelas despejadas
--

--
-- AUTO_INCREMENT de tabela `departamento`
--
ALTER TABLE `departamento`
  MODIFY `ID_DPT` int(6) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT de tabela `funcao`
--
ALTER TABLE `funcao`
  MODIFY `ID_Funcao` int(6) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT de tabela `funcionario`
--
ALTER TABLE `funcionario`
  MODIFY `ID_Funcionario` int(6) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=102;

--
-- Restrições para despejos de tabelas
--

--
-- Limitadores para a tabela `funcionario`
--
ALTER TABLE `funcionario`
  ADD CONSTRAINT `fk_DPT` FOREIGN KEY (`ID_DPT`) REFERENCES `departamento` (`ID_DPT`),
  ADD CONSTRAINT `fk_funcao` FOREIGN KEY (`ID_Funcao`) REFERENCES `funcao` (`ID_Funcao`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
