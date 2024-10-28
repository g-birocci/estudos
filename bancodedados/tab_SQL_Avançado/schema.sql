CREATE TABLE IF NOT EXISTS customers (
    "customer_id" INTEGER,
    "customer_name" TEXT NOT NULL,
    "customer_email" TEXT UNIQUE,
    "customer_address" TEXT NOT NULL,
    "customer_phone_number" NUMERIC UNIQUE NOT NULL,
    "customer_date_of_birth" DATE
    PRIMARY KEY ("id")
);

CREATE TABLE IF NOT EXISTS sales (
    "custumer_id" FOREIGN KEY,
    "product_id" FOREIGN KEY,
    "sale_date" DATE,
    "sale_price" NUMERIC NOT NULL
)

CREATE TABLE IF NOT EXI
