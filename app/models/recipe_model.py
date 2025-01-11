class Recipe(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(120), nullable=False)
    difficulty = db.Column(db.String(20))
    nutrition_facts = db.Column(db.JSON)
    directions = db.Column(db.Text)
    ingredients = db.Column(db.JSON)
