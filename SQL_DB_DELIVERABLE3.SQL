-- USING WINDOW RANK() TO GET RANK BASED ON TOTAL SALE AMOUNT

SELECT
    customer_id,
    order_date,
    get_total_sales_for_order(order_id) as total_amount,
    RANK() OVER (ORDER BY get_total_sales_for_order(order_id) DESC) AS Amount_rank 		
FROM
    customer_order;



---- USING WINDOW RANK() TO GET RANK BASED ON CUSTOMER ORDER YEAR

SELECT
    customer_id,
    order_date,
    EXTRACT(YEAR FROM order_date) AS order_year,
    RANK() OVER (ORDER BY EXTRACT(YEAR FROM order_date)) AS Year_rank 		
FROM
    customer_order;


---- USING WINDOW DENSE_RANK() TO GET RANK BASED ON CUSTOMER ORDER YEAR

SELECT
    customer_id,
    order_date,
    EXTRACT(YEAR FROM order_date) AS order_year,
    DENSE_RANK() OVER (ORDER BY EXTRACT(YEAR FROM order_date)) AS Year_rank 		
FROM
    customer_order;


---- USING RANK() AND PARTITION TO GET RANK BASED ON YEAR AND TOTAL SALES AMOUNT
SELECT
    customer_id,
    order_date,
    get_total_sales_for_order(order_id) as total_amount,	
    EXTRACT(YEAR FROM order_date) AS order_year,
    EXTRACT(MONTH FROM order_date) AS order_month,
    RANK() OVER (PARTITION BY EXTRACT(YEAR FROM order_date) ORDER BY get_total_sales_for_order(order_id) DESC) AS yearly_rank
FROM
    customer_order;

---- USING ROW_NUMER(), TO GET ORDER BASED ON TOTAL SALES AMOUNT
SELECT
    ROW_NUMBER() OVER (ORDER BY get_total_sales_for_order(order_id)) as row_num1,
    order_id,
    customer_id,
    order_date

FROM
    customer_order;


---- USING DENSE_RANK() AND PARTITION TO GET RANK BASED ON YEAR AND TOTAL SALES AMOUNT
SELECT
    customer_id,
    order_date,
    get_total_sales_for_order(order_id) as total_amount,	
    EXTRACT(YEAR FROM order_date) AS order_year,
    EXTRACT(MONTH FROM order_date) AS order_month,
    DENSE_RANK() OVER (PARTITION BY EXTRACT(YEAR FROM order_date) ORDER BY get_total_sales_for_order(order_id) DESC) AS yearly_rank
FROM
    customer_order;

---- USING PERCENT_RANK()TO GET PERCENT RANK BASED TOTAL SALES AMOUNT
SELECT
    order_id,
    order_date,
    get_total_sales_for_order(order_id) as total_amount,	
    ROUND(PERCENT_RANK() OVER (ORDER BY get_total_sales_for_order(order_id)),2) AS 'total_amount_%_rank',
    ROUND(PERCENT_RANK() OVER (ORDER BY get_total_sales_for_order(order_id))*100,2) AS 'total_amount_%_rank_(%age)'
FROM
    customer_order;

---- USING CUME_DIST() TO GET RANK BASED TOTAL SALES AMOUNT
SELECT
    order_id,
    order_date,
    get_total_sales_for_order(order_id) as total_amount,	
    ROUND(CUME_DIST() OVER (ORDER BY get_total_sales_for_order(order_id)),2) AS 'total_amount_cume_dist',
    ROUND(CUME_DIST() OVER (PARTITION BY EXTRACT(YEAR FROM order_date) ORDER BY get_total_sales_for_order(order_id))*100,2) AS 'total_amount_%_(%cume_dist)'
FROM
    customer_order;

---- USING PARTITION AND CUME_DIST() TO GET DISTRIBUTION VALUES BASED TOTAL SALES AMOUNT BY YEAR
SELECT
    order_id,
    order_date,
    get_total_sales_for_order(order_id) as total_amount,	
    ROUND(CUME_DIST() OVER (ORDER BY get_total_sales_for_order(order_id)),2) AS 'total_amount_cume_dist',
    ROUND(CUME_DIST() OVER (PARTITION BY EXTRACT(YEAR FROM order_date) ORDER BY get_total_sales_for_order(order_id))*100,2) AS 'total_amount_%_(%cume_dist)'
FROM
    customer_order;

---- USING FIRST_VALUE AND PARTITION TO GET FIRST ORDER RECEIVED BY CUSTOMER FOR THAT YEAR
SELECT
    order_id,
    customer_id,
    YEAR(order_date) AS order_year,
    FIRST_VALUE(customer_id) OVER (PARTITION BY YEAR(order_date) ORDER BY order_date) AS first_customer_for_year
FROM
    customer_order
ORDER BY
    order_year, first_customer_for_year;                                                                                                                                                                                                                                                                                                                            


---- USING SUM() TO GET TOTAL SALES AMOUNT IN THE CUSTOMER ORDER
SELECT
    co.order_id,
    SUM(coi.request_quantity * p.price_per_unit) AS total_order_amount
FROM
    customer_order co
