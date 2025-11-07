from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from database import SessionLocal, engine
import models, schemas, crud

models.Base.metadata.create_all(bind=engine)
app=FastAPI(title="Media Store System")

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/customer", response_model=schemas.CustomerResponse)
def create_customer(customer: schemas.CustomerCreate, db: Session = Depends(get_db)):
    return crud.create_customer(db, customer)

@app.get("/customer", response_model=list[schemas.CustomerResponse])
def get_all_customers(db: Session = Depends(get_db)):
    customers = crud.get_all_customers(db)
    if not customers:
        raise HTTPException(status_code=404, detail="There is no customer")
    return customers


@app.get("/customer/{customer_id}", response_model=schemas.CustomerResponse)
def get_customer(customer_id: int, db: Session = Depends(get_db)):
    customer = crud.get_customer(db, customer_id)
    if not customer:
        raise HTTPException(status_code=404, detail="Customer not found")
    return customer

@app.delete("/customer/{customer_id}")
def delete_customer(customer_id: int, db: Session = Depends(get_db)):
    deleted = crud.delete_customer(db, customer_id)
    if not deleted:
        return {"error": "Customer not found"}
    return {"message": "Customer deleted successfully"}

@app.post("/media", response_model=schemas.MediaResponse)
def create_media(media: schemas.MediaCreate, db: Session = Depends(get_db)):
    return crud.create_media(db, media)

@app.put("/media/{media_id}")
def update_media(media_id: int, media: schemas.MediaUpdate, db: Session = Depends(get_db)):
    updated = crud.update_media(db, media_id, media)
    if not updated:
        return {"error": "Media not found"}
    return {"message": "Media updated successfully"}

@app.get("/media", response_model=list[schemas.MediaResponse])
def get_all_media(db: Session = Depends(get_db)):
    m = crud.get_all_media(db)
    if not m:
        raise HTTPException(status_code=404, detail="There is no media")
    return m

@app.get("/media/{media_id}", response_model=schemas.MediaResponse)
def get_media(media_id: int, db: Session = Depends(get_db)):
    m = crud.get_media(db, media_id)
    if not m:
        raise HTTPException(status_code=404, detail="Media not found")
    return m

@app.delete("/media/{media_id}")
def delete_media(media_id: int, db: Session = Depends(get_db)):
    deleted = crud.delete_media(db, media_id)
    if not deleted:
        return {"error": "Media not found"}
    return {"message": "Media deleted successfully"}
