from sqlalchemy.orm import Session
import models, schemas

def create_customer(db: Session, customer: schemas.CustomerCreate):
    db_customer = models.Customer(**customer.model_dump())
    db.add(db_customer)
    db.commit()
    db.refresh(db_customer)
    return db_customer

def get_all_customers(db: Session):
    return db.query(models.Customer).all()

def get_customer(db: Session, customer_id: int):
    return db.query(models.Customer).filter(models.Customer.id == customer_id).first()

def delete_customer(db: Session, customer_id: int):
    customer = db.query(models.Customer).filter(models.Customer.id == customer_id).first()
    if not customer:
        return False
    db.delete(customer)
    db.commit()
    return True

def create_media(db: Session, media: schemas.MediaCreate):
    db_media = models.Media(**media.model_dump())
    db.add(db_media)
    db.commit()
    db.refresh(db_media)
    return db_media

def get_all_media(db: Session):
    return db.query(models.Media).all()

def get_media(db: Session, media_id: int):
    return db.query(models.Media).filter(models.Media.id== media_id).first()

def assign_media_to_customer(db: Session, media_id: int, customer_id: int):
    media = get_media(db, media_id)
    if not media:
        return None
    media.customer_id = customer_id
    db.commit()
    db.refresh(media)
    return media

def update_media(db: Session, media_id: int, media_data):
    item = db.query(models.Media).filter(models.Media.id == media_id).first()
    if not item:
        return False
    for field, value in media_data.model_dump(exclude_unset=True).items():
        setattr(item, field, value)
    db.commit()
    return True

def delete_media(db: Session, media_id: int):
    item = db.query(models.Media).filter(models.Media.id == media_id).first()
    if not item:
        return False
    db.delete(item)
    db.commit()
    return True

