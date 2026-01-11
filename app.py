from flask import Flask, request, render_template
from src.pipeline.predict_pipeline import CustomData, PredictPipeline

app = Flask(__name__)

# Home route
@app.route('/')
def index():
    # First page load: no result yet
    return render_template('home.html', results=None)


# Prediction route
@app.route('/predictdata', methods=['GET', 'POST'])
def predict_datapoint():
    if request.method == 'POST':
        try:
            # 1. Collect form data (names must match home.html)
            data = CustomData(
                gender=request.form.get('gender'),
                race_ethnicity=request.form.get('ethnicity'),  # maps "ethnicity" → race_ethnicity
                parental_level_of_education=request.form.get('parental_level_of_education'),
                lunch=request.form.get('lunch'),
                test_preparation_course=request.form.get('test_preparation_course'),
                reading_score=float(request.form.get('reading_score')),
                writing_score=float(request.form.get('writing_score'))
            )

            # 2. Convert to DataFrame
            pred_df = data.get_data_as_data_frame()
            print("Input DataFrame:")
            print(pred_df)

            # 3. Make prediction
            pipeline = PredictPipeline()
            results = pipeline.predict(pred_df)
            print("Prediction result:", results)

            # 4. Send single number to template
            return render_template('home.html', results=round(results[0], 2))

        except Exception as e:
            import traceback
            print(traceback.format_exc())
            # Show error text in place of result
            return render_template('home.html', results=f"Error: {e}")

    # For GET /predictdata (rarely used), just show page with no result
    return render_template('home.html', results=None)


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
