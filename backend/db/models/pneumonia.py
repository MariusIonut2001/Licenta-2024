import mongoengine as db


class PneumoniaHistory(db.Document):
    identifier = db.StringField(required=True)
    createdAt = db.DateTimeField(required=True)
    simptome = db.ListField(db.StringField(required=True))

    meta = {
        "collection": "PneumoniaHistory",
        "indexes": [
            {"fields": ["identifier"], "unique": True, "name": "Unique_identifier_pneumonia_history"},
        ]
    }


class PneumoniaDBModel(db.Document):
    identifier = db.IntField(required=True)
    nume = db.StringField(required=True)
    prenume = db.StringField(required=True)
    nrTel = db.StringField(required=True)
    email = db.StringField(required=True)
    varsta = db.StringField(required=True)
    gen = db.StringField(required=True)
    bolnav = db.BooleanField(required=True)
    istoric = db.ListField(db.ReferenceField(PneumoniaHistory), required=False)

    meta = {
        "collection": "PneumoniaDBModel",
        "indexes": [
            {"fields": ["identifier"], "unique": True, "name": "Unique_identifier_pneumonia"},
        ]
    }

