CREATE_USER_TABLE_QUERY = '''
    CREATE TABLE IF NOT EXISTS telegram_users
    (ID INTEGER PRIMARY KEY,
    TELEGRAM_ID INTEGER,
    USERNAME CHAR(50),
    FIRST_NAME CHAR(50),
    LAST_NAME CHAR(50),
    UNIQUE(TELEGRAM_ID)
    )

'''

INSERT_USER_QUERY = '''INSERT OR IGNORE INTO telegram_users VALUES (?,?,?,?,?)'''


CREATE_BAN_USER_TABLE_QUERY = """
        CREATE TABLE IF NOT EXISTS ban_users
        (ID INTEGER PRIMARY KEY,
        TELEGRAM_ID INTEGER,
        COUNT INTEGER,
        UNIQUE (TELEGRAM_ID)
        )
"""

INSERT_BAN_USER_QUERY = """INSERT OR IGNORE INTO ban_users VALUES (?,?,?)"""

SELECT_BAN_USER_QUERY = """
SELECT * FROM ban_users WHERE TELEGRAM_ID = ?
"""

UPDATE_BAN_USER_COUNT_QUERY = """
UPDATE ban_users SET COUNT = COUNT + 1 WHERE TELEGRAM_ID = ?
"""

CREATE_USER_FORM_TABLE_QUERY = """
    CREATE TABLE IF NOT EXISTS user_form
    (ID INTEGER PRIMARY KEY,
    TELEGRAM_ID INTEGER,
    NICKNAME CHAR(50),
    BIO TEXT,
    AGE INTEGER,
    OCCUPATION TEXT,
    MARRIED CHAR(50),
    PHOTO TEXT,
    UNIQUE (TELEGRAM_ID)
    )
"""

INSERT_USER_FORM_QUERY = """INSERT OR IGNORE INTO user_form VALUES (?,?,?,?,?,?,?,?)"""
SELECT_USER_FORM_QUERY = """
SELECT * FROM user_form WHERE TELEGRAM_ID = ?
"""