CREATE OR REPLACE FUNCTION func_somar(INTEGER,INTEGER)
RETURNS INTEGER
SECURITY DEFINER
-- RETURNS NULL ON NULL INPUT
CALLED ON NULL INPUT
LANGUAGE SQL
AS $$
	SELECT COALESCE($1,100) + COALESCE($2,100);
$$;

SELECT func_somar(1,NULL);

SELECT COALESCE(NULL,NULL,'digital','daniel');


CREATE OR REPLACE FUNCTION bancos_add(p_numero INTEGER,p_nome VARCHAR,p_ativo BOOLEAN)
RETURNS INTEGER
SECURITY INVOKER
LANGUAGE PLPGSQL
CALLED ON NULL INPUT
AS $$
DECLARE variacel_id INTEGER;
BEGIN 
	IF p_numero IS NULL or p_nome IS NULL or p_ativo IS NULL THEN
		RETURN 0;
	END IF;

	SELECT INTO variavel_id numero
	FROM banco
	WHERE numero = p_numero;

	IF variavel_id IS NULL THEN 
		INSERT INTO banco(numero,nome,ativo)
		VALUES (p_numero,p_nome,p_ativo);
	ELSE
		RETURN variavel_id;
	END IF;

	SELECT INTO variavel_id numero
	FROM banco
	WHERE numero = p_numero;

	RETURN variavel_id;
END;$$;

SELECT bancos_add(5432,'Banco Novo',FALSE)

SELECT numero,nome,ativo FROM banco WHERE numero = 5432;
