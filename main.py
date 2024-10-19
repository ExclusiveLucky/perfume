from fastapi import FastAPI, Depends
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from fastapi.requests import Request
from sqlalchemy.orm import Session
from database import get_db
from models import Product

app = FastAPI()

templates = Jinja2Templates(directory="templates")
app.mount("/static", StaticFiles(directory="static"), name="static")
app.mount("/images", StaticFiles(directory="images"), name="images")

@app.get("/")
def read_root():
    return {"message": "Hello world!"}

@app.get("/products")
def show_products(request: Request, db: Session = Depends(get_db)):
    products = db.query(Product).all()
    return templates.TemplateResponse("products.html", {"request": request, "products": products})

@app.get("/products/{product_id}")
def show_product_detail(product_id: int, request: Request, db: Session = Depends(get_db)):
    product = db.query(Product).filter(Product.id == product_id).first()
    if not product:
        return {"error": "Product not found"}
    
    return templates.TemplateResponse("product_detail.html", {"request": request, "product": product})


@app.get("/categories")
def show_products(request: Request, db: Session = Depends(get_db)):
    return templates.TemplateResponse("categories.html", {"request": request})

@app.get("/deals")
def show_products(request: Request, db: Session = Depends(get_db)):
    return templates.TemplateResponse("deals.html", {"request": request})

@app.get("/search")
def show_products(request: Request, db: Session = Depends(get_db)):
    return templates.TemplateResponse("search.html", {"request": request})


@app.get("/contacts")
def show_products(request: Request, db: Session = Depends(get_db)):
    return templates.TemplateResponse("contacts.html", {"request": request})
