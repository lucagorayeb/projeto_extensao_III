CREATE FUNCTION trigger_set_timestamp()
RETURNS TRIGGER as $$
BEGIN
    NEW.updated_at = NOW();
    RETURN NEW;
    END;
$$ language plpgsql;

CREATE TRIGGER set_timestamp
BEFORE UPDATE ON teste
FOR EACH ROW
 WHEN (OLD.name IS DISTINCT FROM NEW.name)
EXECUTE FUNCTION trigger_set_timestamp();

DROP FUNCTION trigger_set_timestamp();
DROP TRIGGER set_timestamp ON teste;

SET TIME ZONE 'America/Porto_Velho';
CREATE TABLE teste(
    id SERIAL PRIMARY KEY,
    name VARCHAR(10) NOT NULL,
    created_at TIMESTAMP NOT NULL DEFAULT NOW(),
    updated_at TIMESTAMPTZ NOT NULL DEFAULT NOW()
);

CREATE TABLE teste2(
    id INT PRIMARY KEY GENERATED ALWAYS AS IDENTITY,
    name VARCHAR(10) NOT NULL,
    created_at TIMESTAMP NOT NULL DEFAULT NOW(),
    updated_at TIMESTAMP NOT NULL DEFAULT NOW()
);

INSERT INTO teste (name) VALUES ('Luca');
INSERT INTO teste2 (name) VALUES ('Larissa');

UPDATE teste SET name = 'Luca Mello' WHERE teste.id = 1;

SELECT t1.id AS IDENTIFIER_TABLE_1, t1.name AS NAME_TABLE_1, t1.created_at AS CREATE_DATE_TABLE_1, t1.updated_at AS LAST_UPDATE_TABLE_1,
       t2.id AS IDENTIFIER_TABLE_2, t2.name AS NAME_TABLE_2, t2.created_at AS CREATE_DATE_TABLE_2, t2.updated_at AS LAST_UPDATE_TABLE_2
FROM teste AS t1 JOIN teste2 AS t2 ON t1.id = t2.id;

DROP TABLE teste;
DROP TABLE teste2;