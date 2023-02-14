INSERT INTO funcionarios (nome,gerente) VALUES ('Ancelmo',null);
INSERT INTO funcionarios (nome,gerente) VALUES ('Beatriz',1);
INSERT INTO funcionarios (nome,gerente) VALUES ('Magno',1);
INSERT INTO funcionarios (nome,gerente) VALUES ('Cremilda',2);
INSERT INTO funcionarios (nome,gerente) VALUES ('Wagner',4);

SELECT id,nome,gerente FROM funcionarios WHERE gerente is NULL
UNION ALL
SELECT id,nome,gerente FROM funcionarios WHERE id = 999;

CREATE OR REPLACE RECURSIVE VIEW AS vw_func(id,gerente,funcionario) AS (
	SELECT id, gerente, nome
	FROM funcionarios
	WHERE gerente IS NULL
	
	UNION ALL
	
	SELECT funcionarios.id,funcionarios.gerente, funcionarios.nome
	FROM funcionarios
	JOIN vw_func ON vw_func.id = funcionarios.gerente
);

SELECT id, gerente, funcionario FROM vw_func;

