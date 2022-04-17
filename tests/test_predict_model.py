# import predict_saved_model from src
from predicter import predict_saved_model


# prediction of cute_dog_photo image
pred = {"cat": str(0.00), "dog": str(99.99887)}

# test function
def test_predict_saved_model():
    assert predict_saved_model(img_path='./cute_dog_photo.jpg',
                               model_path='./model.h5')["dog"] == pred["dog"]
