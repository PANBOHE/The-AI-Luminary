'''
@Description: 
@Author: Panbo Hey
@Date: 2025-08-11 10:25:23
@LastEditTime: 2025-08-11 10:29:49
@LastEditors: Panbo Hey
'''
'''
@Description: 
@Author: Panbo Hey
@Date: 2025-08-11 10:25:23
@LastEditTime: 2025-08-11 10:25:32
@LastEditors: Panbo Hey
'''
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
 
app = FastAPI()
 
# 设置模板目录
templates = Jinja2Templates(directory="templates")
 
@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})
 
@app.get("/about", response_class=HTMLResponse)
async def about(request: Request):
    return templates.TemplateResponse("about.html", {"request": request})
 
@app.get("/contact", response_class=HTMLResponse)
async def contact(request: Request):
    return templates.TemplateResponse("contact.html", {"request": request})