from datetime import datetime

from fastapi import APIRouter, Form, HTTPException, Request
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates

from app.services.post_service import PostService
from app.services.user_service import UserService

router = APIRouter()
templates = Jinja2Templates(directory="app/templates")
post_service = PostService()
user_service = UserService()


@router.get("/posts", response_class=HTMLResponse)
async def read_root(request: Request) -> HTMLResponse:
    posts = post_service.get_all_posts()
    return templates.TemplateResponse(
        "index.html",
        {"request": request, "posts": posts},
    )


@router.get("/posts/create", response_class=HTMLResponse)
async def create_post_form(request: Request) -> HTMLResponse:
    return templates.TemplateResponse("create_posts.html", {"request": request})


@router.post("/posts/create", response_class=HTMLResponse)
async def create_post(
    request: Request,
    title: str = Form(...),
    content: str = Form(...),
    author: str = Form("Анонимный автор"),
) -> HTMLResponse:
    try:
        # Создаем новый пост
        new_post = {
            "id": len(post_service.get_all_posts()) + 1,
            "title": title,
            "content": content,
            "author": author,
            "created_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        }
        post_service.create_post(new_post)
        return RedirectResponse(url="/posts", status_code=303)
    except Exception as e:
        return templates.TemplateResponse(
            "create_posts.html",
            {"request": request, "error": f"Ошибка при создании поста: {str(e)}"},
        )


@router.get("/posts/{post_id}", response_class=HTMLResponse)
async def read_post(request: Request, post_id: int) -> HTMLResponse:
    post = post_service.get_post(post_id)
    if not post:
        raise HTTPException(status_code=404, detail="Post not found")
    return templates.TemplateResponse(
        "post.html",
        {"request": request, "post": post},
    )


@router.get("/posts/{post_id}/edit", response_class=HTMLResponse)
async def edit_post_form(request: Request, post_id: int) -> HTMLResponse:
    post = post_service.get_post(post_id)
    if not post:
        raise HTTPException(status_code=404, detail="Post not found")
    return templates.TemplateResponse(
        "edit_post.html",
        {"request": request, "post": post},
    )


@router.post("/posts/{post_id}/edit", response_class=HTMLResponse)
async def edit_post(
    request: Request,
    post_id: int,
    title: str = Form(...),
    content: str = Form(...),
) -> HTMLResponse:
    try:
        updated_data = {"title": title, "content": content}
        post_service.update_post(post_id, updated_data)
        return RedirectResponse(url=f"/posts/{post_id}", status_code=303)
    except Exception as e:
        post = post_service.get_post(post_id)
        return templates.TemplateResponse(
            "edit_post.html",
            {
                "request": request,
                "post": post,
                "error": f"Ошибка при обновлении поста: {str(e)}",
            },
        )
