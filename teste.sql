--
-- File generated with SQLiteStudio v3.3.3 on sex jun 24 18:02:22 2022
--
-- Text encoding used: System
--
PRAGMA foreign_keys = off;
BEGIN TRANSACTION;

-- Table: info_pagamento
CREATE TABLE info_pagamento (id INTEGER PRIMARY KEY AUTOINCREMENT, n_conta VARCHAR UNIQUE NOT NULL, tipo_conta VARCHAR NOT NULL, saldo_uber INTEGER, agencia INTEGER NOT NULL);
INSERT INTO info_pagamento (id, n_conta, tipo_conta, saldo_uber, agencia) VALUES (1, '2333333333-2', 'corrente', 120, 237);
INSERT INTO info_pagamento (id, n_conta, tipo_conta, saldo_uber, agencia) VALUES (2, '2444444444-2', 'corrente', 0, 4660);
INSERT INTO info_pagamento (id, n_conta, tipo_conta, saldo_uber, agencia) VALUES (3, '9222222222-2', 'corrente', 10, 7);
INSERT INTO info_pagamento (id, n_conta, tipo_conta, saldo_uber, agencia) VALUES (4, '9111111111-2', 'corrente', 0, 7);

-- Table: localizacoes
CREATE TABLE localizacoes (id INTEGER PRIMARY KEY AUTOINCREMENT, CEP VARCHAR NOT NULL, localizacao_maps BLOB NOT NULL, nome VARCHAR NOT NULL);
INSERT INTO localizacoes (id, CEP, localizacao_maps, nome) VALUES (1, '66017-060', 'https://goo.gl/maps/3dNpmxcXTpeH7cLH7', 'Teatro da paz');
INSERT INTO localizacoes (id, CEP, localizacao_maps, nome) VALUES (2, '66075-110', 'https://goo.gl/maps/eReB75mXZoq6J2BE7', 'Universidade Federal do par�');

-- Table: motorista
CREATE TABLE motorista (id INTEGER PRIMARY KEY AUTOINCREMENT, nome NOT NULL, telefone UNIQUE NOT NULL, veiculo_atual REFERENCES veiculo (id), conta_corrente VARCHAR REFERENCES info_pagamento (id), avaliacao DECIMAL (1));

-- Table: usuario
CREATE TABLE usuario (id INTEGER PRIMARY KEY AUTOINCREMENT, nome VARCHAR NOT NULL, telefone VARCHAR UNIQUE NOT NULL, genero CHAR NOT NULL, pontos_uber INTEGER, metodo_pagamento INTEGER REFERENCES info_pagamento (id), avaliacao DECIMAL (1));
INSERT INTO usuario (id, nome, telefone, genero, pontos_uber, metodo_pagamento, avaliacao) VALUES (1, 'Erick', '(91)91111-1111', 'm', 0, 2, 3.5);
INSERT INTO usuario (id, nome, telefone, genero, pontos_uber, metodo_pagamento, avaliacao) VALUES (2, 'Gustavo Lima', '(91)92222-2222', 'm', 28, 1, 4.5);

-- Table: veiculo
CREATE TABLE veiculo (id INTEGER PRIMARY KEY AUTOINCREMENT, placa VARCHAR NOT NULL UNIQUE, modelo VARCHAR NOT NULL, marca VARCHAR NOT NULL, tipo VARCHAR NOT NULL);
INSERT INTO veiculo (id, placa, modelo, marca, tipo) VALUES (1, 'OTX-3899', 'POP 110', 'HONDA', 'Moto');
INSERT INTO veiculo (id, placa, modelo, marca, tipo) VALUES (2, 'LOL-9008', 'KWID', 'RENAULT', 'Carro');
INSERT INTO veiculo (id, placa, modelo, marca, tipo) VALUES (3, 'ZED-5512', 'MOBI LIKE', 'FIAT', 'Carro');

-- Table: viagens
CREATE TABLE viagens (id INTEGER PRIMARY KEY AUTOINCREMENT, id_motorista REFERENCES motorista (id), id_passageiro REFERENCES usuario (id), id_carro REFERENCES veiculo (id), localizacao_inicial BLOB NOT NULL, localizacao_final BLOB NOT NULL, pedido_corrida DATETIME NOT NULL, tempo_inicio_corrida DATETIME NOT NULL, tempo_fim_corrida DATETIME NOT NULL, paradas BOOLEAN NOT NULL, localizacao_parada BLOB, custo_viagem INTEGER NOT NULL, viagem_paga BOOLEAN NOT NULL);

COMMIT TRANSACTION;
PRAGMA foreign_keys = on;
