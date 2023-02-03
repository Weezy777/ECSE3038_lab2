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

@app.patch("/todos"):
async def update_todo_by_id(id, todo_request, fake_database):
    for todo in todo_list:
        if todo['id'] == id:
            todo.update(todo_request)
            return todo, 200
    return None, 404

todo_list = [{"id": 1, "task": "Take out the trash", "isDone": False},
             {"id": 2, "task": "Buy groceries", "isDone": False}]

todo_request = {"isDone": True}
todo, status = update_todo_by_id(1, todo_request, todo_list)

if status == 200:
    print("Todo updated: ", todo)
else:
    print("Todo not found")