SELECT numero,nome FROM banco;
SELECT banco_numero,numero_agencia,nome FROM agencia;
SELECT numero, nome, email FROM cliente;
SELECT banco_numero,agencia_numero,numero_cliente FROM cliente_transacoes;

SELECT * FROM conta_corrente;

SELECT * FROM INFORMATION_SCHEMA.COLUMNS WHERE TABLE_NAME = 'banco';
SELECT COLUMN_NAME, DATA_TYPE FROM INFORMATION_SCHEMA.COLUMNS WHERE TABLE_NAME = 'banco';

-- AVG
-- COUNT(HAVING)
-- MAX 
-- MIN 
-- SUM

SELECT * FROM cliente_transacoes;

SELECT AVG(valor) FROM cliente_transacoes;

SELECT COUNT(numero) FROM client;

SELECT COUNT (numero),email FROM cliente WHERE email ILIKE '%gmail.com' GROUP BY email;

SELECT MAX (numero) FROM cliente;

SELECT MIN (numero) FROM cliente;

SELECT MAX(valor) FROM cliente_transacoes;

SELECT MIN (valor) FROM cliente_transacoes;

SELECT MAX (valor), id_tipo_transacao FROM cliente_transacoes GROUP BY id_tipo_transacoes;

SELECT MIN (valor), id_tipo_transacao FROM cliente_transacoes GROUP BY id_tipo_transacoes;

SELECT COLUMN_NAME, DATA_TYPE FROM INFORMATION_SCHEMA.COLUMNS WHERE TABLE = 'cliente_transacoes';

SELECT COUNT(id),id_tipo_transacao FROM cliente_transacoes GROUP BY id_tipo_transacao;

SELECT COUNT(id),id_tipo_transacao FROM cliente_transacoes GROUP BY id_tipo_transacao HAVING COUNT(id) > 150;

SELECT SUM(valor) FROM cliente_transacoes;

SELECT SUM(valor),id_tipo_transacao FROM cliente_transacoes GROUP BY id_tipo_transacao;
