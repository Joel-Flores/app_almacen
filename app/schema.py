instrutions = [
    "DROP TABLE IF EXISTS codes;",
    "DROP TABLE IF EXISTS zones;",
    "DROP TABLE IF EXISTS citys;",
    """
    CREATE TABLE citys(
        id INT PRIMARY KEY AUTO_INCREMENT NOT NULL,
        city VARCHAR(20) NOT NULL
        );
    """,
    """
    CREATE TABLE zones(
        id INT PRIMARY KEY AUTO_INCREMENT NOT NULL,
        zone VARCHAR(20) NOT NULL,
        city_id INT NOT NULL
        );
    """,
    """
    CREATE TABLE codes(
        id INT PRIMARY KEY
        AUTO_INCREMENT NOT NULL,
        code INT NOT NULL,
        user_name VARCHAR(50) NOT NULL DEFAULT 0,
        tab VARCHAR(10) NOT NULL DEFAULT 0,
        ramal VARCHAR(10)NOT NULL DEFAULT 0,
        georeference VARCHAR(25) NOT NULL DEFAULT 0,
        maps VARCHAR(100) NOT NULL DEFAULT 0,
        committed_reused INT NOT NULL DEFAULT 0,
        images VARCHAR(50),
        zone_id INT NOT NULL
        );
    """,
    """
    ALTER TABLE codes
        ADD CONSTRAINT
        codes_zone_id_zones_id FOREIGN KEY(zone_id)
        REFERENCES zones(id);
    """,
    """
    ALTER TABLE zones
        ADD CONSTRAINT
        zones_city_id_citys_id FOREIGN KEY(city_id)
        REFERENCES citys(id);
    """
]
