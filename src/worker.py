from fastapi import FastAPI


async def on_fetch(request, env):
    import asgi

    return await asgi.fetch(app, request, env)


app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello from Python!"}


@app.get("/hello/{name}")
async def hello(name: str):
    import jinja2

    environment = jinja2.Environment()
    template = environment.from_string("Hello, {{ name }}!")
    message = template.render(name=name)
    return {"message": message}


@app.get("/version")
async def version():
    import cffi

    return {"version": cffi.__version__}
