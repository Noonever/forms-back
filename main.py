from fastapi import FastAPI
from schemas import FormData

app = FastAPI()


@app.get("/create-form/{form_type}")
async def create_form(form_type: str, uid: str):
        


@app.post("/forms")
async def handle_form(form_data: FormData):
    print(f"\033[93mKey: {form_data}\033[0m")

    


