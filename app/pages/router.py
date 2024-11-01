from fastapi import APIRouter
from fastapi.templating import Jinja2Templates
from fastapi.requests import Request
from fastapi.responses import HTMLResponse
from app.api.dao import ServiceDAO, MasterDAO

router = APIRouter(prefix='', tags=['Фронтенд'])
templates = Jinja2Templates(directory='app/templates')



@router.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    return templates.TemplateResponse("index.html",
                                      {"request": request, "title": "Элегантная парикмахерская"})


@router.get("/form", response_class=HTMLResponse)
async def read_from(request: Request, user_id='', first_name=''):
    return templates.TemplateResponse("form.html",
                                      {"request": request, 
                                       "title": "Форма заявки",
                                       "user_id": user_id,
                                       "first_name": first_name,
                                       "services": await ServiceDAO.find_all(),
                                       "masters": await MasterDAO.find_all(),})