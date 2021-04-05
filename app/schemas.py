from typing import List

from pydantic import BaseModel


class UserRequestType(BaseModel):
    name: str
    email: str
    password: str


class UserResponseType(BaseModel):
    name: str
    email: str

    class Config:
        orm_mode = True


class OrderBase(BaseModel):
    code: str


class CustomerRequestType(BaseModel):
    name: str
    email: str
    password: str


class CustomerResponseType(BaseModel):
    name: str
    email: str
    orders: List[OrderBase] = []

    class Config:
        orm_mode = True


class OrderRequestType(OrderBase):
    code: str
    # customer: CustomerRequestType


class OrderResponseType(OrderBase):
    code: str
    customer: CustomerResponseType

    class Config:
        orm_mode = True
