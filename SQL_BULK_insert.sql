INSERT INTO customer (customer_name, customer_location, customer_email, customer_telephone)
VALUES
    ('John Doe', 'New York, USA', 'john.doe@example.com', '123-456-7890'),
    ('Jane Smith', 'London, UK', 'jane.smith@example.com', '987-654-3210'),
    ('Michael Brown', 'Sydney, Australia', 'michael.brown@example.com', '555-123-4567'),
    ('Sarah Wilson', 'Toronto, Canada', 'sarah.wilson@example.com', '444-555-6666'),
    ('David Lee', 'San Francisco, USA', 'david.lee@example.com', '333-444-5555'),
    ('Emma Johnson', 'Berlin, Germany', 'emma.johnson@example.com', '666-777-8888'),
    ('Lucas Miller', 'Paris, France', 'lucas.miller@example.com', '777-888-9999'),
    ('Olivia Martinez', 'Madrid, Spain', 'olivia.martinez@example.com', '888-999-0000'),
    ('Liam Davis', 'Rome, Italy', 'liam.davis@example.com', '999-000-1111'),
    ('Isabella Garcia', 'Los Angeles, USA', 'isabella.garcia@example.com', '101-112-1314'),
    ('Ethan Robinson', 'Toronto, Canada', 'ethan.robinson@example.com', '131-415-1617'),
    ('Mia Thomas', 'Melbourne, Australia', 'mia.thomas@example.com', '212-223-2345'),
    ('Alexander White', 'New York, USA', 'alexander.white@example.com', '314-151-6171'),
    ('Ava Harris', 'London, UK', 'ava.harris@example.com', '415-161-7181'),
    ('Benjamin Clark', 'Tokyo, Japan', 'benjamin.clark@example.com', '161-718-1920'),
    ('Charlotte Rodriguez', 'Madrid, Spain', 'charlotte.rodriguez@example.com', '202-213-2435'),
    ('Sebastian Walker', 'Paris, France', 'sebastian.walker@example.com', '213-243-2934'),
    ('Amelia Lewis', 'Rome, Italy', 'amelia.lewis@example.com', '324-323-2323'),
    ('Samuel Young', 'Sydney, Australia', 'samuel.young@example.com', '431-432-1234');


INSERT INTO product_category (category_name)
VALUES
    ('Electronics'),
    ('Clothing'),
    ('Groceries'),
    ('Home Appliances'),
    ('Furniture'),
    ('Toys'),
    ('Books'),
    ('Sports Equipment'),
    ('Beauty Products'),
    ('Automotive'),
    ('Health & Wellness'),
    ('Pet Supplies'),
    ('Food & Beverages'),
    ('Office Supplies'),
    ('Garden Tools'),
    ('Outdoor Gear'),
    ('Stationery'),
    ('Musical Instruments'),
    ('Jewelry'),
    ('Kitchenware');

INSERT INTO supplier (supplier_name, supplier_contact_number)
VALUES
    ('ABC Electronics', '123-456-7890'),
    ('Fashion Trends', '234-567-8901'),
    ('Green Grocers', '345-678-9012'),
    ('Home Tech Co.', '456-789-0123'),
    ('Classic Furniture', '567-890-1234'),
    ('Toy World', '678-901-2345'),
    ('Book Haven', '789-012-3456'),
    ('Sports Zone', '890-123-4567'),
    ('Beauty Essence', '901-234-5678'),
    ('Auto Parts Inc.', '012-345-6789'),
    ('Tech Innovations', '123-987-6543'),
    ('Apparel World', '234-876-5432'),
    ('Fresh Farms', '345-765-4321'),
    ('Smart Home Solutions', '456-654-3210'),
    ('Furniture Galaxy', '567-543-2109'),
    ('Toy Kingdom', '678-432-1098'),
    ('Novel Reads', '789-321-0987'),
    ('Fitness Gear', '890-210-9876'),
    ('Luxury Beauty', '901-109-8765'),
    ('Car Parts Supply', '012-098-7654');


INSERT INTO product (serial_no, product_name, product_weight, price_per_unit, product_category_id, product_supplier_id)
VALUES
    ('ELC123', 'Smartphone', 0.2, 699.99, 1, 2),
    ('CLT456', 'T-shirt', 0.3, 19.99, 2, 2),
    ('GRC789', 'Organic Apples', 1.5, 5.99, 3, 3),
    ('HAP101', 'Air Conditioner', 25.5, 399.99, 4, 4),
    ('FUR202', 'Wooden Desk', 20.0, 199.99, 5, 5),
    ('TOY303', 'Lego Set', 1.0, 49.99, 6, 8),
    ('BOOK404', 'Programming 101', 0.7, 29.99, 10, 7),
    ('SPE505', 'Tennis Racket', 1.2, 89.99, 3, 8),
    ('BPR606', 'Lipstick', 0.05, 12.99, 8, 9),
    ('AUT707', 'Car Engine Oil', 5.0, 25.99, 7, 6),
    ('ELC124', 'Laptop', 1.5, 999.99, 1, 2),
    ('CLT457', 'Jeans', 0.6, 39.99, 2, 2),
    ('GRC790', 'Bananas', 1.2, 2.99, 3, 3),
    ('HAP102', 'Washing Machine', 30.0, 499.99, 4, 4),
    ('FUR203', 'Dining Table', 15.0, 299.99, 5, 5),
    ('TOY304', 'Dollhouse', 0.8, 59.99, 6, 8),
    ('BOOK405', 'Data Science Basics', 1.0, 34.99, 10, 7),
    ('SPE506', 'Basketball', 0.9, 29.99, 3, 8),
    ('BPR607', 'Nail Polish', 0.03, 9.99, 8, 9),
    ('AUT708', 'Brake Pads', 3.0, 45.99, 7, 6);


