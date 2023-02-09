CREATE DATABASE financas;

CREATE TABLE IF NOT EXISTS banco (
	numero INTEGER NOT NULL PRIMARY KEY,
	nome VARCHAR(80) NOT NULL UNIQUE,
	ativo BOOLEAN NOT NULL DEFAULT TRUE,
	data_criacao TIMESTAMP NOT NULL DEFAULT NOW()
);

CREATE TABLE IF NOT EXISTS agencia (
	banco_numero INTEGER NOT NULL,
	numero_agencia INTEGER NOT NULL,
	nome VARCHAR(60) NOT NULL,
	ativo BOOLEAN NOT NULL DEFAULT TRUE,
	data_criacao TIMESTAMP NOT NULL DEFAULT NOW(),
	CONSTRAINT pk_identifY_bank_agency PRIMARY KEY (banco_numero,numero_agencia),
	CONSTRAINT fk_numero_banco FOREIGN KEY (banco_numero) REFERENCES banco(numero)
);

CREATE TABLE cliente(
	numero BIGSERIAL PRIMARY KEY,
	nome VARCHAR (120) NOT NULL,
	email VARCHAR(90) NOT NULL,
	ativo BOOLEAN NOT NULL DEFAULT TRUE,
	data_cricao TIMESTAMP NOT NULL DEFAULT NOW()
);

CREATE TABLE conta_corrente(
	banco_numero INTEGER NOT NULL,
	agencia_numero INTEGER NOT NULL,
	numero_conta BIGINT NOT NULL,
	digito SMALLINT NOT NULL,
	numero_cliente BIGINT NOT NULL,
	ativo BOOLEAN NOT NULL DEFAULT TRUE,
	data_cricao TIMESTAMP NOT NULL DEFAULT NOW(),
	CONSTRAINT pK_identificacao PRIMARY KEY (banco_numero,agencia_numero,numero_conta,digito,numero_cliente),
	CONSTRAINT fk_contac_bancoagencia FOREIGN KEY (banco_numero,agencia_numero) REFERENCES agencia(banco_numero,numero_agencia),
	CONSTRAINT fk_id_cliente FOREIGN KEY (numero_cliente) REFERENCES cliente(numero)
);

CREATE TABLE tipo_transacao(
	id_trasacao SMALLSERIAL PRIMARY KEY,
	nome VARCHAR(70) NOT NULL,
	ativo BOOLEAN NOT NULL DEFAULT TRUE,
	data_criacao TIMESTAMP DEFAULT NOW()
);

CREATE TABLE cliente_transacoes(
	id BIGSERIAL PRIMARY KEY,
	banco_numero INTEGER NOT NULL,
	agencia_numero INTEGER NOT NULL,
	numero_conta_corrente BIGINT NOT NULL,
	digito_conta_corrente SMALLINT NOT NULL,
	numero_cliente BIGINT NOT NULL,
	id_tipo_transacao SMALLINT NOT NULL,
	valor NUMERIC(15,2) NOT NULL,
	data_transacao TIMESTAMP NOT NULL DEFAULT NOW(),
	CONSTRAINT fk_ident_transacao_conta FOREIGN KEY (banco_numero,agencia_numero,numero_conta_corrente,digito_conta_corrente,numero_cliente) REFERENCES conta_corrente(banco_numero,agencia_numero,numero_conta,digito,numero_cliente)
);