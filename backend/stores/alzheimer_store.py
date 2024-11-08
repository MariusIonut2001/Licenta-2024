from backend.db.models.alzheimer import AlzheimerDBModel, AlzheimerHistory


class AlzheimerStore:
    @staticmethod
    def save(alzheimer_model: AlzheimerDBModel):
        alzheimer_model.save()

    @staticmethod
    def update(identifier: int, **kwargs):
        AlzheimerDBModel.objects(identifier=identifier).update_one(**kwargs)

    @staticmethod
    def delete(identifier: int):
        AlzheimerDBModel.objects(identifier=identifier).delete()
