import pandas as pd
from src.exception import CustomException
import sys
import os
from src.utils import load_object


class CustomData:
    def __init__(self, gender, race_ethnicity, parental_level_of_education,
                 lunch, test_preparation_course, reading_score, writing_score):
        self.gender = gender
        self.race_ethnicity = race_ethnicity
        self.parental_level_of_education = parental_level_of_education
        self.lunch = lunch
        self.test_preparation_course = test_preparation_course
        self.reading_score = reading_score
        self.writing_score = writing_score

    def get_data_as_data_frame(self):
        try:
            data_dict = {
                "gender": [self.gender],
                "race/ethnicity": [self.race_ethnicity],
                "parental level of education": [self.parental_level_of_education],
                "lunch": [self.lunch],
                "test preparation course": [self.test_preparation_course],
                "reading score": [self.reading_score],
                "writing score": [self.writing_score],
            }
            return pd.DataFrame(data_dict)
        except Exception as e:
            raise CustomException(e, sys)

        
class PredictPipeline:
    def __init__(self):
        
        # base_dir = project root (one level above src)
        base_dir = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))

        self.model_path = os.path.join(base_dir, "artifacts", "model.pkl")
        self.preprocessor_path = os.path.join(base_dir, "artifacts", "preprocessor.pkl")

        print("BASE DIR:", base_dir)
        print("MODEL PATH:", self.model_path)
        print("PREPROCESSOR PATH:", self.preprocessor_path)


    def predict(self, features):
        try:
            model = load_object(self.model_path)
            preprocessor = load_object(self.preprocessor_path)

            data_scaled = preprocessor.transform(features)
            preds = model.predict(data_scaled)

            return preds

        except Exception as e:
            raise CustomException(e, sys)

