from fastapi import FastAPI, Request
from pydantic import BaseModel
from model.model import predict_pipeline
from model.model import __version__ as model_version
from fastapi.middleware.cors import CORSMiddleware
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse


app = FastAPI()

templates = Jinja2Templates(directory="templates")


# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=[ "https://cmg-ai-ml.netlify.app/","http://localhost:3000/", ],
#     allow_methods=["*"],
#     allow_headers=["*"],
    
# )

class TextIn(BaseModel):
    text: str

class PredictionOut(BaseModel):
    language: str

@app.get("/",response_class=HTMLResponse)
def home(request: Request):
    return  templates.TemplateResponse(name="home.html")
    #return {"health_check": "OK", "model_version": model_version}

@app.post("/predict", response_model=PredictionOut)
def predict(payload: TextIn):
    print("text",payload)
    print("text1",payload.text)
    language = predict_pipeline(payload.text)
    print(language)
    return {"language": language}

