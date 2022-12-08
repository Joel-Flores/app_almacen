instrutions = [
    "DROP TABLE IF EXISTS serials;",
    "DROP TABLE IF EXISTS equipment;",
    "DROP TABLE IF EXISTS user;",
    "DROP TABLE IF EXISTS materials;",
    
    """CREATE TABLE user(
        id INT PRIMARY KEY AUTO_INCREMENT,
        username VARCHAR(25) UNIQUE NOT NULL,
        password VARCHAR(110) NOT NULL
        );
    """,
    """CREATE TABLE materials(
        id INT PRIMARY KEY AUTO_INCREMENT,
        cable_hadmi INT NOT NULL DEFAULT 0,
        cable_rca INT NOT NULL DEFAULT 0,
        spliter_two INT NOT NULL DEFAULT 0,
        spliter_three INT NOT NULL DEFAULT 0,
        remote_control INT NOT NULL DEFAULT 0,
        connector_int INT NOT NULL DEFAULT 0,
        connector_ext INT NOT NULL DEFAULT 0,
        power_supply INT NOT NULL DEFAULT 0,
        q_span INT NOT NULL DEFAULT 0,
        cp_black INT NOT NULL DEFAULT 0,
        sp_black INT NOT NULL DEFAULT 0,
        sp_withe INT NOT NULL DEFAULT 0,
        satellite_dish INT NOT NULL DEFAULT 0,
        lnb INT NOT NULL DEFAULT 0
    );
    """,
    """CREATE TABLE equipment(
        id INT PRIMARY KEY AUTO_INCREMENT,
        name VARCHAR(20) NOT NULL
    );
    """,
    """CREATE TABLE serials(
        id INT PRIMARY KEY AUTO_INCREMENT,
        cm_mac VARCHAR(30) NOT NULL,
        cm_mac_two VARCHAR(30) NOT NULL DEFAULT 0,
        card_number INT NOT NULL DEFAULT 0,
        create_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
        equipment_id INT NOT NULL
    );
    """,
    """ALTER TABLE serials
        ADD CONSTRAINT 
        serials_equipment_id_equipment_id FOREIGN KEY(equipment_id)
        REFERENCES equipment(id);
    """
]
