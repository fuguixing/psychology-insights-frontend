import os
import joblib
from azure.storage.blob import BlobServiceClient

class ModelFactory:
    _models = {}

    @classmethod
    def get_model(cls, model_file_name):
        if model_file_name not in cls._models:
            cls._models[model_file_name] = cls.load_model(model_file_name)
        return cls._models[model_file_name]

    @staticmethod
    def load_model(model_file_name):
        container_name = "models"
        local_model_file_path = os.path.join(os.getcwd(), container_name, model_file_name)
        if os.path.exists(local_model_file_path):
            model = joblib.load(local_model_file_path)
        else:
            blob_connection_string = os.environ["PsyModelsStorage"]
            blob_service_client = BlobServiceClient.from_connection_string(blob_connection_string)
            container_client = blob_service_client.get_container_client(container_name)
            blob_client = container_client.get_blob_client(model_file_name)
            
            with open(local_model_file_path, "wb") as local_file:
                local_file.write(blob_client.download_blob().readall())
            
            model = joblib.load(local_model_file_path)
        
        return model
