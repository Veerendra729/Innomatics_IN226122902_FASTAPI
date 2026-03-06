from fastapi import FastAPI

app = FastAPI()

# initial product list
products = [
    {"id":1, "name":"Wireless Mouse", "price":799, "category":"Electronics", "in_stock":True},
    {"id":2, "name":"Notebook", "price":99, "category":"Stationery", "in_stock":True},
    {"id":3, "name":"Pen Set", "price":49, "category":"Stationery", "in_stock":True},
    {"id":4, "name":"USB Cable", "price":199, "category":"Electronics", "in_stock":False},

    # Q1 Added products
    {"id":5, "name":"Laptop Stand", "price":1299, "category":"Electronics", "in_stock":True},
    {"id":6, "name":"Mechanical Keyboard", "price":2499, "category":"Electronics", "in_stock":True},
    {"id":7, "name":"Webcam", "price":1899, "category":"Electronics", "in_stock":False},
]

@app.get("/products")
def get_products():
    return {
        "products": products,
        "total": len(products)
    }

@app.get("/products/category/{category_name}")
def get_products_by_category(category_name: str):

    filtered_products = []

    for product in products:
        if product["category"] == category_name:
            filtered_products.append(product)

    if len(filtered_products) == 0:
        return {"error": "No products found in this category"}

    return {
        "category": category_name,
        "products": filtered_products,
        "total": len(filtered_products)
    }

@app.get("/products/instock")
def get_instock_products():

    available_products = []

    for product in products:
        if product["in_stock"] == True:
            available_products.append(product)

    return {
        "in_stock_products": available_products,
        "count": len(available_products)
    }

@app.get("/store/summary")
def get_store_summary():

    total_products = len(products)

    in_stock_count = 0

    for product in products:
        if product["in_stock"] == True:
            in_stock_count += 1

    out_of_stock_count = total_products - in_stock_count

    categories = []

    for product in products:
        if product["category"] not in categories:
            categories.append(product["category"])

    return {
        "store_name": "My E-commerce Store",
        "total_products": total_products,
        "in_stock": in_stock_count,
        "out_of_stock": out_of_stock_count,
        "categories": categories
    }

@app.get("/products/search/{keyword}")
def search_products(keyword: str):

    matched_products = []

    for product in products:
        product_name = product["name"].lower()
        search_word = keyword.lower()

        if search_word in product_name:
            matched_products.append(product)

    if len(matched_products) == 0:
        return {"message": "No products matched your search"}

    return {
        "keyword": keyword,
        "results": matched_products,
        "total_matches": len(matched_products)
    }

@app.get("/products/deals")
def get_best_deals():

    cheapest_product = products[0]
    expensive_product = products[0]

    for product in products:

        if product["price"] < cheapest_product["price"]:
            cheapest_product = product

        if product["price"] > expensive_product["price"]:
            expensive_product = product

    return {
        "best_deal": cheapest_product,
        "premium_pick": expensive_product
    }