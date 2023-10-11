-- migrate:up

CREATE TABLE categories(
    id serial PRIMARY KEY ,
    name varchar(100) NOT NULL,
	parent_id int REFERENCES categories (id)
);

CREATE TABLE products (
    id serial PRIMARY KEY,
    name varchar(100) NOT NULL,
	category_id int REFERENCES categories (id)
);

CREATE INDEX idx_categories_parent_id ON categories (parent_id);
CREATE INDEX idx_products_category_id ON products (category_id);

-- migrate:down

DROP TABLE IF EXISTS categories CASCADE;
DROP TABLE IF EXISTS products CASCADE;