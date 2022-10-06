from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse, FileResponse
from aiohttp import ClientSession
from PIL import Image
from fastapi.staticfiles import StaticFiles
from io import BytesIO
from fastapi.templating import Jinja2Templates
from imagegen import h1, h2, h3

app = FastAPI()
app.mount("/static", StaticFiles(directory="external"), name="static")
templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
async def homepage(request: Request):
    return templates.TemplateResponse("index.html", {
        "request": request,
    })

@app.get("/api", response_class=FileResponse)
async def api(avatar, template_id):

    if avatar == "http://localhost:8000/static/test_avatar.png":
        avatar = Image.open("./external/test_avatar.png")
    else:
        async with ClientSession()   as session:
            async with session.get(avatar) as response:
                data = await response.read()
        
        avatar =  Image.open(BytesIO(data))

    if template_id == "h1":
        a = h1(avatar)    
        return FileResponse(f"./trash/{a}.png")
    elif template_id == "h2":
        a = h2(avatar)    
        return FileResponse(f"./trash/{a}.png")
    elif template_id == "h3":
        a = h3(avatar)    
        return FileResponse(f"./trash/{a}.png")