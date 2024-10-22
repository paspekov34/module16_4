from fastapi import FastAPI, Path, HTTPException
from typing import Annotated
from pydantic import BaseModel
from typing import List

app = FastAPI()


users = []


class User(BaseModel):
    id: int = None
    username: str
    age: int = None

@app.get("/users")
async def user_get() -> List[User]:
    return users


@app.post("/user/{username}/{age}")
async def user_post(user: User, username: Annotated[str, Path(min_length=5, max_length=20, description="Enter username")],
                    age: Annotated[int, Path(ge=18, le=120, description="Enter age")]) -> User:
    len_user = len(users)
    if len_user == 0:
        user.id = 1
    else:
        user.id = users[len_user - 1].id + 1
    user.username = username
    user.age = age
    users.append(user)
    return user



@app.put('/user/{user_id}/{username}/{age}')
async def user_put(user_id: int, username: str, age: int):
    raise1 = True
    for edit_user in users:
        if edit_user.id == user_id:
            edit_user.username = username
            edit_user.age = age
            return edit_user
    if raise1:
        raise HTTPException(status_code=404, detail='User was not found')


@app.delete('/user/{user_id}')
async def delete_user(user_id: int):
    raise2 = True
    ind_del = 0
    for delete_user in users:
        if delete_user.id == user_id:
            users.pop(ind_del)
            return delete_user
        ind_del += 1
    if raise2:
        raise HTTPException(status_code=404, detail='User was not found')
