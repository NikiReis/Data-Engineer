
INSERT INTO cliente VALUES (1,'Linek','pedrin04@gmai.com',TRUE,now()),
(2,'Carla','carlin@1gmai.com',TRUE,now()),
(3,'Luis','luisin@hotmail.com',TRUE,now()),
(4,'Maria','mary1@yahoo.com',TRUE,now());

SELECT * FROM cliente;

INSERT INTO banco VALUES (1,'Banco do Brasil',TRUE,'1808-10-02'),
(3,'Banco Itaú',TRUE,'2008-11-04'),
(2,'Caixa Econômica Federal',TRUE,'1861-01-12');

SELECT * FROM banco;

INSERT INTO agencia VALUES (1,101,'Agencia JK',TRUE,now()),
(1,1,'Primeira agencia',TRUE,'1808-10-02'),
(3,12,'Agencia Avenida Paulista',TRUE,'2009-01-10'),
(3,4,'Agencia Corcovado',TRUE,'2009-02-13'),
(2,9,'Agencia Pedro Ribas',TRUE,'2014-05-23'),
(2,671,'Agencia Pedro II',TRUE,'1874-10-08');

SELECT * FROM agencia;

INSERT INTO conta_corrente VALUES (1,101,86325,4,1,TRUE,now()),
(3,4,84631,6,2,TRUE,'2009-02-13'),
(2,671,38465,5,3,FALSE,'1907-09-21'),
(1,1,57839,3,4,TRUE,'1991-10-03');

SELECT * FROM conta_corrente;

INSERT INTO tipo_transacao VALUES (1,'PIX',TRUE,'2020-02-19'),
(2,'TED',FALSE,'2002-04-23'),
(3,'DOC',TRUE,'2002-04-23'),
(4,'Deposito',TRUE,'1200-01-01'),
(5,'Saque',TRUE,'1200-01-01'),
(6,'Compra',TRUE,'1200-01-01'),
(7,'Venda',TRUE,'1200-01-01');

SELECT * FROM tipo_transacao;

