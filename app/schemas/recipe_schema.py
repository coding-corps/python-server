from pydantic import BaseModel


class RecipeSchema(BaseModel):
    title: str
    difficulty: str
    directions: str

   

