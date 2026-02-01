from flask import Flask, render_template, request
import joblib
import pandas as pd

app = Flask(__name__)

# ✅ Load model properly
# During training you should have saved like:
# joblib.dump((model, model_columns), "mental_stress_model.pkl")
model, model_columns = joblib.load("mental_stress_model.pkl")


@app.route("/", methods=["GET", "POST"])
def home():
    prediction = None

    if request.method == "POST":

        # Collect form data (names MUST match HTML)
        input_data = {
            "Gender": request.form["Gender"],
            "Country": request.form["Country"],
            "Occupation": request.form["Occupation"],
            "Family History": request.form["Family_History"],
            "Treatment": request.form["Treatment"],
            "Days Indoors": request.form["Days_Indoors"],
            "Changes in Habits": request.form["Changes_in_Habits"],
            "Mental Health History": request.form["Mental_Health_History"],
            "Mood Swings": request.form["Mood_Swings"],
            "Coping Struggles": request.form["Coping_Struggles"],
            "Work Interest": request.form["Work_Interest"],
            "Social Weakness": request.form["Social_Weakness"],
            "Mental Health Interview": request.form["Mental_Health_Interview"],
            "Care Options": request.form["Care_Options"]
        }

        # Convert to DataFrame
        input_df = pd.DataFrame([input_data])

        #  One-hot encode
        input_encoded = pd.get_dummies(input_df)

        #  Align with training columns
        input_encoded = input_encoded.reindex(
            columns=model_columns,
            fill_value=0
        )

        #  Predict
        pred = model.predict(input_encoded)[0]

        #  Map prediction
        result_map = {
            0: "🙂 Low Stress",
            1: "😟 High Stress",
            2: "😐 Moderate Stress"
        }

        prediction = result_map.get(pred, "Unknown Result")

    return render_template("index.html", prediction=prediction)


if __name__ == "__main__":
    app.run(debug=True)
