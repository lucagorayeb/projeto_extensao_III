-- Function to update de column update_at
CREATE FUNCTION trigger_set_timestamp()
RETURNS TRIGGER as $$
BEGIN
    NEW.updated_at = NOW();
    RETURN NEW;
    END;
$$ language plpgsql;

-- Loop to trigger the function above in all tables
DO $$
DECLARE
    t text;
BEGIN
    FOR t IN
        SELECT table_name
        FROM information_schema.columns
        WHERE table_schema = 'public'
            AND column_name = 'updated_at'
            AND table_name NOT LIKE 'pq_%'
    LOOP
        EXECUTE format('DROP TRIGGER IF EXISTS set_timestamp ON %I;', t);
        EXECUTE format('CREATE TRIGGER set_timestamp BEFORE UPDATE ON %I FOR EACH ROW EXECUTE FUNCTION trigger_set_timestamp();', t);
    END LOOP;
END;
$$;

-- Setting the local timezone
SET TIME ZONE 'America/Porto_Velho';

CREATE TABLE IF NOT EXISTS users(
    user_id INT PRIMARY KEY GENERATED ALWAYS AS IDENTITY,
	user_email VARCHAR(50) unique NOT NULL,
    user_password VARCHAR(255) NOT NULL,
    user_fk_member INT NOT NULL REFERENCES member(member_id),
    created_at TIMESTAMP NOT NULL DEFAULT NOW(),
    updated_at TIMESTAMP NOT NULL DEFAULT NOW()

);

CREATE TABLE IF NOT EXISTS member(
    member_id INT PRIMARY KEY GENERATED ALWAYS AS IDENTITY,
    member_name VARCHAR(100) NOT NULL,
    member_cpf CHAR(11) NOT NULL,
    member_function INT NOT NULL,
    created_at TIMESTAMP NOT NULL DEFAULT NOW(),
    updated_at TIMESTAMP NOT NULL DEFAULT NOW()
);

CREATE TABLE IF NOT EXISTS function(
    function_id INT PRIMARY KEY GENERATED ALWAYS AS IDENTITY,
    function_name VARCHAR(50) NOT NULL,
    created_at TIMESTAMP NOT NULL DEFAULT NOW()
);

CREATE TABLE IF NOT EXISTS supplier(
    supplier_id INT PRIMARY KEY GENERATED ALWAYS AS IDENTITY,
    supplier_name VARCHAR(50) NOT NULL,
    supplier_cpf_cnpj VARCHAR(15) NOT NULL unique,
    supplier_email VARCHAR(20) NOT NULL,
    supplier_telephone VARCHAR(10) NOT NULL,
    supplier_address INT NOT NULL,
    created_at TIMESTAMP NOT NULL DEFAULT NOW(),
    updated_at TIMESTAMP NOT NULL DEFAULT NOW()
);

CREATE TABLE IF NOT EXISTS address(
    address_id INT PRIMARY KEY GENERATED ALWAYS AS IDENTITY,
    address_cep CHAR(8) NOT NULL,
    address_logradouro VARCHAR(150) NOT NULL,
    address_number INT NOT NULL,
    address_complement VARCHAR(20) NOT NULL,
    address_neighbor VARCHAR(100) NOT NULL,
    address_city VARCHAR(100) NOT NULL,
    address_state VARCHAR(2) NOT NULL,
    created_at TIMESTAMP NOT NULL DEFAULT NOW(),
    updated_at TIMESTAMP NOT NULL DEFAULT NOW()
);

CREATE TABLE IF NOT EXISTS supplier_address(
    supplier_address_id INT PRIMARY KEY GENERATED ALWAYS AS IDENTITY,
    supplier_address_fk_id_supplier INT NOT NULL REFERENCES supplier(supplier_id),
    supplier_address_fk_id_address INT NOT NULL REFERENCES address(address_id),
    created_at TIMESTAMP NOT NULL DEFAULT NOW(),
    updated_at TIMESTAMP NOT NULL DEFAULT NOW()
);

CREATE TABLE IF NOT EXISTS product(
    product_id INT PRIMARY KEY GENERATED ALWAYS AS IDENTITY,
    product_name VARCHAR(50) NOT NULL,
    product_description VARCHAR(255) NOT NULL,
    product_code_bar VARCHAR(50) NOT NULL unique,
    product_buy_price FLOAT NOT NULL,
    product_for_sale BOOLEAN NOT NULL,
    product_sale_price FLOAT,
    product_category INT NOT NULL,
    created_at TIMESTAMP NOT NULL DEFAULT NOW(),
    updated_at TIMESTAMP NOT NULL DEFAULT NOW()
);

CREATE TABLE IF NOT EXISTS product_supplier(
    product_supplier_id INT PRIMARY KEY GENERATED ALWAYS AS IDENTITY,
    product_supplier_fk_id_product INT NOT NULL REFERENCES product(product_id),
    product_supplier_fk_id_supplier INT NOT NULL REFERENCES supplier(supplier_id),
    created_at TIMESTAMP NOT NULL DEFAULT NOW(),
    updated_at TIMESTAMP NOT NULL DEFAULT NOW()
);

CREATE TABLE IF NOT EXISTS storage(
    storage_id INT PRIMARY KEY GENERATED ALWAYS AS IDENTITY,
    storage_fk_id_product INT NOT NULL REFERENCES product(product_id),
    storage_quantity INT NOT NULL,
    storage_minimal_quantity INT NOT NULL,
    storage_blade VARCHAR(50) NOT NULL,
    created_at TIMESTAMP NOT NULL DEFAULT NOW(),
    updated_at TIMESTAMP NOT NULL DEFAULT NOW()
);

CREATE TYPE movement_type AS ENUM('IN', 'OUT', 'ADJUSTMENTS');
CREATE TABLE IF NOT EXISTS movement(
    movement_id INT PRIMARY KEY GENERATED ALWAYS AS IDENTITY,
    movement_fk_product_id INT NOT NULL REFERENCES product(product_id),
    movement_fk_supplier_id INT NOT NULL REFERENCES supplier(supplier_id),
    movement_type MOVEMENT_TYPE NOT NULL,
    movement_quantity INT NOT NULL,
    movement_fk_id_member INT NOT NULL REFERENCES member(member_id),
    movement_fk_id_user INT NOT NULL REFERENCES users(user_id),
    created_at TIMESTAMP NOT NULL DEFAULT NOW()
);

CREATE TABLE IF NOT EXISTS logs(
    log_id INT PRIMARY KEY GENERATED ALWAYS AS IDENTITY,
    log_fk_id_member INT NOT NULL REFERENCES member(member_id),
    log_fk_id_user INT NOT NULL REFERENCES users(user_id),
    log_action VARCHAR(255) NOT NULL,
    created_at TIMESTAMP NOT NULL DEFAULT NOW()
);