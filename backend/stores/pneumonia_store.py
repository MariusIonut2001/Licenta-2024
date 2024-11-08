from backend.db.models.pneumonia import PneumoniaDBModel


class PneumoniaStore:
    @staticmethod
    def save(pneumonia_model: PneumoniaDBModel):
        pneumonia_model.save()

    @staticmethod
    def update(identifier: int, **kwargs):
        PneumoniaDBModel.objects(identifier=identifier).update_one(**kwargs)

    @staticmethod
    def delete(identifier: int):
        PneumoniaDBModel.objects(identifier=identifier).delete()
