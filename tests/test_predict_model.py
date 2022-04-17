# import predict_saved_model from src
from src.predicter import predict_saved_model
from pytest import approx

# prediction of cute_dog_photo image
pred = {"cat": str(0.00), "dog": 99.99887}

# test function
def test_predict_saved_model():
    assert float(predict_saved_model(img_path='./cute_dog_photo.jpg',
                               model_path='./model.h5')["dog"]) == approx(pred["dog"])
