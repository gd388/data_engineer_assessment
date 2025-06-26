CREATE DATABASE IF NOT EXISTS home_db;
USE home_db;


-- Drop if already exists
DROP TABLE IF EXISTS taxes, rehab, hoa, valuation, leads, property;

-- Main Property Table
CREATE TABLE property (
    property_id INT AUTO_INCREMENT PRIMARY KEY,
    title VARCHAR(255),
    address VARCHAR(255),
    street_address VARCHAR(255),
    city VARCHAR(100),
    state VARCHAR(100),
    zip VARCHAR(20),
    market VARCHAR(100),
    flood VARCHAR(50),
    property_type VARCHAR(100),
    highway VARCHAR(100),
    train VARCHAR(100),
    tax_rate DECIMAL(10, 2),
    sqft_basement INT,
    htw VARCHAR(50),
    pool VARCHAR(50),
    commercial VARCHAR(50),
    water VARCHAR(50),
    sewage VARCHAR(50),
    year_built INT,
    sqft_mu INT,
    sqft_total INT,
    parking VARCHAR(100),
    bed INT,
    bath INT,
    basement_yes_no VARCHAR(10),
    layout VARCHAR(100),
    rent_restricted VARCHAR(10),
    neighborhood_rating DECIMAL(5,2),
    latitude DECIMAL(10,6),
    longitude DECIMAL(10,6),
    subdivision VARCHAR(100),
    school_average DECIMAL(5,2),
    UNIQUE(address, zip)
);

-- Leads Table
CREATE TABLE leads (
    lead_id INT AUTO_INCREMENT PRIMARY KEY,
    property_id INT,
    reviewed_status VARCHAR(100),
    most_recent_status VARCHAR(100),
    occupancy VARCHAR(100),
    net_yield DECIMAL(6, 2),
    irr DECIMAL(6, 2),
    selling_reason VARCHAR(255),
    seller_retained_broker VARCHAR(255),
    final_reviewer VARCHAR(255),
    source VARCHAR(100),
    FOREIGN KEY (property_id) REFERENCES property(property_id)
);

-- Valuation Table
CREATE TABLE valuation (
    valuation_id INT AUTO_INCREMENT PRIMARY KEY,
    property_id INT,
    previous_rent DECIMAL(10, 2),
    list_price DECIMAL(12, 2),
    zestimate DECIMAL(12, 2),
    arv DECIMAL(12, 2),
    expected_rent DECIMAL(10, 2),
    rent_zestimate DECIMAL(10, 2),
    low_fmr DECIMAL(10, 2),
    high_fmr DECIMAL(10, 2),
    redfin_value DECIMAL(12, 2),
    FOREIGN KEY (property_id) REFERENCES property(property_id)
);

-- HOA Table
CREATE TABLE hoa (
    hoa_id INT AUTO_INCREMENT PRIMARY KEY,
    property_id INT,
    hoa_amount DECIMAL(10, 2),
    hoa_flag VARCHAR(10),
    FOREIGN KEY (property_id) REFERENCES property(property_id)
);

-- Rehab Table
CREATE TABLE rehab (
    rehab_id INT AUTO_INCREMENT PRIMARY KEY,
    property_id INT,
    underwriting_rehab DECIMAL(10, 2),
    rehab_calculation VARCHAR(255),
    paint_flag BOOLEAN,
    flooring_flag BOOLEAN,
    foundation_flag BOOLEAN,
    roof_flag BOOLEAN,
    hvac_flag BOOLEAN,
    kitchen_flag BOOLEAN,
    bathroom_flag BOOLEAN,
    appliances_flag BOOLEAN,
    windows_flag BOOLEAN,
    landscaping_flag BOOLEAN,
    trashout_flag BOOLEAN,
    FOREIGN KEY (property_id) REFERENCES property(property_id)
);

-- Taxes Table
CREATE TABLE taxes (
    tax_id INT AUTO_INCREMENT PRIMARY KEY,
    property_id INT,
    taxes_amount DECIMAL(10, 2),
    FOREIGN KEY (property_id) REFERENCES property(property_id)
);


ALTER USER 'db_user'@'%' IDENTIFIED WITH mysql_native_password BY '6equj5_db_user';
FLUSH PRIVILEGES;
