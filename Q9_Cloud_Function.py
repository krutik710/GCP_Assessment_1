import base64
from google.cloud import bigquery

def hello_pubsub(event, context):
    message = base64.b64decode(event['data']).decode('utf-8')

    message_list = message.splitlines()
    bucket_name = message_list[0]
    object_path = message_list[1]

    print(bucket_name)
    print(object_path)
    
    client = bigquery.Client()
    dataset_ref = client.dataset('krutik_dataset')
    job_config = bigquery.LoadJobConfig()
    
    job_config.autodetect = True
	
    job_config.source_format = bigquery.SourceFormat.NEWLINE_DELIMITED_JSON
    
    uri  = "gs://" + bucket_name + "/" + object_path
    load_job = client.load_table_from_uri(uri, dataset_ref.table("gcptable"), job_config=job_config)  # API request
    print("Starting job {}".format(load_job.job_id))
    load_job.result()  
