from fastapi import FastAPI
from routes import chat
from storage import weaviate

client = weaviate.Storage()
client.is_ready()
client.delete()
client.get()


article_schema = {
    "class": "Chat",
    "description": "Collection Chat From Zendesk API",
    "vectorizer": "text2vec-openai",
    "moduleConfig": {
        "text2vec-openai": {
            "model": "ada",
            "modelVersion": "002",
            "type": "text"
        }
    },
    "properties": [{
        "name": "ticket_title",
        "description": "Title of the article",
        "dataType": ["string"]
    },
        {
        "name": "message",
        "description": "Contents of the article",
        "dataType": ["text"]
    },
        {
        "name": "increase_withdraw_limit",
        "description": "indicate this row is a request to withdraw limit",
        "dataType": ["boolean"],
    }]
}

client.create_schema(article_schema)
client.get()


app = FastAPI(debug=True,)
app.include_router(chat.router)
