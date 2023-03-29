from src.domain.aggregates.ml_model import MLModel

class MLModelRepository:
    def save(self, ml_model: MLModel) -> MLModel:
        # ここでモデルを永続化するロジックを実装
        # データベースやファイルシステムを使って保存します
        saved_ml_model = None  # Replace this with actual saving logic
        return saved_ml_model

    def get(self, model_id: int) -> MLModel:
        # ここでモデルを取得するロジックを実装
        # データベースやファイルシステムから読み込みます
        ml_model = None  # Replace this with actual retrieval logic
        return ml_model