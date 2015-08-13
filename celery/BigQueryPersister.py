from celery.utils import get_service
import json
import uuid
import configparser

class BigQueryPersister:
    
    @staticmethod
    def getInstance():
        config = configparser.ConfigParser()
        config.read('conf/bigQuery.cfg')  
    
    def __init__(self, project_id, dataset_id, table_id):
        self.service = get_service()
        self.project_id = project_id
        self.dataset_id = dataset_id
        self.table_id = table_id
        
    def stream_row_to_bigquery(self, data, num_retries = 5):
    # Generate a unique row id so retries
    # don't accidentally duplicate insert
        insert_all_data = {
            'insertId': str(uuid.uuid4()),
            'rows': [{'json': data}]
        }
        return self.service.tabledata().insertAll(
            projectId=self.project_id,
            datasetId=self.dataset_id,
            tableId=self.table_id,
            body=insert_all_data).execute(num_retries=num_retries)
        
    