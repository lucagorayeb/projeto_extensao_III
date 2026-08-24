SET TIME ZONE 'America/Porto_Velho';

CREATE TABLE IF NOT EXISTS users(
    user_id INT PRIMARY KEY GENERATED ALWAYS AS IDENTITY,
	user_email VARCHAR(50) unique NOT NULL,
    user_password VARCHAR(255) NOT NULL,
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
    supplier_address_id_supplier INT NOT NULL,
    supplier_address_id_address INT NOT NULL,
    created_at TIMESTAMP NOT NULL DEFAULT NOW(),
    updated_at TIMESTAMP NOT NULL DEFAULT NOW()
);

CREATE TABLE IF NOT EXISTS product(
    product_id INT PRIMARY KEY GENERATED ALWAYS AS IDENTITY,
    product_name VARCHAR(50) NOT NULL,
    product_description VARCHAR(255) NOT NULL,
    product_code_bar VARCHAR(50) NOT NULL unique,
    product_buy_price float NOT NULL,
    product_for_sale boolean NOT NULL,
    product_sale_price float,
    product_category INT NOT NULL,
    created_at TIMESTAMP NOT NULL DEFAULT NOW(),
    updated_at TIMESTAMP NOT NULL DEFAULT NOW()
);

CREATE TABLE IF NOT EXISTS product_supplier(
    product_supplier_id INT PRIMARY KEY GENERATED ALWAYS AS IDENTITY,
    product_supplier_id_product INT NOT NULL,
    product_supplier_id_supplier INT NOT NULL,
    created_at TIMESTAMP NOT NULL DEFAULT NOW(),
    updated_at TIMESTAMP NOT NULL DEFAULT NOW(),
    FOREIGN KEY(produto_id) REFERENCES produto(id),
    FOREIGN KEY(fornecedor_id) REFERENCES fornecedor(id),
    unique(produto_id, fornecedor_id)
);

CREATE TABLE IF NOT EXISTS storage(
    storage_id INT PRIMARY KEY GENERATED ALWAYS AS IDENTITY,
    storage_product_id INT NOT NULL,
    storage_quantity INT NOT NULL,
    storage_minimal_quantity INT NOT NULL,
    storage_blade VARCHAR(50) NOT NULL,
    created_at TIMESTAMP NOT NULL DEFAULT NOW(),
    updated_at TIMESTAMP NOT NULL DEFAULT NOW(),
    FOREIGN KEY(produto_id) REFERENCES produto(id)
);

CREATE TABLE IF NOT EXISTS movement(
    movement_id SERIAL,
    movement_product_id INT NOT NULL,
    movement_fornecedor_id INT,
    movement_type VARCHAR NOT NULL CHECK(tipo IN ('entrada','saida','ajuste')),
    movement_quantidade INT NOT NULL,
    movement_usuario_id INT NOT NULL,
    created_at TIMESTAMP NOT NULL DEFAULT NOW(),
    FOREIGN KEY(produto_id) REFERENCES produto(id),
    FOREIGN KEY(fornecedor_id) REFERENCES fornecedor(id),
    FOREIGN KEY(usuario_id) REFERENCES usuario(id)
);