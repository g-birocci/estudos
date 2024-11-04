CREATE TABLE IF NOT EXISTS "products" (
	"id" INTEGER NOT NULL UNIQUE,
	"name" TEXT,
	"description" TEXT,
	"price" REAL,
	"category_id" INTEGER,
	PRIMARY KEY("id"),
	FOREIGN KEY ("category_id") REFERENCES "categories"("id")
	ON UPDATE NO ACTION ON DELETE NO ACTION
);

CREATE TABLE IF NOT EXISTS "categories" (
	"id" INTEGER NOT NULL UNIQUE,
	"name" TEXT,
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
	ON UPDATE NO ACTION ON DELETE NO ACTION,
	FOREIGN KEY ("customer_id") REFERENCES "customers"("id")
	ON UPDATE NO ACTION ON DELETE NO ACTION
);

CREATE TABLE IF NOT EXISTS "reviews" (
	"id" INTEGER NOT NULL UNIQUE,
	"customer_id" INTEGER,
	"product_id" INTEGER,
	"rating" INTEGER,
	"content" TEXT,
	"date" TEXT,
	PRIMARY KEY("id"),
	FOREIGN KEY ("customer_id") REFERENCES "customers"("id")
	ON UPDATE NO ACTION ON DELETE NO ACTION,
	FOREIGN KEY ("product_id") REFERENCES "products"("id")
	ON UPDATE NO ACTION ON DELETE NO ACTION
);

CREATE TABLE IF NOT EXISTS "customers" (
	"id" INTEGER NOT NULL UNIQUE,
	"name" TEXT,
	"address" TEXT,
	"email" TEXT,
	"phone" TEXT,
	PRIMARY KEY("id")
);
