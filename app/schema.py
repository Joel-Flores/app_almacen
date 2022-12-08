instrutions = [
    "DROP TABLE IF EXISTS technical_material;",
    "DROP TABLE IF EXISTS code_works;",
    "DROP TABLE IF EXISTS user_staff;",
    "DROP TABLE IF EXISTS work_orders;",
    "DROP TABLE IF EXISTS serials;",
    "DROP TABLE IF EXISTS equipment;",
    "DROP TABLE IF EXISTS user;",
    "DROP TABLE IF EXISTS materials;",
    "DROP TABLE IF EXISTS staff;",
    "DROP TABLE IF EXISTS positions;",
    "DROP TABLE IF EXISTS codes;",
    
    """CREATE TABLE user(
        id INT PRIMARY KEY AUTO_INCREMENT,
        nickname VARCHAR(25) UNIQUE NOT NULL,
        password VARCHAR(110) NOT NULL
        );
    """,
    """CREATE TABLE positions(
        id INT PRIMARY KEY AUTO_INCREMENT,
        position VARCHAR (15) NOT NULL
    )
    """,
    """CREATE TABLE staff(
        id INT PRIMARY KEY AUTO_INCREMENT,
        user_name VARCHAR(15) NOT NULL,
        user_name_two VARCHAR(15) DEFAULT "None",
        user_lastname VARCHAR(15) NOT NULL,
        user_lastname_two VARCHAR(15) DEFAULT "None",
        positions_id INT NOT NULL,
        create_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
    );
    """,
    """ALTER TABLE staff
        ADD CONSTRAINT
        staff_positions_id_positions_id FOREIGN KEY(positions_id)
        REFERENCES positions(id);
    """,
    """CREATE TABLE user_staff(
        id INT PRIMARY KEY AUTO_INCREMENT,
        user_id INT NOT NULL,
        staff_id INT NOT NULL
    );
    """,
    """ALTER TABLE user_staff
        ADD CONSTRAINT
        user_staff_user_id_user_id FOREIGN KEY(user_id)
        REFERENCES user(id);
    """,
    """ALTER TABLE user_staff
        ADD CONSTRAINT
        user_staff_staff_id_staff_id FOREIGN KEY(staff_id)
        REFERENCES staff(id);
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
    """,
    """CREATE TABLE technical_material(
        id INT PRIMARY KEY AUTO_INCREMENT,
        technical_id INT NOT NULL,
        materials_id INT NOT NULL,
        serials_id INT NOT NULL,
        create_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
    );
    """,
    """ALTER TABLE technical_material
        ADD CONSTRAINT 
        technical_material_technical_id_staff_id FOREIGN KEY(technical_id)
        REFERENCES staff(id);
    """,
    """ALTER TABLE technical_material
        ADD CONSTRAINT 
        technical_material_materials_id_materials_id FOREIGN KEY(materials_id)
        REFERENCES materials(id);
    """,
    """ALTER TABLE technical_material
        ADD CONSTRAINT 
        technical_material_serials_id_serials_id FOREIGN KEY(serials_id)
        REFERENCES serials(id);
    """,
    """CREATE TABLE codes(
        id INT PRIMARY KEY AUTO_INCREMENT,
        code INT NOT NULL
    );
    """,
    """CREATE TABLE work_orders(
        id INT PRIMARY KEY AUTO_INCREMENT,
        work_order INT NOT NULL,
        serials_id INT NOT NULL,
        materials_id INT DEFAULT 0,
        create_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
    );
    """,
    """CREATE TABLE code_works(
        id INT PRIMARY KEY AUTO_INCREMENT,
        codes_id INT NOT NULL,
        work_orders_id INT NOT NULL,
        create_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
    );
    """,
    """ALTER TABLE code_works
        ADD CONSTRAINT 
        code_workscodes_id_codes_id FOREIGN KEY(codes_id)
        REFERENCES codes(id);
    """,
    """ALTER TABLE code_works
        ADD CONSTRAINT 
        code_works_work_orders_id_work_orders_id FOREIGN KEY(work_orders_id)
        REFERENCES work_orders(id);
    """
]