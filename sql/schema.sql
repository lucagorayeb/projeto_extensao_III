CREATE TABLE usuario(id INTEGER PRIMARY KEY AUTOINCREMENT,
		      nome TEXT NOT NULL UNIQUE);

CREATE TABLE fornecedor(id INTEGER PRIMARY KEY AUTOINCREMENT,
			  nome TEXT NOT NULL,
			  cpf_cnpj TEXT NOT NULL UNIQUE,
			  email TEXT NOT NULL,
			  telefone TEXT NOT NULL,
			  endereco TEXT NOT NULL,
			  cidade TEXT NOT NULL,
			  estado TEXT NOT NULL); 

CREATE TABLE produto(id INTEGER PRIMARY KEY AUTOINCREMENT,
		      nome TEXT NOT NULL,
       	              descricao TEXT NOT NULL,
		      codigo_barra TEXT NOT NULL UNIQUE,
	              preco_custo REAL NOT NULL,
		      vendivel INTEGER NOT NULL,
		      preco_venda REAL,
		      categoria TEXT NOT NULL);

CREATE TABLE estoque(id INTEGER PRIMARY KEY AUTOINCREMENT,
		     produto_id INTEGER NOT NULL,
		     quantidade INTEGER NOT NULL,
		     quantidade_minima INTEGER NOT NULL,
		     localizacao TEXT NOT NULL,
		     FOREIGN KEY(produto_id) REFERENCES produto(id));

CREATE TABLE movimentacao(id INTEGER PRIMARY KEY AUTOINCREMENT,
			  produto_id INTEGER NOT NULL,
			  fornecedor_id INTEGER,
			  tipo TEXT NOT NULL CHECK(tipo IN ('entrada','saida','ajuste')),
			  quantidade INTEGER NOT NULL,
			  observacao TEXT NOT NULL,
			  usuario_id INTEGER NOT NULL,
			  data_movimentacao TEXT NOT NULL,
		     	  FOREIGN KEY(produto_id) REFERENCES produto(id),
		     	  FOREIGN KEY(fornecedor_id) REFERENCES fornecedor(id),
		     	  FOREIGN KEY(usuario_id) REFERENCES usuario(id));

CREATE TABLE produto_fornecedor(id INTEGER PRIMARY KEY AUTOINCREMENT,
				produto_id INTEGER NOT NULL,
				fornecedor_id INTEGER NOT NULL,
		     	  	FOREIGN KEY(produto_id) REFERENCES produto(id),
		     	  	FOREIGN KEY(fornecedor_id) REFERENCES fornecedor(id),
				UNIQUE(produto_id, fornecedor_id));
