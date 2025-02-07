--
-- Create database
--
CREATE database IIT_CS727;
use IIT_CS727;

--
-- Create model Product
--


CREATE TABLE `product` 
(`product_id` int NOT NULL PRIMARY KEY AUTO_INCREMENT, 
`serial_no` nvarchar(50) NOT NULL, 
`product_name` nvarchar(50) NOT NULL, 
`product_weight` double precision NOT NULL, 
`price_per_unit` numeric(10, 2) NOT NULL);
--
-- Create model Customer
--
CREATE TABLE `customer` 
(`customer_id` int NOT NULL PRIMARY KEY AUTO_INCREMENT, 
`customer_name` nvarchar(100) NOT NULL, 
`customer_location` nvarchar(100) NOT NULL, 
`customer_email` nvarchar(100) NOT NULL, 
`customer_telephone` nvarchar(20) NOT NULL);
--
-- Create model CustomerOrder
--
CREATE TABLE `customer_order` 
(`order_id` int NOT NULL PRIMARY KEY AUTO_INCREMENT, 
`order_date` datetime(6) NOT NULL, 
`customer_id` int NOT NULL);
--
-- Create model CustomerOrderItems
--
CREATE TABLE `customer_order_items` 
(`line_item_id` int NOT NULL PRIMARY KEY AUTO_INCREMENT, 
`request_quantity` int NOT NULL, 
`customer_order_id` int NOT NULL, 
`product_id` int NOT NULL);
--
-- Create model InventoryLocation
--
CREATE TABLE `inventory_location` 
(`location_id` int NOT NULL PRIMARY KEY AUTO_INCREMENT, 
`aisle_number` nvarchar(50) NOT NULL, 
`bin_location` nvarchar(50) NOT NULL);
--
-- Create model Inventory
--
CREATE TABLE `inventory` 
(`inventory_id` int NOT NULL PRIMARY KEY AUTO_INCREMENT, 
`available_quantity` int NOT NULL, 
`inventory_status` tinyint NOT NULL, 
`inventory_location_id` int NOT NULL, 
`product_id` int NOT NULL);
--
-- Create model OrderProcess
--
CREATE TABLE `order_process` 
(`transaction_id` int NOT NULL PRIMARY KEY AUTO_INCREMENT, 
`transaction_date` date NOT NULL, 
`sales_amount` double precision NOT NULL, 
`order_processed` tinyint NOT NULL, 
`customer_order_id` int NOT NULL UNIQUE, 
`processed_by_id` int NOT NULL);
--
-- Create model ProcessedLineItems
--
CREATE TABLE `processed_line_items` 
(`line_item_id` int NOT NULL PRIMARY KEY AUTO_INCREMENT, 
`allocated_quantity` int NOT NULL, 
`customer_line_item_id` int NOT NULL, 
`inventory_id` int NOT NULL, 
`process_id_id` int NOT NULL);
--
-- Create model ProductCategory
--
CREATE TABLE `product_category` 
(`category_id` int NOT NULL PRIMARY KEY AUTO_INCREMENT, 
`category_name` nvarchar(50) NOT NULL);
--
-- Add field product_category to product
--
ALTER TABLE `product` ADD `product_category_id` int NOT NULL;
--
-- Create model Supplier
--
CREATE TABLE `supplier` 
(`supplier_id` int NOT NULL PRIMARY KEY AUTO_INCREMENT, 
`supplier_name` nvarchar(50) NOT NULL, 
`supplier_contact_number` nvarchar(20) NOT NULL);
--
-- Add field product_supplier to product
--
ALTER TABLE `product` ADD `product_supplier_id` int NOT NULL;
--
-- Alter unique_together for product (1 constraint(s))
--


ALTER TABLE `order_process` ADD CONSTRAINT `order_process_customer_order_id_c6b5bec1_fk_customer_customer_id` FOREIGN KEY (`customer_order_id`) REFERENCES `customer` (`customer_id`);
CREATE INDEX `customer_order_items_customer_order_id_ae2c3fe6` ON `customer_order_items` (`customer_order_id`);
ALTER TABLE `product` ADD CONSTRAINT `product_category_id_1ba01076_fk_product_category_category_id` FOREIGN KEY (`product_category_id`) REFERENCES `product_category` (`category_id`);
ALTER TABLE `inventory` ADD CONSTRAINT `inventory_location_id_7a805a22_fk_inventory_location_id` FOREIGN KEY (`inventory_location_id`) REFERENCES `inventory_location` (`location_id`);
ALTER TABLE `customer_order` ADD CONSTRAINT `customer_order_customer_id_05fff94c_fk_customer_customer_id` FOREIGN KEY (`customer_id`) REFERENCES `customer` (`customer_id`);
CREATE INDEX `customer_order_items_product_id_049dbf42` ON `customer_order_items` (`product_id`);
ALTER TABLE `processed_line_items` ADD CONSTRAINT `processed_line_items_id_3e9ade1e_fk_order_process_transaction_id` FOREIGN KEY (`process_id_id`) REFERENCES `order_process` (`transaction_id`);
CREATE INDEX `product_product_category_id_1ba01076` ON `product` (`product_category_id`);
CREATE INDEX `customer_order_customer_id_05fff94c` ON `customer_order` (`customer_id`);
ALTER TABLE `inventory` ADD CONSTRAINT `inventory_product_id_7c50457a_fk_product_product_id` FOREIGN KEY (`product_id`) REFERENCES `product` (`product_id`);

