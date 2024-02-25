from typing import Union
import weaviate
import os


class Storage:
    """
    intialize weaviate client
    """

    def __init__(self, host="localhost", port=8080):
        client = weaviate.client.Client(
            url=f"http://{host}:{port}",
            additional_headers={
                "X-OpenAI-Api-Key": os.getenv("OPENAI_API_KEY"),
            })
        self.client = client

    def is_ready(self):
        """
        check if weaviate is ready
        """
        return self.client.is_ready()

    def delete(self):
        """
        delete all data
        """
        self.client.schema.delete_all()

    def get(self):
        """
        get current schema
        """
        self.client.schema.get()

    def create_schema(self,  schema_class: Union[dict, str]):
        self.client.schema.create_class(schema_class)
