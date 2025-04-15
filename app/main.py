from fastapi import FastAPI
from app.routers import mail, map, payment, checkPayment

app = FastAPI()

# Include routers
app.include_router(mail.router, prefix="/api", tags=["Mail"])
app.include_router(map.router, prefix="/api", tags=["Map"])
app.include_router(payment.router, prefix="/api", tags=["Payment"])
app.include_router(checkPayment.router, prefix="/api", tags=["updatePayment"])

@app.get("/")
async def root():
    return {"message": "Welcome to the combined FastAPI app"}
