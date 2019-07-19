# Import Google Cloud client library
from google.cloud import storage

# Importing Logging for storing logs of operations
import logging

# Logging config
logging.basicConfig(filename="bucket.log", format='%(asctime)s %(message)s', filemode='w') 
logger=logging.getLogger()
logger.setLevel(logging.DEBUG)


storage_client = storage.Client()


def upload_blob():
    """ Uploads a file to the bucket """

    bucket_name = "krutik-source"
    destination_blob_name = "teletubbies.jpeg"

    try:
        bucket = storage_client.get_bucket(bucket_name)
        blob = bucket.blob(destination_blob_name)
        blob.upload_from_filename(destination_blob_name)

        # Logging info as object is uploaded successfully
        logging.info('Object Uploaded')

    except Exception as e:
        # Displays and Logs Errors
        logger.error(e)
        print('Error! Please Check Your Code.')


def download_blob():
    """ Downloads a blob from the bucket """

    source_blob_name = "teletubbies.jpeg"
    destination_file_name = "/home/krutik/Downloads/teletubbies.jpeg"
    bucket_name = "krutik-source"

    try:
        bucket = storage_client.get_bucket(bucket_name)
        blob = bucket.blob(source_blob_name)
        blob.download_to_filename(destination_file_name)

        # Logging info as object is downloaded successfully
        logging.info('Object Downloaded')

    except Exception as e:
        # Displays and Logs Errors
        logger.error(e)
        print('Error! Please Check Your Code.')



def copy_blob():
    """ Copies a blob from one bucket to another with a new name """

    bucket_name = "krutik-source"
    new_bucket_name = "krutik-destination"
    blob_name = "teletubbies.jpeg"

    try:
        source_bucket = storage_client.get_bucket(bucket_name)
        source_blob = source_bucket.blob(blob_name)
        destination_bucket = storage_client.get_bucket(new_bucket_name)

        new_blob = source_bucket.copy_blob(source_blob, destination_bucket, blob_name)

        # Logging info as object is downloaded successfully
        logging.info('Object Copied')

    except Exception as e:
        # Displays and Logs Errors
        logger.error(e)
        print('Error! Please Check Your Code.')



def delete_blob():
    """ Deletes a blob from the bucket """

    bucket_name = "krutik-source"
    blob_name = "teletubbies.jpeg"

    try:
        bucket = storage_client.get_bucket(bucket_name)
        blob = bucket.blob(blob_name)

        blob.delete()

        # Logging info as object is deleted successfully
        logging.info('Object Deleted')

    except Exception as e:
        # Displays and Logs Errors
        logger.error(e)
        print('Error! Please Check Your Code.')



def move_blob():
    """ Moves a blob from one bucket to another """

    bucket_name = "krutik-source"
    new_bucket_name = "krutik-destination"
    blob_name = "teletubbies.jpeg"

    try:
        source_bucket = storage_client.get_bucket(bucket_name)
        source_blob = source_bucket.blob(blob_name)
        destination_bucket = storage_client.get_bucket(new_bucket_name)

        new_blob = source_bucket.copy_blob(source_blob, destination_bucket, blob_name)
        blob = source_bucket.blob(blob_name)
        blob.delete()

        # Logging info as object is deleted successfully
        logging.info('Object Deleted')

    except Exception as e:
        # Displays and Logs Errors
        logger.error(e)
        print('Error! Please Check Your Code.')



def main():
    upload_blob()
    download_blob()
    copy_blob()
    delete_blob()
    upload_blob()
    move_blob()


if __name__ == '__main__':
    main()