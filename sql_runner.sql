-- DELIMITER //

-- CREATE FUNCTION get_total_sales_for_order(order_id INT)
-- RETURNS DECIMAL(10, 2)
-- DETERMINISTIC
-- BEGIN
--     DECLARE total_sales DECIMAL(10, 2);
    
--     -- Calculate the total sales for the order by multiplying quantity with product price
--     SELECT SUM(customer_order_items.request_quantity * product.price_per_unit) INTO total_sales
--     FROM customer_order_items
--     JOIN product ON customer_order_items.product_id = product.product_id
--     WHERE customer_order_items.customer_order_id = order_id;
    
--     -- Return the total sales price
--     RETURN total_sales;
-- END //

-- DELIMITER ;

-- DELIMITER //

-- CREATE FUNCTION get_total_sales_for_order(order_id INT)
-- RETURNS DECIMAL(10, 2)
-- DETERMINISTIC
-- BEGIN
--     DECLARE total_sales DECIMAL(10, 2);
    
--     -- Calculate the total sales for the order by multiplying quantity with product price
--     SELECT SUM(coi.request_quantity * p.price_per_unit) INTO total_sales
--     FROM customer_order_items coi
--     JOIN product p ON coi.product_id = p.product_id
--     WHERE coi.customer_order_id = order_id;
    
--     -- Return the total sales price
--     RETURN total_sales;
-- END //

-- DELIMITER ;

-- DELIMITER //

-- CREATE PROCEDURE update_inventory_after_order(IN order_id INT)
-- BEGIN
--     DECLARE done INT DEFAULT 0;
--     DECLARE product_id INT;
--     DECLARE requested_quantity INT;
    
--     -- Declare a cursor for looping through the order items
--     DECLARE cur CURSOR FOR 
--         SELECT product_id, request_quantity
--         FROM customer_order_items  -- Updated table name here
--         WHERE customer_order_id = order_id;
    
--     -- Declare a handler to set 'done' when the cursor finishes
--     DECLARE CONTINUE HANDLER FOR NOT FOUND SET done = 1;

--     -- Open the cursor to iterate through the order items
--     OPEN cur;

--     -- Loop through the order items
--     read_loop: LOOP
--         FETCH cur INTO product_id, requested_quantity;
        
--         IF done THEN
--             LEAVE read_loop;
--         END IF;
        
--         -- Update the inventory based on the requested quantity
--         UPDATE inventory
--         SET available_quantity = available_quantity - requested_quantity
--         WHERE product_id = product_id;
        
--     END LOOP;

--     -- Close the cursor
--     CLOSE cur;
-- END //

-- DELIMITER ;


    -- DELIMITER //

    -- CREATE TRIGGER update_inventory_status_after_update
    -- AFTER UPDATE ON inventory
    -- FOR EACH ROW
    -- BEGIN
    --     -- Check if the available_quantity has fallen below or equal to the minimum_trigger_quantity
    --     IF NEW.available_quantity <= NEW.reorder_trigger_quantity THEN
    --         -- Update inventory_status to FALSE
    --         UPDATE inventory
    --         SET inventory_status = FALSE
    --         WHERE inventory_id = NEW.inventory_id;
    --     END IF;
    -- END //

    -- DELIMITER ;

CREATE VIEW order_summary_view AS
SELECT 
    co.order_id,
    c.customer_name,
    c.customer_email,
    co.order_date,
    p.product_name,
    coi.request_quantity,
    p.price_per_unit,
    (coi.request_quantity * p.price_per_unit) AS total_price
FROM 
    customer_order co
JOIN 
    customer_order_items coi ON co.order_id = coi.customer_order_id
JOIN 
    product p ON coi.product_id = p.product_id
JOIN 
    customer c ON co.customer_id = c.customer_id;


CREATE TEMPORARY TABLE order_summary_temp AS
SELECT 
    co.customer_order_id,
    c.customer_name,
    c.customer_email,
    co.order_date,
    p.product_name,
    coi.request_quantity,
    p.price_per_unit,
    (coi.request_quantity * p.price_per_unit) AS total_price
FROM 
    customer_order co
JOIN 
    customer_order_item coi ON co.customer_order_id = coi.customer_order_id
JOIN 
    product p ON coi.product_id = p.product_id
JOIN 
    customer c ON co.customer_id = c.customer_id
WHERE 
    co.customer_order_id = 123;