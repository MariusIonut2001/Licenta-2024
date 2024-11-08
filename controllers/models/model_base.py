class ModelBase:
    def __init__(self):
        self.model = None
        self.processor = None
        self.init()

    def init(self):
        raise NotImplementedError()

    def predict(self, prediction_input):
        raise NotImplementedError()
