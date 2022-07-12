from asyncapi import get_asyncapp
from myapp import get_app
from fastapi import FastAPI

my_app: FastAPI = FastAPI()

app = get_app(my_app)
app = get_asyncapp(app)

if __name__ == '__main__':
    import uvicorn

    uvicorn.run(app='main:app',
                host="127.0.0.1",
                port=8000,
                reload=True,
                debug=True)
