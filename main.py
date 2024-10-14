from fastapi import *
from database.models import *
from sqlalchemy.orm import Session

app = FastAPI()


@app.post("/products/")
async def create_product(name: str, description: str, cost: int, amount: int):
    db = SessionLocal()
    db_product = Product(name=name, description=description, cost=cost, amount=amount)
    db.add(db_product)
    db.commit()
    db.refresh(db_product)
    return db_product


@app.get("/products/{item_id}")
async def read_products(item_id: int):
    db = SessionLocal()
    product = db.query(Product).filter(Product.id == item_id).first()
    return product


@app.put("/products/{product_id}")
async def update_product(product_id: int, name: str, description: str, cost: int, amount: int):
    db = SessionLocal()
    db_product = db.query(Product).filter(Product.id == product_id).first()
    if name is not None:
        db_product.name = name
    if description is not None:
        db_product.description = description
    if cost is not None:
        db_product.cost = cost
    if amount is not None:
        db_product.amount = amount
    db.commit()
    return db_product


@app.delete("/products/{product_id}")
async def delete_product(product_id: int):
    db = SessionLocal()
    db_prod = db.query(Product).filter(Product.id == product_id).first()
    db.delete(db_prod)
    db.commit()
    return {"message": "Product deleted successfully!"}


@app.get("/product/list/")
async def get_list_product():
    db = SessionLocal()
    prod_list = db.query(Product).all()
    return prod_list


@app.get("/filter_products/")
async def get_filter_product(name: str = None, description: str = None,
                             cost: int = None, amount: int = None):
    db = SessionLocal()
    prod_query = db.query(Product)
    if name:
        prod_query = prod_query.filter(Product.name.contains(name))
    if cost:
        prod_query = prod_query.filter(Product.cost == cost)
    if amount:
        prod_query = prod_query.filter(Product.amount == amount)
    products = prod_query.all()
    return products
