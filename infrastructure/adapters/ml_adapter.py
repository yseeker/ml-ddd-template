from sklearn import svm

class MLApiAdapter:
    def train_model(self, model_type: str, X, y):
        if model_type == "svm":
            model = svm.SVC()
        else:
            raise ValueError("Unsupported model type")

        model.fit(X, y)
        return model

    def predict(self, model, X):
        return model.predict(X)