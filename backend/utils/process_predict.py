def process_predict(prediction: str):
    if prediction == "MildDemented":
        pred = 2
    elif prediction == "NonDemented":
        pred = 0
    elif prediction == "VeryMildDemented":
        pred = 1
    else:
        pred = 3
    return pred