JOIN
    customer_order_items coi ON co.order_id = coi.customer_order_id
JOIN
    product p ON coi.product_id = p.product_id
GROUP BY
    co.order_id;

---- USING NTILE() TO GET  GROUP (BUCKETS) FOR TOTAL SALES AMOUNT
SELECT
    order_id,
    customer_id,
    get_total_sales_for_order(order_id) as total_amount,
    NTILE(3) OVER (ORDER BY get_total_sales_for_order(order_id)) AS order_tile3,
    NTILE(4) OVER (ORDER BY get_total_sales_for_order(order_id)) AS order_tile4,
    NTILE(5) OVER (ORDER BY get_total_sales_for_order(order_id)) AS order_tile5
FROM
    customer_order;


---- USING PRECEDING TO GET THE AVERAGE SALES OF PRODUCTS FOR EACH PREVIOUS DAY, ON THAT DAY AND THE NEXT DAY
SELECT
    coi.product_id,
    co.order_date,
    AVG(coi.request_quantity) 
        OVER (
            PARTITION BY coi.product_id
            ORDER BY co.order_date
            ROWS BETWEEN 1 PRECEDING AND 1 FOLLOWING
        ) AS avg_sales
FROM
    customer_order_items coi
JOIN 
    customer_order co ON coi.customer_order_id = co.order_id
ORDER BY
    coi.product_id;

-- RUNNING TOTAL TO GET THE SALES BY PRODUCT CATEGORY FOR PREVIOUS DAY, SAME DAY AND THE NEXT DAY
-- AVG WITH UNBOUNDED PREDEDING
SELECT 
    pc.category_name,
    co.order_date,
    SUM(coi.request_quantity) 
        OVER (
            PARTITION BY coi.product_id
            ORDER BY co.order_date
            ROWS BETWEEN 1 PRECEDING AND 1 FOLLOWING
        ) AS sum_sales,
    AVG(coi.request_quantity) 
        OVER (
            PARTITION BY coi.product_id
            ORDER BY co.order_date
            ROWS UNBOUNDED PRECEDING
        ) AS avg_sales    
FROM
    customer_order_items coi
JOIN 
    customer_order co ON coi.customer_order_id = co.order_id
JOIN
    product p ON coi.product_id = p.product_id
JOIN
    product_category pc ON p.product_category_id = pc.category_id
ORDER BY
    co.order_date;

-- TOTAL PROCESSED INVENTORY FOR LAST 5 DAYS BY PRODUCT CATEGORY AND DATE.
SELECT 
    co.order_date,
    pc.category_name,
    SUM(coi.request_quantity) AS total_quantity,
    SUM(coi.request_quantity * p.price_per_unit) AS total_sales
FROM 
    customer_order_items coi
JOIN 
    customer_order co ON coi.customer_order_id = co.order_id
JOIN 
    product p ON coi.product_id = p.product_id
JOIN 
    product_category pc ON p.product_category_id = pc.category_id
WHERE 
    co.order_date >= CURDATE() - INTERVAL 5 DAY
GROUP BY 
    co.order_date, pc.category_name
ORDER BY 
    co.order_date DESC, pc.category_name;


--OPEN ORDERS BY CUSTOMER WITH TOTAL SALES VALUE (INCLUDING ORDER_STATUS FROM ORDER_PROCESS)
SELECT 
    c.customer_name,
    c.customer_email,
    co.order_id,
    co.order_date,
    get_total_sales(co.order_id) AS total_sales  -- Call the get_total_sales function
FROM 
    customer_order co
JOIN 
    customer c ON co.customer_id = c.customer_id
JOIN 
    customer_order_items coi ON co.order_id = coi.customer_order_id
JOIN 
    product p ON coi.product_id = p.product_id
JOIN 
    order_process op ON co.order_id = op.customer_order_id -- Join with order_process table to get order status
WHERE 
    op.order_processed = 1   -- Filter orders that are processed (order_processed = 1)
ORDER BY 
    co.order_date DESC;


--TOTAL CUSTOMER ORDER VALUE WITH SUBTOTAL AND GRAND TOTAL BY PRODUCT CATEGORY NAME AND DATE
SELECT 
    pc.category_name,
    co.order_date,
    SUM(coi.request_quantity * p.price_per_unit) AS total_order_amount
FROM 
    customer_order co
JOIN 
    customer_order_items coi ON co.order_id = coi.customer_order_id
JOIN 
    product p ON coi.product_id = p.product_id
JOIN 
    product_category pc ON p.product_category_id = pc.category_id
GROUP BY 
    pc.category_name, co.order_date
WITH ROLLUP
ORDER BY 
    pc.category_name desc, co.order_date desc;

SELECT 
    pc.category_name,
    co.order_date,
    get_total_sales(co.order_id)  AS total_order_amount
FROM 
    customer_order co
JOIN 
    customer_order_items coi ON co.order_id = coi.customer_order_id
JOIN 
    product p ON coi.product_id = p.product_id
JOIN 
    product_category pc ON p.product_category_id = pc.category_id
GROUP BY 
    pc.category_name, co.order_date
WITH CUBE
ORDER BY 
    pc.category_name desc, co.order_date desc;
