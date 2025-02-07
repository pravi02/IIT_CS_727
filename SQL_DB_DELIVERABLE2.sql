--
-- Customer table CRUD statements
--

INSERT INTO customer (customer_name, customer_location, customer_email, customer_telephone)
VALUES ('PR Doe', 'Newark', 'john.doex@example.com', '1234567890');

SELECT * FROM customer;

-- Get a specific customer by ID
SELECT * FROM customer WHERE customer_id = 1;

UPDATE customer
SET customer_name = 'John D.', customer_email = 'john.doex@example.com'
WHERE customer_id = 1;

DELETE FROM customer WHERE customer_id = 1;


--
-- Customer table CRUD statements
--
INSERT INTO product (serial_no, product_name, product_weight, price_per_unit, product_category_id, product_supplier_id)
VALUES ('MNI45', 'Product A', 1.5, 19.99, 1, 1);

SELECT * FROM product;

-- Get a specific product by ID
SELECT * FROM product WHERE product_id = 1;


UPDATE product
SET product_name = 'Product B', price_per_unit = 24.99
WHERE product_id = 1;

DELETE FROM product WHERE product_id = 1;


-- Create a temporary table to store inventory data
CREATE TEMPORARY TABLE temp_inventory (
    product_id INT,
    product_name VARCHAR(100),
    available_quantity INT
);

--
-- Insert data into the temporary table
--
INSERT INTO temp_inventory (product_id, product_name, available_quantity)
SELECT p.product_id, p.product_name, i.available_quantity
FROM product p
JOIN inventory i ON p.product_id = i.product_id
WHERE i.inventory_status = TRUE;

-- Query the temporary table to see the results
SELECT * FROM temp_inventory;

-- Drop the temporary table (optional, as it will be dropped automatically when the session ends)
DROP TEMPORARY TABLE temp_inventory;


--
-- Create a function to calculate total sales for a given order_id
--
DELIMITER //
CREATE FUNCTION get_total_sales(@order_id INT)
RETURNS DECIMAL(10, 2)
AS
BEGIN
    DECLARE total_sales DECIMAL(10, 2);
    
    -- Calculate the total sales for the order by multiplying quantity with product price
    SELECT @total_sales = SUM(customer_order_item.request_quantity * product.price_per_unit)
    FROM customer_order_item
    JOIN product ON customer_order_item.product_id = product.product_id
    WHERE customer_order_item.customer_order_id = @order_id;
    
    -- Return the total sales price
    RETURN @total_sales;
END//
DELIMITER ;

-- Example usage of the function
SELECT get_total_sales(1) AS total_sales;

-- Create a stored procedure to create a new order
DELIMITER //

CREATE PROCEDURE create_new_order(
    IN customer_id INT,
    IN order_date DATETIME,
    IN sales_amount DECIMAL(10, 2),
    IN processed_by INT
)
BEGIN
    -- Insert the new order into the customer_order table
    INSERT INTO customer_order (customer_id, order_date)
    VALUES (customer_id, order_date);

    -- Get the last inserted order_id
    DECLARE new_order_id INT;
    SET new_order_id = LAST_INSERT_ID();

    -- Insert the order process record
    INSERT INTO order_process (transaction_date, sales_amount, processed_by, customer_order_id, order_processed)
    VALUES (order_date, sales_amount, processed_by, new_order_id, FALSE);

    -- Return the new order ID
    SELECT new_order_id AS new_order_id;
END //

DELIMITER ;

-- Example usage of the stored procedure
CALL create_new_order(1, '2025-02-04 12:00:00', 150.75, 1);

--
-- Create the trigger function to update inventory after an order is processed
--

CREATE OR REPLACE FUNCTION update_inventory_after_order_processed()
RETURNS TRIGGER AS $$
BEGIN
    -- Loop through the processed line items for the processed order
    FOR line_item IN
        SELECT product_id, allocated_quantity, inventory_location_id
        FROM processed_line_items
        WHERE process_id = NEW.transaction_id
    LOOP
        -- Update the available_quantity in the inventory
        UPDATE inventory
        SET available_quantity = available_quantity - line_item.allocated_quantity
        WHERE product_id = line_item.product_id
          AND inventory_location_id = line_item.inventory_location_id
          AND available_quantity >= line_item.allocated_quantity;

        -- Optional: If available quantity becomes negative, raise an error
        IF NOT FOUND THEN
            RAISE EXCEPTION 'Not enough inventory for product % at location %', line_item.product_id, line_item.inventory_location_id;
        END IF;
    END LOOP;

    -- Return the NEW row (important for AFTER triggers)
    RETURN NEW;
END;

--
-- Create a view to show order summary
--

CREATE VIEW order_summary AS
SELECT
    op.transaction_id,
    op.transaction_date,
    op.sales_amount,
    c.customer_name,
    c.customer_email,
    string_agg(p.product_name, ', ') AS products_in_order
FROM order_process op
JOIN customer c ON op.customer_order_id = c.customer_id
JOIN processed_line_items pli ON op.transaction_id = pli.process_id
JOIN product p ON pli.product_id = p.product_id
WHERE op.order_processed = TRUE
GROUP BY op.transaction_id, op.transaction_date, op.sales_amount, c.customer_name, c.customer_email;