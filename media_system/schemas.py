from pydantic import BaseModel
from datetime import datetime

class CustomerBase(BaseModel):
    name: str
    phone: str

class CustomerCreate(CustomerBase):
    pass

class CustomerResponse(CustomerBase):
    id: int
    name: str
    phone: str
    created_at: datetime
    class Config:
        orm_mode = True

class MediaBase(BaseModel):
    title: str
    category: str
    author_or_artist: str
    store_name: str
    customer_id: int

class MediaCreate(MediaBase):
    pass

class MediaResponse(BaseModel):
    id: int
    title: str
    category: str
    author_or_artist: str
    store_name: str
    customer_id: int | None = None
    created_at: datetime
    updated_at: datetime | None = None

    class Config:
        orm_mode = True


class MediaUpdate(BaseModel):
    title: str | None = None
    category: str | None = None
    author_or_artist: str | None = None
    store_name: str | None = None
    customer_id: int | None = None
