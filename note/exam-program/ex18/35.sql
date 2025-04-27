/* Create & Drop */
CREATE TABLE ints(n UNIQUE, prime);

/* Insert */
INSERT INTO ints VALUES (2, 1), (3, 1);
INSERT INTO ints SELECT n+2, 1 FROM ints;
INSERT INTO ints SELECT n+4, 1 FROM ints;
INSERT INTO ints SELECT n+8, 1 FROM ints;
INSERT INTO ints SELECT n+16, 1 FROM ints;
SELECT * FROM ints;

/* Update */
UPDATE ints SET prime=0 WHERE n > 2 AND n % 2 = 0;
UPDATE ints SET prime=0 WHERE n > 3 AND n % 3 = 0;
UPDATE ints SET prime=0 WHERE n > 5 AND n % 5 = 0;
SELECT * FROM ints;

/* Delete */
DELETE FROM ints WHERE prime=0;
SELECT n FROM ints;
