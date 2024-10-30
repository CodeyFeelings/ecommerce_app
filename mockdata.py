from db_setup import connect_database

inventory_definitions = {
    "item1":"""
        INSERT INTO inventory (title,description, price, quantity, photo, is_active) VALUES ('Small Succulents','Two low-maintenance plants perfect for a desk or windowsill.', '10.00', '50', '../static/uploads/succulents.jpg', 'True')
    """,
    "item2": """
        INSERT INTO inventory (title,description, price, quantity, photo, is_active) VALUES ('Stonehenge painting','A serene landscape capturing the ancient wonder.', '50.00', '10', '../static/uploads/stonhenge-painting.jpg', 'True')
    """,
    "item3": """
        INSERT INTO inventory (title,description, price, quantity, photo, is_active) VALUES ('Leather pouch','A stylish and durable accessory for everyday carry.', '20.00', '50', '../static/uploads/leather-pouch.jpg', 'True')
    """,
    "item4": """
        INSERT INTO inventory (title,description, price, quantity, photo, is_active) VALUES ('Goldfish painting','A vibrant and playful depiction of aquatic life.', '30.00', '25', '../static/uploads/goldfish-photo.jpg', 'True')
    """,
    "item5": """
        INSERT INTO inventory (title,description, price, quantity, photo, is_active) VALUES ('Duffle bag','A spacious and versatile bag for travel or weekend getaways.', '50.00', '30', '../static/uploads/duffle-bag.jpg', 'True')
    """,
    "item6": """
        INSERT INTO inventory (title,description, price, quantity, photo, is_active) VALUES ('Desk lamp','A functional and stylish addition to any workspace.', '20.00', '100', '../static/uploads/desk-lamp.jpg', 'True')
    """,
    "item7": """
        INSERT INTO inventory (title,description, price, quantity, photo, is_active) VALUES ('Crochet ornaments','A handmade and unique decoration for the holiday season.', '10.00', '100', '../static/uploads/crochet-ornaments.jpg', 'True')
    """,
    "item8": """
        INSERT INTO inventory (title,description, price, quantity, photo, is_active) VALUES ('Crochet animal','A cute and cuddly companion for a child or adult.', '20.00', '50', '../static/uploads/crochet-animal.jpg', 'True')
    """,
    "item9": """
        INSERT INTO inventory (title,description, price, quantity, photo, is_active) VALUES ('Mid-century modern chair','A stylish and comfortable seating option for any room.', '200.00', '15', '../static/uploads/chair.jpg', 'False')
    """,
    "item10": """
        INSERT INTO inventory (title,description, price, quantity, photo, is_active) VALUES ('Abstract painting','A bold and expressive piece of art that will add personality to any space.', '50.00', '25', '../static/uploads/abstract-painting.jpg', 'False')
    """
}

def insert_mock_data():
    conn= connect_database()
    db=conn.cursor()
    for insert_name, insert_data in inventory_definitions.items():
        db.execute(insert_data)
    conn.commit()
    db.close()


if __name__ == "__main__":
    insert_mock_data()
