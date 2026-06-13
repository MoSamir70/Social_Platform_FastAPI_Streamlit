import uvicorn



if __name__ == "__main__":
    uvicorn.run("app.app:app", host="127.0.0.1", port=8000, reload=True)

# app.app:app --> folder.file : variable of fastapi

# http://127.0.0.1:8000
# http://127.0.0.1:8000/docs
# http://127.0.0.1:8000/redoc --> redoc
# http://127.0.0.1:8000/hello_world

