from fastapi import APIRouter
from fastapi.templating import Jinja2Templates
from fastapi.requests import Request
from fastapi.responses import HTMLResponse

from app.api.dao import MasterDAO, ServiceDAO

router = APIRouter(prefix='', tags=['Фронтенд'])
templates = Jinja2Templates(directory='app/templates')


@router.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    return templates.TemplateResponse("index.html",
                                      {"request": request, "title": "Студия маникюра RumNails"})


@router.get("/form", response_class=HTMLResponse)
async def read_root(request: Request, user_id: int = None, first_name: str = None):
    masters = await MasterDAO.find_all()
    services = await ServiceDAO.find_all()
    data_page = {"request": request,
                 "user_id": user_id,
                 "first_name": first_name,
                 "title": "Запись на услуги - RumNails",
                 "masters": masters,
                 "services": services}
    return templates.TemplateResponse("form.html", data_page)

