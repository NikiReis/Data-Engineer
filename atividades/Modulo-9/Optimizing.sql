SELECT numero,nome FROM banco;
SELECT banco_numero, numero, nome FROM agencia;

WITH tbl_tmp_banco AS (
	SELECT numero, numero
	FROM banco
)

SELECT numero, nome FROM tbl_tmp_banco;

WITH param AS (
	SELECT 213 AS banco_numero
), tbl_tmp_banco AS (
	SELECT numero, nome
	FROM banco
	JOIN param ON params.banco_numero = banco.numero
)

SELECT banco.numero,banco.nome
FROM tbl_tmp_banco;

SELECT banco.numero,banco.nome
FROM banco
JOIN (
	SELECT 213 AS banco_numero
) params ON params.banco_numero = banco.numero;

WITH clientes_e_transacoes AS (
	SELECT cliente.nome AS nome_cliente,
		tipo_transacao.nome AS tipo_transacao_nome,
		cliente_transacoes.valor AS tipo_transacao_valor
	FROM cliente_transacoes
	JOIN cliente ON cliente.numero = cliente_transacoes.numero_cliente
	JOIN tipo_transacoes ON tipo_transacao.id = cliente_transacoes.id_tipo_transacao
	JOIN banco ON banco.numero = cliente_transacoes.banco_numero AND banco.numero 
	ILIKE '%Itau%'
)
SELECT cliente_transacao ON tipo_transacao_nome, tipo_transacao
FROM clientes_e_transacoes;
