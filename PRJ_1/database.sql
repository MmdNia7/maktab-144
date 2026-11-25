-- CREATE TABLE users (
--     id SERIAL PRIMARY KEY,
--     first_name VARCHAR(100) NOT NULL,
--     last_name VARCHAR(100) NOT NULL,
--     username VARCHAR(100) UNIQUE NOT NULL,
--     password TEXT NOT NULL,
--     is_admin BOOLEAN NOT NULL DEFAULT FALSE
-- );



-- CREATE TABLE airports (
--     id SERIAL PRIMARY KEY,
--     code VARCHAR(10) UNIQUE NOT NULL,
--     name VARCHAR(100) NOT NULL,
--     city VARCHAR(100) NOT NULL,
--     country VARCHAR(100) NOT NULL,
--     latitude NUMERIC(9,6) NOT NULL,
--     longitude NUMERIC(9,6) NOT NULL
-- );


-- CREATE TABLE flights (
--     id SERIAL PRIMARY KEY,
--     flight_number VARCHAR(20),
--     origin_airport VARCHAR(100),
--     destination_airport VARCHAR(100),
--     departure_time TIMESTAMP,
--     arrival_time TIMESTAMP,
--     price NUMERIC(10,2),
--     capacity INTEGER,
--     status VARCHAR(20) DEFAULT 'active'
-- );


-- CREATE TABLE tickets (
--     id SERIAL PRIMARY KEY,
--     username VARCHAR(100),
--     flight_number VARCHAR(20),
--     purchase_time TIMESTAMP,
--     price NUMERIC(10,2)
-- );


-- ALTER TABLE users
-- ADD COLUMN balance NUMERIC(10,2) NOT NULL DEFAULT 0;



-- CREATE TABLE transactions (
--     id SERIAL PRIMARY KEY,
--     user_id INTEGER,
--     amount NUMERIC(10,2),
--     type VARCHAR(20),
--     created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
-- );


-- DELETE FROM users
-- WHERE username = 'ali123';

-- ALTER TABLE flights
-- ADD COLUMN booked_seats INTEGER NOT NULL DEFAULT 0;


-- UPDATE users
-- SET is_admin = TRUE
-- WHERE username = 'mhd0';


-- INSERT INTO airports (code, name, city, country, latitude, longitude)
-- VALUES
-- ('IKA', 'Imam Khomeini Airport', 'Tehran', 'Iran', 35.4161, 51.1522),
-- ('MHD', 'Mashhad International Airport', 'Mashhad', 'Iran', 36.2352, 59.6409),
-- ('TBZ', 'Tabriz International Airport', 'Tabriz', 'Iran', 38.1339, 46.2350)


-- UPDATE airports
-- SET name = 'Mashhad Airport'
-- WHERE code = 'MHD';

-- UPDATE airports
-- SET name = 'Tabriz Airport'
-- WHERE code = 'TBZ';

-- INSERT INTO flights
-- (flight_number, origin_airport, destination_airport, departure_time, arrival_time, price, capacity, status, booked_seats)
-- VALUES
-- ('IR101', 'Imam Khomeini Airport', 'Mashhad Airport',
--  '2026-12-01 08:00', '2026-12-01 09:30', 2500000, 100, 'active', 0),

-- ('IR102', 'Mashhad Airport', 'Imam Khomeini Airport',
--  '2026-12-01 12:00', '2026-12-01 13:30', 2500000, 100, 'active', 0),

-- ('IR103', 'Imam Khomeini Airport', 'Tabriz Airport',
--  '2026-12-02 09:00', '2026-12-02 10:15', 2000000, 90, 'active', 0),

-- ('IR104', 'Tabriz Airport', 'Mashhad Airport',
--  '2026-12-02 14:00', '2026-12-02 15:30', 2200000, 80, 'active', 0),

-- ('IR105', 'Mashhad Airport', 'Tabriz  Airport',
--  '2026-12-03 10:00', '2026-12-03 11:30', 2100000, 80, 'active', 0);


-- UPDATE flights
-- SET price = 80000000
-- WHERE flight_number = 'IR101';

-- UPDATE flights
-- SET price = 7500000
-- WHERE flight_number = 'IR102';

-- UPDATE flights
-- SET price = 9000000
-- WHERE flight_number = 'IR103';

-- UPDATE flights
-- SET price = 11000000
-- WHERE flight_number = 'IR105';

-- UPDATE flights
-- SET price = 10000000
-- WHERE flight_number = 'IR104';

-- UPDATE flights
-- SET destination_airport = 'Tabriz Airport'
-- WHERE flight_number = 'IR105';


-- CREATE TABLE seats (
--     id SERIAL PRIMARY KEY,
--     flight_id INTEGER NOT NULL REFERENCES flights(id),
--     seat_number VARCHAR(10) NOT NULL,
--     seat_class VARCHAR(20) NOT NULL
-- );

-- ALTER TABLE seats
-- ADD CONSTRAINT unique_flight_seat
-- UNIQUE (flight_id, seat_number);


-- INSERT INTO seats (flight_id, seat_number, seat_class)
-- VALUES
-- (1, '1A', 'Economy'),
-- (1, '1B', 'Economy'),
-- (1, '1C', 'Economy'),
-- (1, '2A', 'Business'),
-- (1, '2B', 'Business');

-- INSERT INTO seats (flight_id, seat_number, seat_class)
-- VALUES
-- (2, '1A', 'Economy'),
-- (2, '1B', 'Economy'),
-- (2, '1C', 'Economy'),
-- (2, '2A', 'Business'),
-- (2, '2B', 'Business');

-- ALTER TABLE tickets
-- ADD COLUMN seat_id INTEGER;

-- ALTER TABLE seats
-- ADD COLUMN is_booked BOOLEAN DEFAULT FALSE;

-- ALTER TABLE tickets
-- ADD COLUMN status VARCHAR(20) DEFAULT 'PAID';


-- ALTER TABLE transactions
-- ADD COLUMN description VARCHAR(255);