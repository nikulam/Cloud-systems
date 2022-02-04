import flask
from google.cloud import storage
import os


def create_text_file_http(request):

    request_data = request.get_data(as_text=True)
    r = request.get_json()

    name = r['fileName']
    content = r['fileContent']

    bucketName = os.environ.get('BUCKET_ENV_VAR', 'Specified environment variable is not set.')

    storage_client = storage.Client()
    bucket = storage_client.get_bucket(bucketName)
    blob = bucket.blob(name)
    blob.upload_from_string(content)

    return flask.jsonify(name), 200