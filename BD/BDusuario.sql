CREATE DATABASE cadastro_usuario;
USE cadastro_usuario;

CREATE TABLE usuario(
	id_usuario INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
    nome VARCHAR(100) NOT NULL,
    email VARCHAR(100),
    senha VARCHAR(100),
    data_criacao varchar(20)
);

drop database cadastro_usuario;
SELECT * FROM usuario;