instrutions = [
    "DROP TABLE IF EXISTS user_staff;",
    "DROP TABLE IF EXISTS technical_material;",
    "DROP TABLE IF EXISTS technical_serial;",
    "DROP TABLE IF EXISTS serials_tech;",
    "DROP TABLE IF EXISTS code_works;",
    "DROP TABLE IF EXISTS staff;",
    "DROP TABLE IF EXISTS work_orders;",
    "DROP TABLE IF EXISTS serials;",
    "DROP TABLE IF EXISTS materials;",
    "DROP TABLE IF EXISTS codes;",
    "DROP TABLE IF EXISTS user;",
    "DROP TABLE IF EXISTS positions;",
    "DROP TABLE IF EXISTS equipment;",
    "DROP TABLE IF EXISTS type_works;",
    
    """CREATE TABLE user(
        id INT PRIMARY KEY AUTO_INCREMENT,
        nickname VARCHAR(25) UNIQUE NOT NULL,
        password VARCHAR(110) NOT NULL,
        active BOOLEAN NOT NULL,
        created_in TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
        );
    """,
    """CREATE TABLE positions(
        id INT PRIMARY KEY AUTO_INCREMENT,
        position VARCHAR (15) NOT NULL,
        created_in TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
    )
    """,
    """CREATE TABLE staff(
        id INT PRIMARY KEY AUTO_INCREMENT,
        user_name VARCHAR(15) NOT NULL,
        user_name_two VARCHAR(15) DEFAULT "None",
        user_lastname VARCHAR(15) NOT NULL,
        user_lastname_two VARCHAR(15) DEFAULT "None",
        positions_id INT NOT NULL,
        created_in TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
    );
    """,
    """CREATE TABLE user_staff(
        id INT PRIMARY KEY AUTO_INCREMENT,
        user_id INT NOT NULL,
        staff_id INT NOT NULL,
        created_in TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
    );
    """,
    """CREATE TABLE materials(
        id INT PRIMARY KEY AUTO_INCREMENT,
        cable_hdmi INT NOT NULL DEFAULT 0,
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
        lnb INT NOT NULL DEFAULT 0,
        user_id INT NOT NULL,
        created_in TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
    );
    """,
    """CREATE TABLE equipment(
        id INT PRIMARY KEY AUTO_INCREMENT,
        name VARCHAR(20) NOT NULL,
        created_in TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
    );
    """,
    """CREATE TABLE serials(
        id INT PRIMARY KEY AUTO_INCREMENT,
        cm_mac VARCHAR(30) NOT NULL,
        cm_mac_two VARCHAR(30) NOT NULL DEFAULT 0,
        card_number INT NOT NULL DEFAULT 0,
        equipment_id INT NOT NULL,
        user_id INT NOT NULL,
        created_in TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
    );
    """,
    """CREATE TABLE technical_material(
        id INT PRIMARY KEY AUTO_INCREMENT,
        technical_id INT NOT NULL,
        materials_id INT NOT NULL,
        created_in TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
    );
    """,
    """CREATE TABLE technical_serial(
        id INT PRIMARY KEY AUTO_INCREMENT,
        technical_id INT NOT NULL,
        serials_id INT NOT NULL,
        created_in TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
    );
    """,
    """CREATE TABLE codes(
        id BIGINT PRIMARY KEY AUTO_INCREMENT,
        code INT NOT NULL,
        type_works_id INT NOT NULL,
        technical_id INT NOT NULL,
        created_in TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
    );
    """,
    """CREATE TABLE type_works(
        id INT PRIMARY KEY AUTO_INCREMENT,
        type_work VARCHAR(10) NOT NULL,
        created_in TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
    );
    """,
    """CREATE TABLE work_orders(
        id BIGINT PRIMARY KEY AUTO_INCREMENT,
        work_order INT NOT NULL,
        serials_id INT NOT NULL,
        materials_id INT NOT NULL,
        code_id BIGINT NOT NULL,
        technical_id INT NOT NULL,
        created_in TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
    );
    """,
    """CREATE TABLE serials_tech(
        id INT PRIMARY KEY AUTO_INCREMENT,
        cm_mac VARCHAR(30) NOT NULL,
        cm_mac_two VARCHAR(30) NOT NULL DEFAULT 0,
        card_number INT NOT NULL DEFAULT 0,
        equipment_id INT NOT NULL,
        code_id BIGINT NOT NULL,
        work_orders_id BIGINT NOT NULL,
        user_id INT NOT NULL,
        created_in TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
    );
    """,
    
    """ALTER TABLE staff
        ADD CONSTRAINT
        staff_positions_id_positions_id FOREIGN KEY(positions_id)
        REFERENCES positions(id);
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
    """ALTER TABLE materials
        ADD CONSTRAINT
        materials_user_id_user_id FOREIGN KEY(user_id)
        REFERENCES user(id);
    """,
    """ALTER TABLE serials
        ADD CONSTRAINT
        serials_equipment_id_equipment_id FOREIGN KEY(equipment_id)
        REFERENCES equipment(id);
    """,
    """ALTER TABLE serials
        ADD CONSTRAINT
        serials_user_id_user_id FOREIGN KEY(user_id)
        REFERENCES user(id);
    """,
    """ALTER TABLE technical_material
        ADD CONSTRAINT 
        technical_material_technical_id_user_id FOREIGN KEY(technical_id)
        REFERENCES user(id);
    """,
    """ALTER TABLE technical_material
        ADD CONSTRAINT 
        technical_material_materials_id_materials_id FOREIGN KEY(materials_id)
        REFERENCES materials(id);
    """,
    """ALTER TABLE technical_serial
        ADD CONSTRAINT 
        technical_serial_technical_id_user_id FOREIGN KEY(technical_id)
        REFERENCES user(id);
    """,
    """ALTER TABLE technical_serial
        ADD CONSTRAINT 
        technical_serial_serials_id_serials_id FOREIGN KEY(serials_id)
        REFERENCES serials(id);
    """,
    """ALTER TABLE codes
        ADD CONSTRAINT 
        codes_type_works_id_type_works_id FOREIGN KEY(type_works_id)
        REFERENCES type_works(id);
    """,
    """ALTER TABLE codes
        ADD CONSTRAINT 
        codes_technical_id_user_id FOREIGN KEY(technical_id)
        REFERENCES user(id);
    """,
    """ALTER TABLE work_orders
        ADD CONSTRAINT 
        work_orders_serials_id_serials_id FOREIGN KEY(serials_id)
        REFERENCES serials(id);
    """,
    """ALTER TABLE work_orders
        ADD CONSTRAINT 
        work_orders_materials_id_materials_id FOREIGN KEY(materials_id)
        REFERENCES materials(id);
    """,
    """ALTER TABLE work_orders
        ADD CONSTRAINT 
        work_orders_code_id_code_id FOREIGN KEY(code_id)
        REFERENCES codes(id);
    """,
    """ALTER TABLE work_orders
        ADD CONSTRAINT 
        work_orders_technical_id_user_id FOREIGN KEY(technical_id)
        REFERENCES user(id);
    """,
    """ALTER TABLE serials_tech
        ADD CONSTRAINT
        serials_tech_equipment_id_equipment_id FOREIGN KEY(equipment_id)
        REFERENCES equipment(id);
    """,
    """ALTER TABLE serials_tech
        ADD CONSTRAINT
        serials_tech_user_id_user_id FOREIGN KEY(user_id)
        REFERENCES user(id);
    """,
    """ALTER TABLE serials_tech
        ADD CONSTRAINT
        serials_tech_code_id_code_id FOREIGN KEY(code_id)
        REFERENCES codes(id);
    """,
    """ALTER TABLE serials_tech
        ADD CONSTRAINT
        serials_tech_work_orders_id_work_orders_id FOREIGN KEY(work_orders_id)
        REFERENCES work_orders(id);
    """
]