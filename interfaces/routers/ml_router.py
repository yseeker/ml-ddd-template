
from fastapi import APIRouter
from src.application.services.train_and_save_model_use_case import TrainAndSaveModelUseCase
from src.application.services.predict_with_model_use_case import PredictWithModelUseCase
from src.interfaces.api.view_models.ml_model import TrainModelInput, PredictModelInput, MLModelResponse

router = APIRouter()

def train_model_background(task_id: str, input_data: TrainModelInput):
    try:
        ml_model = ml_model_service.train_model(input_data.model_type, np.array(input_data.X), np.array(input_data.y), input_data.test_size)
        # ここで、トレーニングされたモデルを保存するか、データベースに記録します。
    except Exception as e:
            error_info = traceback.format_exc()
            logger.error(f"Error in background task {task_id}: {e}\n{error_info}")

@router.post("/train", response_model=MLModelResponse)
async def train_model(input_data: TrainModelInput):
    use_case = TrainAndSaveModelUseCase()
    ml_model = use_case.execute(input_data.model_type, input_data.X, input_data.y, input_data.test_size)
    return MLModelResponse.from_domain_model(ml_model)

@router.post("/predict", response_model=MLModelResponse)
async def predict_with_model(input_data: PredictModelInput):
    use_case = PredictWithModelUseCase()
    y_pred = use_case.execute(input_data.model_id, input_data.X)
    return MLModelResponse(y_pred=y_pred)


