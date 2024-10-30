# TABLE DEFINITIONS TO INITIALIZE THE DATABASE
table_definitions = {
    "inventory":"""
        CREATE TABLE IF NOT EXISTS inventory (
        id SERIAL PRIMARY KEY,
        title VARCHAR(255) NOT NULL,
        description TEXT NOT NULL,
        price NUMERIC(10,2) NOT NULL,
        quantity INTEGER NOT NULL,
        photo VARCHAR (255) NOT NULL,
        is_active BOOLEAN DEFAULT TRUE,
        CONSTRAINT price_positive CHECK (price > 0),
        CONSTRAINT quantity_nonnegative CHECK (quantity >= 0)
        );
    """,
}