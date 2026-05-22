import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
import joblib

#Load Dataset
data = pd.read_csv("Dataset/students.csv")

#Label Encoding
label_encoder = LabelEncoder()

data["Gender"] = label_encoder.fit_transform(data["Gender"])
data["Final_Performance"] = label_encoder.fit_transform(data["Final_Performance"])

#Features (Input)
x = data.drop("Final_Performance", axis=1)

#Features (Output)
y = data["Final_Performance"]

#Split Dataset
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = 0.2, random_state = 42)

#Create Model
model = RandomForestClassifier()

#Train Model
model.fit(x_train, y_train)

#Make Prdeictions
y_pred = model.predict(x_test)

#Check Accuracy
accuracy = accuracy_score(y_test, y_pred)

print("Model Accuracy:", accuracy)

joblib.dump(model, "Model/model.pkl")

print("Model saved Successfully!")