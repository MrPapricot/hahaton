from fastapi import FastAPI
from fastapi.responses import HTMLResponse
import requests

ownerAlias = "gorod-it-hack"
projectAlias = "uglublenka"
base = "https://api.gitflic.ru/"
TOKEN = "8322c6b6-99d0-4423-8cce-4b9868c5a6cd"
headers = {
    "Authorization": f"token {TOKEN}"
}

app = FastAPI()

@app.get('/')
def default():
    print("agag")