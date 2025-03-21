from contextlib import asynccontextmanager
from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware

from server.auth.auth_bearer import JWTBearer
from server.routes.jwt_token import router as JwtRouter
from server.routes.item import router as ItemRouter
from server.routes.order import router as OrderRouter
from server.utils.csv_import_to_mysql import mysql_import

@asynccontextmanager
async def lifespan(app: FastAPI):
    mysql_import()
    yield
    # Clean up

app = FastAPI(root_path="/api/v1", lifespan=lifespan)

origins = [
    "http://localhost:3000",
    "http://127.0.0.1:3000",
    "http://localhost:8080",
    # change ip to the machine running this app to test front app on stand-alone mobile
    "http://192.168.1.45:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.include_router(JwtRouter, tags=["JWT Token"], prefix="/token")
app.include_router(ItemRouter, tags=["Item"], prefix="/item", dependencies=[Depends(JWTBearer())])
app.include_router(OrderRouter, tags=["Order"], prefix="/order", dependencies=[Depends(JWTBearer())])

@app.get("/", tags=["Root"])
async def read_root():
    return {"message": "Project Raven is running on PORT:8000"}
