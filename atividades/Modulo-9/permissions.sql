CREATE ROLE professores NOCREATEDB NOCREATEROLE 
	INHERIT NOLOGIN NOBYPASSRLS CONNECTION LIMIT 10;
	
ALTER ROLE professores PASSWORD '123';	

CREATE ROLE daniel LOGIN PASSWORD '123';

DROP ROLE daniel;
      
CREATE ROLE daniel LOGIN PASSWORD '123' IN ROLE professores;
	  
SELECT * FROM pg_roles;

DROP ROLE daniel;

CREATE ROLE daniel LOGIN PASSWORD '123' ROLE professores;

DROP ROLE daniel;

CREATE TABLE TEST (nome varchar(40));

GRANT ALL ON TABLE test TO professores;

CREATE ROLE daniel LOGIN PASSWORD '123';

-- login to the database as daniel
psql -U daniel aulasdb;
-- trying to recover some informations
SELECT nome FROM test;

DROP ROLE daniel;

-- creating the role daniel again, but this time inside role 'professores' and inheriting the privilleges 
-- from 'professores role to be able to revocer informations inside the table

CREATE ROLE daniel INHERIT LOGIN PASSWORD '123' IN ROLE professores;

-- conecting to the database again as daniel
psql -U daniel aulasdb;

-- trying again to recover the informations from the table 'test'
SELECT nome FROM test;

-- revoking daniel from professores' role, that means that daniel lost the professores privilleges
REVOKE professores FROM daniel;

ALTER ROLE daniel INHERIT LOGIN PASSWORD '123';

GRANT professores TO daniel;