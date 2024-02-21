import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.neural_network import MLPClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import OneHotEncoder
from sklearn.preprocessing import OrdinalEncoder
from sklearn.preprocessing import LabelEncoder
from sklearn.pipeline import Pipeline
from sklearn.metrics import accuracy_score

# Real Data
real_data = pd.read_csv('cities_demo.csv')

# Synthetic Data
synthetic_data = pd.read_csv('cities_demo.csv')

# synthetic_data = pd.DataFrame(
#                 {'Name': ['Dick', 'Harry', 'Tom'],
#                 'Age':[29,29,29],
#                 'Height':[177,177,177],
#                 'Weight':[75,65,85]}
# )

X_real, y_real = real_data[["Temperature","Longitude"]], real_data["Category"]
X_synthetic, y_synthetic = real_data[["Temperature","Longitude"]], real_data["Category"] #TODO: split x and y

# Prototype Evaluation Method
def evaluate(X_real, y_real,X_synthetic, y_synthetic):

    # Encode the Real Data
    ordinal_enc = OrdinalEncoder()
    label_enc  = LabelEncoder()
                                                  
    # X_real, y_real = ordinal_enc.transform(X_real), label_enc.transform(y_real)

    categories = ["Category"] #['Continental','Subtropical','Tropical']
    print(len(categories))
    print(type(categories))
    ohe = OneHotEncoder(handle_unknown='ignore')
    logreg = LogisticRegression()
    eval_pipeline = Pipeline([('encoder', ohe), ('model', logreg)])
    eval_pipeline.fit(X_synthetic, y_synthetic)
    y_pred = eval_pipeline.predict(X_real)

    return accuracy_score(y_real, y_pred)
    # return type(X_real)
    # return categories.shape

result = evaluate(X_real, y_real, X_synthetic, y_synthetic)
print("accuracy score: ", result)
        



