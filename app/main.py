from fastapi import FastAPI
from app.database import Base, engine
from app.routes.transaction import router

# ✅ database table create करेगा
Base.metadata.create_all(bind=engine)

# ✅ FastAPI app create
app = FastAPI()

# ✅ routes जोड़ना
app.include_router(router, prefix="/transactions", tags=["Transactions"])