import pickle
import pandas as pd

# load model
with open('model/model.pkl', 'rb') as f:
    model = pickle.load(f)

MODEL_VERSION = '1.0.0'


def predict_output(user_input: dict):

    input_df = pd.DataFrame([user_input])

    predicted_class = model.predict(input_df)[0]

    probabilities = model.predict_proba(input_df)[0]
    classes = model.classes_

    probability_dict = {
        cls: round(float(prob), 2)
        for cls, prob in zip(classes, probabilities)
    }

    confidence = probability_dict[predicted_class]

    return {
        "predicted_category": predicted_class,
        "confidence": confidence,
        "probabilities": probability_dict,
    }

