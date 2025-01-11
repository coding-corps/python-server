class RecipeSchema(Schema):
    title = fields.Str(required=True)
    difficulty = fields.Str()
    nutrition_facts = fields.Dict()
    directions = fields.Str()
    ingredients = fields.List(fields.Str())
