from pydantic import BaseModel


class AddressBase(BaseModel):
    email: str
    user_id: int


class AddressCreate(AddressBase):
    """"""


class Address(AddressBase):
    id: int

    class Config:
        orm_mode = True


class UserBase(BaseModel):
    name: str


class UserCreate(UserBase):
    """"""


class User(UserBase):
    id: int
    addresses: list[Address] = []

    class Config:
        orm_mode = True
