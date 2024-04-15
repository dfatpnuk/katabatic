from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import accuracy_score
import numpy as np

# Input must be dataframes
def evaluate(X_synthetic, y_synthetic, X_real, y_real):

    # print(' X_synthetic type: ',type(X_synthetic),' y_synthetic type: ', type(y_synthetic), ' X_real type: ',type(X_real), ' y_real type: ', type(y_real))
    # print(X_synthetic.isnull().sum())
    # print(y_synthetic.isnull().sum())
    # print(X_real.isnull().sum())
    # print(y_real.isnull().sum())
    # TODO: error handling, data validation
    X_synthetic = X_synthetic.to_numpy()
    y_synthetic = y_synthetic.to_numpy().ravel()
    X_real = X_real.to_numpy()
    y_real = y_real.to_numpy().ravel()
    
    # le = LabelEncoder() # Use labelencoder to convert strings to values
    # le.fit(np.unique(y_synthetic))   # TODO: Combine both y_synth and y_real values here
    # y_synthetic = le.transform(y_synthetic)
    # y_real.apply(LabelEncoder().fit_transform)
    # print(y_real)
    y_train = y_synthetic.astype('int')
    # TSTR Evaluation using Log Reg
    model = LogisticRegression(max_iter=200)
    model.fit(X_synthetic, y_train)
    y_pred = model.predict(X_real)

    return accuracy_score(y_real, y_pred)