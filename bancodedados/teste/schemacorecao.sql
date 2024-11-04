CREATE TABLE IF NOT EXISTS "categories" (
	"id" INTEGER NOT NULL UNIQUE,
	"name" TEXT,
	PRIMARY KEY("id")
);

CREATE TABLE IF NOT EXISTS "products" (
	"id" INTEGER NOT NULL UNIQUE,
	"name" TEXT,
	"description" TEXT,
	"price" REAL,
	"category_id" INTEGER,
	PRIMARY KEY("id"),
	FOREIGN KEY ("category_id") REFERENCES "categories"("id")
	ON UPDATE NO ACTION ON DELETE SET NULL
);

CREATE TABLE IF NOT EXISTS "phone_cases" (
	"id" INTEGER NOT NULL UNIQUE,
	"product_id" INTEGER UNIQUE,
	"material" TEXT,
	"color" TEXT,
	"compatible_models" TEXT,
	PRIMARY KEY("id"),
	FOREIGN KEY ("product_id") REFERENCES "products"("id")
	ON UPDATE CASCADE ON DELETE CASCADE
);

CREATE TABLE IF NOT EXISTS "chargers" (
	"id" INTEGER NOT NULL UNIQUE,
	"product_id" INTEGER UNIQUE,
	"type" TEXT, -- Exemplo: "wireless", "USB-C", "micro-USB"
	"power_output" REAL, -- Em watts (W)
	"cable_length" REAL, -- Em metros (opcional)
	PRIMARY KEY("id"),
	FOREIGN KEY ("product_id") REFERENCES "products"("id")
	ON UPDATE CASCADE ON DELETE CASCADE
);

CREATE TABLE IF NOT EXISTS "customers" (
	"id" INTEGER NOT NULL UNIQUE,
	"name" TEXT,
	"address" TEXT,
	"email" TEXT,
	"phone" TEXT,
	PRIMARY KEY("id")
);

CREATE TABLE IF NOT EXISTS "orders" (
	"id" INTEGER NOT NULL UNIQUE,
	"date" TEXT,
	"customer_id" INTEGER,
	"amount" INTEGER,
	"status" TEXT CHECK("status" in ('delivered', 'received', 'processing')),
	"product_id" INTEGER,
	PRIMARY KEY("id"),
	FOREIGN KEY ("product_id") REFERENCES "products"("id")
	ON UPDATE CASCADE ON DELETE SET NULL,
	FOREIGN KEY ("customer_id") REFERENCES "customers"("id")
	ON UPDATE CASCADE ON DELETE CASCADE
);

CREATE TABLE IF NOT EXISTS "reviews" (
	"id" INTEGER NOT NULL UNIQUE,
	"customer_id" INTEGER,
	"product_id" INTEGER,
	"rating" INTEGER CHECK("rating" BETWEEN 1 AND 5),
	"content" TEXT,
	"date" TEXT,
	PRIMARY KEY("id"),
	FOREIGN KEY ("customer_id") REFERENCES "customers"("id")
	ON UPDATE CASCADE ON DELETE CASCADE,
	FOREIGN KEY ("product_id") REFERENCES "products"("id")
	ON UPDATE CASCADE ON DELETE CASCADE
);
