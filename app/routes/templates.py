from fastapi import APIRouter, Request, Form, HTTPException
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse, RedirectResponse
from app.services.post_service import post_service
from app.models.post import PostCreate, PostUpdate

router = APIRouter(prefix="", tags=["pages"])
templates = Jinja2Templates(directory="app/templates")

# ГЛАВНАЯ СТРАНИЦА
@router.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    posts = await post_service.get_all_posts()
    return templates.TemplateResponse("index.html", {
        "request": request, 
        "posts": posts
    })

# ФОРМА СОЗДАНИЯ ПОСТА - ДОЛЖЕН БЫТЬ ВЫШЕ!
@router.get("/posts/create", response_class=HTMLResponse)
async def create_post_form(request: Request):
    return templates.TemplateResponse("create_posts.html", {"request": request})

# СОЗДАНИЕ ПОСТА (POST)
@router.post("/posts/create", response_class=HTMLResponse)
async def create_post(
    request: Request,
    author_id: int = Form(...),
    title: str = Form(...),
    content: str = Form(...)
):
    try:
        post_data = PostCreate(title=title, content=content)
        post = await post_service.create_post(author_id, post_data)
        posts = await post_service.get_all_posts()
        return templates.TemplateResponse("index.html", {
            "request": request, 
            "posts": posts,
            "message": "Пост успешно создан!"
        })
    except Exception as e:
        return templates.TemplateResponse("create_posts.html", {
            "request": request,
            "error": str(e)
        })

# ПРОСМОТР КОНКРЕТНОГО ПОСТА - ДОЛЖЕН БЫТЬ НИЖЕ!
@router.get("/posts/{post_id}", response_class=HTMLResponse)
async def read_post(request: Request, post_id: int):
    post = await post_service.get_post_by_id(post_id)
    return templates.TemplateResponse("post.html", {"request": request, "post": post})

# РЕДАКТИРОВАНИЕ ПОСТА
@router.get("/posts/{post_id}/edit", response_class=HTMLResponse)
async def edit_post_form(request: Request, post_id: int):
    post = await post_service.get_post_by_id(post_id)
    return templates.TemplateResponse("edit_post.html", {"request": request, "post": post})

@router.post("/posts/{post_id}/edit", response_class=HTMLResponse)
async def edit_post(
    request: Request,
    post_id: int,
    title: str = Form(...),
    content: str = Form(...)
):
    try:
        post_data = PostUpdate(title=title, content=content)
        post = await post_service.update_post(post_id, post_data)
        
        return RedirectResponse(f"/posts/{post_id}?message=Пост успешно обновлен", status_code=303)
    except Exception as e:
        post = await post_service.get_post_by_id(post_id)
        return templates.TemplateResponse("edit_post.html", {
            "request": request,
            "post": post,
            "error": str(e)
        })