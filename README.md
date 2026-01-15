## End to End Machine Learning Project# StudentPerfomance_EndToEndProject

# Student Performance End-to-End Machine Learning Project

This project is an end-to-end Machine Learning application that predicts student exam performance based on academic and demographic factors. It demonstrates the complete ML workflow, including data ingestion, preprocessing, model training, evaluation, and deployment using Flask.

---

## Project Overview

The objective of this project is to predict students’ math scores using the following features:

* Gender
* Race/Ethnicity
* Parental level of education
* Lunch type
* Test preparation course
* Reading score
* Writing score

The project focuses on building a complete machine learning pipeline and generating predictions using trained models.

---

## Machine Learning Pipeline

The project follows a modular pipeline-based approach:

1. Data Ingestion

   * Loads the dataset
   * Splits data into training and testing sets

2. Data Transformation

   * Handles numerical and categorical features
   * Applies scaling and encoding

3. Model Training

   * Trains multiple regression models
   * Uses GridSearchCV for hyperparameter tuning
   * Selects the best-performing model

4. Prediction Pipeline

   * Loads trained model and preprocessor
   * Generates predictions from user input

---

## Technology Stack

* Python
* NumPy
* Pandas
* Scikit-learn
* Pickle / Dill
* Git and GitHub

---

## How to Run the Project

1. Clone the repository

```bash
git clone https://github.com/Shraddha964-dev/StudentPerfomance_EndToEndProject.git
cd StudentPerfomance_EndToEndProject
```

2. Create and activate a virtual environment

```bash
python -m venv venv
venv\Scripts\activate
```

3. Install dependencies

```bash
pip install -r requirements.txt
```

4. Run the training pipeline

```bash
python src/pipeline/train_pipeline.py
```
5. Run the application
```
python app.py
```
6. Open the application in a browser
```
http://127.0.0.1:5000/
```


## Output

The trained model predicts student math scores based on input features. Model performance is evaluated using regression metrics.

<img width="1913" height="986" alt="image" src="https://github.com/user-attachments/assets/bea24415-0f64-47d4-b21e-4ea4a7b20cf0" />

<img width="1901" height="965" alt="image" src="https://github.com/user-attachments/assets/949d18df-ab54-4c94-a614-ef933810f947" />

<img width="1907" height="987" alt="image" src="https://github.com/user-attachments/assets/30b2b544-a09c-4ac1-9af3-0fd612114430" />

---

## Learning Outcomes

* Understanding end-to-end machine learning workflows
* Building modular and reusable ML pipelines
* Applying hyperparameter tuning using GridSearchCV
* * Implementing logging and exception handling

---

## Future Improvements

* Add Docker support
* Deploy the application on cloud platforms
* Improve user interface
* Add CI/CD pipeline

---

## About Me

I am learning Machine Learning and Data Science and actively building projects to improve my skills.

If you have suggestions or feedback, feel free to share.

If you find this helpful, feel free to star the repository!

If you liked what you saw, want to have a chat with me about the portfolio, work opportunities, or collaboration, shoot an email at ssajane86@gmail.com.
