from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import make_pipeline


class MLApiAdapter:
    def __init__(self):
        self.models = {
            'linear_regression': LinearRegression,
        }

    def train_model(self, model_type: str, X_train, y_train):
        if model_type not in self.models:
            raise ValueError(f"Unsupported model type: {model_type}")

        model_class = self.models[model_type]
        model = make_pipeline(StandardScaler(), model_class())
        model.fit(X_train, y_train)

        return model

    def predict(self, model, X):
        return model.predict(X)