from starlette.responses import JSONResponse


async def root(request):
    return JSONResponse({"message": "Hello, World!"})
