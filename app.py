from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = [
    "https://ecse-week3-demo.netlify.app"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

fake_database = []

@app.get("/todos")
async def get_all_todos():
  return fake_database

@app.post("/todos")
async def create_todo(request: Request):
  todo = await request.json()
  fake_database.append(todo)
  return todo

@app.patch("/todos/{id}")
async def update_todo_by_id(id:int, todo_request: Request):
    todo_update = await todo_request.json()
    for todo in fake_database:
        if todo['id'] == id:
            print(todo)
            todo.update(todo_update)
            return todo, 200
    return None, 404

