'''
@Description: 
@Author: Panbo Hey
@Date: 2025-08-11 10:05:47
@LastEditTime: 2025-08-11 10:21:49
@LastEditors: Panbo Hey
'''
# main.py
from fastapi import FastAPI
app = FastAPI()
@app.get("/")
async def read_root():
    return {"Hello": "World"}
