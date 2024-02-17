#Method taken from GANBLR evaluate method
def evaluate(x, y, model='lr') -> float:
        """
        Perform a TSTR(Training on Synthetic data, Testing on Real data) evaluation.

        Parameters
        ----------
        x, y : array_like
            Test dataset.

        model : str or object
            The model used for evaluate. Should be one of ['lr', 'mlp', 'rf'], or a model class that have sklearn-style `fit` and `predict` method.

        Return:
        --------
        accuracy_score : float.

        """
        from sklearn.linear_model import LogisticRegression
        from sklearn.neural_network import MLPClassifier
        from sklearn.ensemble import RandomForestClassifier
        from sklearn.preprocessing import OneHotEncoder
        from sklearn.pipeline import Pipeline
        from sklearn.metrics import accuracy_score
        
        eval_model = None
        models = dict(
            lr=LogisticRegression,
            rf=RandomForestClassifier,
            mlp=MLPClassifier
        )
        if model in models.keys():
            eval_model = models[model]()
        elif hasattr(model, 'fit') and hasattr(model, 'predict'):
            eval_model = model
        else:
            raise Exception("Invalid Arugument `model`, Should be one of ['lr', 'mlp', 'rf'], or a model class that have sklearn-style `fit` and `predict` method.")

        synthetic_data = self._sample()
        synthetic_x, synthetic_y = synthetic_data[:,:-1], synthetic_data[:,-1]
        x_test = self._ordinal_encoder.transform(x)
        y_test = self._label_encoder.transform(y)

        categories = self._d.get_categories()
        pipline = Pipeline([('encoder', OneHotEncoder(categories=categories, handle_unknown='ignore')), ('model',  eval_model)]) 
        pipline.fit(synthetic_x, synthetic_y)
        pred = pipline.predict(x_test)
        return accuracy_score(y_test, pred)