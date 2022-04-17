import tensorflow as tf
from tensorflow import keras
import numpy as np
import PIL

# predictor function
def predict_saved_model(img_path, model_path):
    '''
    Takes the saved model to make an inference on a given image
    '''
    #model = tf.saved_model.load('models/my_saved_model')
    model = tf.keras.models.load_model(model_path)
    image_size = (180, 180)
    img = keras.preprocessing.image.load_img(
        img_path, target_size=image_size
        )
    img_array = keras.preprocessing.image.img_to_array(img)
    img_array = tf.expand_dims(img_array, 0)  # Create batch axis

    predictions = model.predict(img_array)
    score = predictions[0]
    print(score)
    print(
        "This image is %.2f percent cat and %.2f percent dog."
        % (100 * (1 - score), 100 * score)
        )

    return {
            "cat": str((100 * (1 - score))[0]),
            "dog": str((100 * score)[0])
            }
