import mongoengine as db


class AlzheimerTest(db.Document):
    identifier = db.StringField(required=True)
    pacient_identifier = db.StringField(required=True)
    nume_test = db.StringField(required=True)
    scor_test = db.IntField(required=True)
    rezultat = db.StringField(required=True)
    meta = {
        "collection": "AlzheimerTest",
        "indexes": [
            {"fields": ["identifier"], "unique": True, "name": "Unique_identifier_alzheimer_test"},
        ]
    }


class AlzheimerHistory(db.Document):
    identifier = db.StringField(required=True)
    createdAt = db.DateTimeField(required=True)
    simptome = db.ListField(db.StringField(required=True))
    meta = {
        "collection": "AlzheimerHistory",
        "indexes": [
            {"fields": ["identifier"], "unique": True, "name": "Unique_identifier_alzheimer_history"},
        ]
    }


class AlzheimerDBModel(db.Document):
    identifier = db.IntField(required=True)
    nume = db.StringField(required=True)
    prenume = db.StringField(required=True)
    nrTel = db.StringField(required=True)
    email = db.StringField(required=True)
    varsta = db.StringField(required=True)
    gen = db.StringField(required=True)
    stadiuAlzheimer = db.StringField(required=True)
    istoric = db.ListField(db.ReferenceField(AlzheimerHistory), required=False)
    test_sanatate_mintala_1 = db.ListField(db.ReferenceField(AlzheimerTest), required=False)

    meta = {
        "collection": "AlzheimerDBModel",
        "indexes": [
            {"fields": ["identifier"], "unique": True, "name": "Unique_identifier_alzheimer"},
        ]
    }
