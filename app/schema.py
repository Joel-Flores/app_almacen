instrutions = [
    "DROP TABLE IF EXISTS todo;",
    "DROP TABLE IF EXISTS user;",
    """CREATE TABLE user(
        id INT PRIMARY KEY AUTO_INCREMENT,
        username VARCHAR(25) UNIQUE NOT NULL,
        password VARCHAR(110) NOT NULL
        );
    """
]
