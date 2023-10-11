import logging

import asyncpg
from asyncpg import Record

logger = logging.getLogger(__name__)


async def tasks_run(db_config: dict):
    conn = await asyncpg.connect(db_config.get("dsn"))
    await fill_db(conn)
    task4_result = await task4(conn, 'iPhone X')
    logger.info(task4_result)
    task5_result = await task5(conn, 'Электроника')
    logger.info(task5_result)


async def fill_db(conn: asyncpg.Connection):
    try:
        await conn.execute(
            """
            INSERT INTO categories (id, name, parent_id)
            VALUES (1, 'Электроника', NULL);
            INSERT INTO categories (id, name, parent_id)
            VALUES (2, 'Телефоны', 1);
            INSERT INTO categories (id, name, parent_id)
            VALUES (3, 'Компьютеры', 1);
            INSERT INTO categories (id, name, parent_id)
            VALUES (4, 'Смартфоны', 2);
            INSERT INTO categories (id, name, parent_id)
            VALUES (5, 'Ноутбуки', 3);
            INSERT INTO products (id, name, category_id)
            VALUES (1, 'iPhone X', 4);
            INSERT INTO products (id, name, category_id)
            VALUES (2, 'Samsung Galaxy S9', 4);
            INSERT INTO products (id, name, category_id)
            VALUES (3, 'MacBook Pro', 5);
            INSERT INTO products (id, name, category_id)
            VALUES (4, 'Dell XPS 13', 5);
            """
        )
    except asyncpg.exceptions.UniqueViolationError as e:
        logger.error(e)


async def task4(conn: asyncpg.Connection, product: str) -> list[Record]:
    result = await conn.fetch(
        f"""
        WITH RECURSIVE category_tree AS (
            SELECT id, name, parent_id
            FROM categories
            WHERE id = (SELECT category_id FROM products where name = '{product}')
            UNION ALL
            SELECT c.id, c.name, c.parent_id
            FROM categories c
            JOIN category_tree ct ON ct.parent_id = c.id
        )
        SELECT name
        FROM category_tree
        ORDER BY id DESC;
        """
    )
    return result


async def task5(conn: asyncpg.Connection, category: str) -> list[Record]:
    result = await conn.fetch(
        f"""
        WITH RECURSIVE category_tree AS (
            SELECT id, name, parent_id
            FROM categories
            WHERE id = (SELECT id FROM categories where name = '{category}')
            UNION ALL
            SELECT c.id, c.name, c.parent_id
            FROM categories c
            JOIN category_tree ct ON ct.id = c.parent_id
        )
        SELECT p.name
        FROM products p
        JOIN category_tree ct ON p.category_id = ct.id;
        """
    )
    return result
