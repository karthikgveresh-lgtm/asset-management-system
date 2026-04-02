-- =========================
-- DATABASE: AssetTrackr
-- =========================

CREATE DATABASE IF NOT EXISTS assettrackr;
USE assettrackr;

-- Drop tables if exist
DROP TABLE IF EXISTS asset_assignments;
DROP TABLE IF EXISTS assets;
DROP TABLE IF EXISTS employees;
DROP TABLE IF EXISTS hr_admins;

-- =========================
-- TABLE: Employees
-- =========================
CREATE TABLE employees (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100),
    email VARCHAR(100),
    department VARCHAR(50),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- =========================
-- TABLE: HR/Admins
-- =========================
CREATE TABLE hr_admins (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100),
    email VARCHAR(100),
    role VARCHAR(50),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- =========================
-- TABLE: Assets
-- =========================
CREATE TABLE assets (
    id INT AUTO_INCREMENT PRIMARY KEY,
    asset_name VARCHAR(100),
    asset_type VARCHAR(50),
    serial_number VARCHAR(100),
    status VARCHAR(20),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- =========================
-- TABLE: Asset Assignments
-- =========================
CREATE TABLE asset_assignments (
    id INT AUTO_INCREMENT PRIMARY KEY,
    asset_id INT,
    employee_id INT,
    assigned_date DATE,
    return_date DATE,
    status VARCHAR(20)
);

-- =========================
-- INSERT DUMMY DATA
-- =========================

INSERT INTO employees (name, email, department) VALUES
('Karthik', 'karthik@gmail.com', 'Engineering'),
('Rahul', 'rahul@gmail.com', 'HR'),
('Sneha', 'sneha@gmail.com', 'Finance'),
('Amit', 'amit@gmail.com', 'Engineering');

INSERT INTO hr_admins (name, email, role) VALUES
('Priya HR', 'priya@company.com', 'HR Manager'),
('Arjun HR', 'arjun@company.com', 'HR Executive');

INSERT INTO assets (asset_name, asset_type, serial_number, status) VALUES
('Dell Laptop', 'Laptop', 'DL12345', 'Assigned'),
('iPhone 13', 'Mobile', 'IP67890', 'Available'),
('HP Laptop', 'Laptop', 'HP54321', 'Assigned'),
('Office Chair', 'Furniture', 'CH11223', 'Available');

INSERT INTO asset_assignments (asset_id, employee_id, assigned_date, return_date, status) VALUES
(1, 1, '2026-04-01', NULL, 'Active'),
(3, 2, '2026-03-20', NULL, 'Active');