INSERT INTO customer_order (customer_id, order_date)
VALUES
    (1, '2025-01-01 10:30:00'),
    (2, '2025-01-02 11:00:00'),
    (3, '2025-01-03 12:15:00'),
    (4, '2025-01-04 13:30:00'),
    (5, '2025-01-05 14:00:00'),
    (6, '2025-01-06 15:15:00'),
    (7, '2025-01-07 16:00:00'),
    (8, '2025-01-08 17:45:00'),
    (9, '2025-01-09 18:30:00'),
    (10, '2025-01-10 19:00:00'),
    (11, '2025-01-11 20:15:00'),
    (12, '2025-01-12 21:00:00'),
    (13, '2025-01-13 22:30:00'),
    (14, '2025-01-14 23:45:00'),
    (15, '2025-01-15 09:00:00'),
    (16, '2025-01-16 10:30:00');

INSERT INTO customer_order_items (customer_order_id, product_id, request_quantity)
VALUES
    (1, 1, 25), (1, 2, 30), (1, 3, 18),
    (2, 2, 15), (2, 3, 22), (2, 1, 40),
    (3, 1, 10), (3, 3, 50), (3, 2, 8),
    (4, 1, 35), (4, 2, 28), (4, 3, 14),
    (5, 2, 45), (5, 3, 13), (5, 1, 60),
    (6, 3, 20), (6, 1, 55), (6, 2, 33),
    (7, 1, 48), (7, 2, 25), (7, 3, 38),
    (8, 3, 22), (8, 2, 45), (8, 1, 12),
    (9, 1, 37), (9, 2, 20), (9, 3, 52),
    (10, 1, 18), (10, 2, 60), (10, 3, 31),
    (11, 1, 43), (11, 2, 12), (11, 3, 28),
    (12, 1, 24), (12, 3, 35), (12, 2, 50),
    (13, 1, 42), (13, 2, 39), (13, 3, 17),
    (14, 2, 27), (14, 1, 53), (14, 3, 23),
    (15, 1, 29), (15, 3, 21), (15, 2, 13),
    (16, 1, 31), (16, 3, 48), (16, 2, 22);

INSERT INTO inventory_location (aisle_number, bin_location)
VALUES
    ('SM41', 'A-01-01'),
    ('SM41', 'A-01-02'),
    ('SM42', 'A-02-03'),
    ('SM42', 'A-02-04'),
    ('SM43', 'B-01-05'),
    ('SM43', 'B-01-06'),
    ('SM44', 'C-01-07'),
    ('SM44', 'C-01-08'),
    ('SM45', 'D-01-09'),
    ('SM45', 'D-01-10'),
    ('SM46', 'E-01-11'),
    ('SM46', 'E-01-12'),
    ('SM47', 'F-01-13'),
    ('SM47', 'F-01-14'),
    ('SM48', 'G-01-15'),
    ('SM48', 'G-01-16'),
    ('SM49', 'H-01-17'),
    ('SM49', 'H-01-18'),
    ('SM50', 'I-01-19'),
    ('SM50', 'I-01-20');

INSERT INTO inventory (product_id, available_quantity, inventory_status, inventory_location_id)
VALUES
    (1, 100, 1, 1),  -- Product 1, 100 units, Location 1
    (2, 150, 1, 2),  -- Product 2, 150 units, Location 2
    (3, 200, 1, 3),  -- Product 3, 200 units, Location 3
    (4, 50, 1, 4),   -- Product 4, 50 units, Location 4
    (5, 30, 1, 5),   -- Product 5, 30 units, Location 5
    (6, 75, 1, 6),   -- Product 6, 75 units, Location 6
    (7, 120, 1, 7),  -- Product 7, 120 units, Location 7
    (8, 180, 1, 8),  -- Product 8, 180 units, Location 8
    (9, 95, 1, 9),   -- Product 9, 95 units, Location 9
    (10, 65, 1, 10), -- Product 10, 65 units, Location 10
    (11, 140, 1, 11), -- Product 11, 140 units, Location 11
    (12, 110, 1, 12), -- Product 12, 110 units, Location 12
    (13, 250, 1, 13), -- Product 13, 250 units, Location 13
    (14, 90, 1, 14),  -- Product 14, 90 units, Location 14
    (15, 80, 1, 15),  -- Product 15, 80 units, Location 15
    (16, 130, 1, 16), -- Product 16, 130 units, Location 16
    (17, 60, 1, 17),  -- Product 17, 60 units, Location 17
    (18, 200, 1, 18), -- Product 18, 200 units, Location 18
    (19, 170, 1, 19), -- Product 19, 170 units, Location 19
    (20, 90, 1, 20);  -- Product 20, 90 units, Location 20
