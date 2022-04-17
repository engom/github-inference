import json
import urllib.parse
import boto3
from src.predicter import predict_saved_model as predict_model


# main function
def main(aws_key_id, aws_secret_access_key):
    # creation a session to connect to s3
    session = boto3.Session(
                            aws_access_key_id=aws_key_id,
                            aws_secret_access_key=aws_secret_access_key,
                            region_name='us-east-1')

    # Set up some variables we'll need
    print("start ....")
    image_path = "/tmp/image.jpg"
    model_path = "/tmp/model.h5"


    # Connect to AWS Services
    s3_client = session.client('s3') #boto3.client('s3')

    ssm_client = session.client('ssm') #boto3.client('ssm')


    # S3  bucket name
    s3_bucket = s3_client.list_buckets()['Buckets'][1]['Name']
    print(s3_bucket)

    # s3 Image object name
    s3_img = s3_client.list_objects(Bucket=s3_bucket)['Contents'][1]['Key']
    print(s3_img)

    # s3 model_path
    s3_model_path = s3_client.list_objects(Bucket=s3_bucket)['Contents'][3]['Key']
    print(s3_model_path)

    # Download image container
    with open(image_path, 'wb') as f:
        s3_client.download_fileobj(s3_bucket, s3_img, f)


    # Download model container
    with open(model_path, 'wb') as f:
        s3_client.download_fileobj(s3_bucket, s3_model_path, f)


    # Make the inference
    prediction = predict_model(image_path, model_path)

    return {
            "statusCode": 200,
            "headers": {
                "Content-Type": "application/json"
                },
            "body": json.dumps({
                    "cat": prediction["cat"],
                    "dog": prediction["dog"]
                    })
            }
            
# main program
if __name__ == '__main__':
    #predict_model(img_path='./cute_dog_photo.jpg',
    #            model_path='./model.h5')
    main(aws_key_id, aws_secret_access_key)
