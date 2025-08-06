import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split

flavour_data = pd.read_csv("ice_cream_internship/flavour_data.csv")

X = flavour_data.drop(columns=["Flavour"])
y = flavour_data["Flavour"] 
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

model = DecisionTreeClassifier()
model.fit(X_train, y_train)

age_group_mappings = {
    "18-29": 0,
    "30-44": 1,
    "45-64": 2,
    "65+": 3,
}

def predict_flavour(gender, age_group):
    input_data = pd.DataFrame([{
        "Gender": gender,
        "Age Group": age_group_mappings[age_group],
    }])

    prediction = model.predict(input_data)
    return prediction[0]
