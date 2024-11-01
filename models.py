# SECTION: SELECT
SELECT_ACTIVE_INVENTORY="SELECT * FROM inventory WHERE is_active = 'true'"
SELECT_USERNAME = "SELECT username from users WHERE username = %s"
SELECT_PASSWORD = "SELECT password FROM users WHERE username = %s"
SELECT_USER_TYPE= "SELECT user_type FROM users WHERE username = %s"
SELECT_EMAIL = "SELECT email from users WHERE email = %s"

# SECTION INSERT
REGISTER_USER= "INSERT INTO users (email, username, password, first_name, last_name, user_type) VALUES (%s,%s,%s,%s,%s,%s)"