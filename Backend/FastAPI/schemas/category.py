from datetime import datetime
from pydantic import BaseModel, validator

#?metodo que retorna la estructura de un modelo category
def category_schema_function(category)->dict:
  return {
    "id"          : category.id,
    "description" : category.description,
    "state"       : category.state,
    "created_at"  : category.created_at,
    "updated_at"  : category.updated_at
  }
#?metodo que retorna la lista estructura de un modelo category
def categories_schema_function(categories)->list:
  return [category_schema_function(category) for category in categories]

class Category(BaseModel):
  id: int | None
  description: str
  state: bool| None
  
  class Config:
    validate_assignment = True
  @validator('state')
  def set_state(cls, state):
    return state==None or state

class CategoryUpdte(BaseModel):
  id: int
  description: str
  state: bool

class CategoryFull(Category):
  created_at: datetime
  updated_at: datetime