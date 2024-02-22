
from fastapi import FastAPI
from routes import chat

app = FastAPI(debug=True,)
app.include_router(chat.router)