CREATE INDEX `processed_line_items_customer_line_item_id_544df771` ON `processed_line_items` (`customer_line_item_id`);
CREATE INDEX `order_process_processed_by_id_47fce1d4` ON `order_process` (`processed_by_id`);

CREATE INDEX `processed_line_items_inventory_id_73a2f783` ON `processed_line_items` (`inventory_id`);
ALTER TABLE `customer_order_items` ADD CONSTRAINT `customer_order_id_ae2c3fe6_fk_customer_order_order_id` FOREIGN KEY (`customer_order_id`) REFERENCES `customer_order` (`order_id`);
ALTER TABLE `processed_line_items` ADD CONSTRAINT `customer_line_item_id_544df771_fk_customer_order_items_line_id` FOREIGN KEY (`customer_line_item_id`) REFERENCES `customer_order_items` (`line_item_id`);

CREATE INDEX `inventory_inventory_location_id_7a805a22` ON `inventory` (`inventory_location_id`);

CREATE INDEX `processed_line_items_process_id_id_3e9ade1e` ON `processed_line_items` (`process_id_id`);
ALTER TABLE `customer_order_items` ADD CONSTRAINT `customer_order_items_product_id_049dbf42_fk_product_product_id` FOREIGN KEY (`product_id`) REFERENCES `product` (`product_id`);
CREATE INDEX `inventory_product_id_7c50457a` ON `inventory` (`product_id`);
ALTER TABLE `processed_line_items` ADD CONSTRAINT `processed_line_items_id_73a2f783_fk_inventory_inventory_id` FOREIGN KEY (`inventory_id`) REFERENCES `inventory` (`inventory_id`);
CREATE INDEX `product_product_supplier_id_4a91fe9b` ON `product` (`product_supplier_id`);
ALTER TABLE `product` ADD CONSTRAINT `product_product_supplier_id_4a91fe9b_fk_supplier_supplier_id` FOREIGN KEY (`product_supplier_id`) REFERENCES `supplier` (`supplier_id`);
ALTER TABLE inventory ADD COLUMN reorder_trigger_quantity INT DEFAULT 10;

-- ALTER TABLE `order_process` ADD CONSTRAINT `order_process_processed_by_id_47fce1d4_fk_auth_user_id` FOREIGN KEY (`processed_by_id`) REFERENCES `auth_user` (`id`);

-- CREATE UNIQUE INDEX `product_product_name_product_category_id_85c716ab_uniq` ON `product` (`product_name`, `product_category_id`) WHERE `product_name` IS NOT NULL AND `product_category_id` IS NOT NULL;
-- CREATE UNIQUE INDEX `supplier_supplier_name_supplier_contact_number_05b4eb27_uniq` ON `supplier` (`supplier_name`, `supplier_contact_number`) WHERE `supplier_name` IS NOT NULL AND `supplier_contact_number` IS NOT NULL;
-- CREATE UNIQUE INDEX `inventory_location_aisle_number_bin_location_caf8ae9b_uniq` ON `inventory_location` (`aisle_number`, `bin_location`) WHERE `aisle_number` IS NOT NULL AND `bin_location` IS NOT NULL;
-- CREATE UNIQUE INDEX `product_category_category_name_670b01bc_uniq` ON `product_category` (`category_name`) WHERE `category_name` IS NOT NULL;
-- CREATE UNIQUE INDEX `inventory_product_id_inventory_location_id_fe2b657c_uniq` ON `inventory` (`product_id`, `inventory_location_id`) WHERE `product_id` IS NOT NULL AND `inventory_location_id` IS NOT NULL;
-- CREATE UNIQUE INDEX `customer_customer_name_customer_location_customer_telephone_1e2ef099_uniq` ON `customer` (`customer_name`, `customer_location`, `customer_telephone`) WHERE `customer_name` IS NOT NULL AND `customer_location` IS NOT NULL AND `customer_telephone` IS NOT NULL;

