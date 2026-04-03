from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from sqlalchemy import func
from app.database import get_db
from app.models.transaction import Transaction
from app.schemas.transaction_schema import TransactionCreate

router = APIRouter()

# ✅ Create Transaction (POST)
@router.post("/")
def create_transaction(data: TransactionCreate, db: Session = Depends(get_db)):
    txn = Transaction(**data.dict())
    db.add(txn)
    db.commit()
    db.refresh(txn)
    return txn


# ✅ Get All Transactions (GET)
@router.get("/")
def get_transactions(db: Session = Depends(get_db)):
    return db.query(Transaction).all()


#FILTER
@router.get("/filter")
def filter_transactions(type: str = None, category: str = None, db: Session = Depends(get_db)):
    query = db.query(Transaction)

    if type:
        query = query.filter(func.lower(Transaction.type) == type.lower())

    if category:
        query = query.filter(func.lower(Transaction.category) == category.lower())

    return query.all()


@router.get("/summary")
def get_summary(db: Session = Depends(get_db)):
    transactions = db.query(Transaction).all()

    total_income = 0
    total_expense = 0

    for t in transactions:
        if t.type.lower() == "income":
            total_income += t.amount
        elif t.type.lower() == "expense":
            total_expense += t.amount

    return {
        "total_income": total_income,
        "total_expense": total_expense,
        "balance": total_income - total_expense
    }


# ✅ UPDATE
@router.put("/{id}")
def update_transaction(id: int, data: TransactionCreate, db: Session = Depends(get_db)):
    txn = db.query(Transaction).filter(Transaction.id == id).first()

    if not txn:
        raise HTTPException(status_code=404, detail="Transaction not found")

    txn.amount = data.amount
    txn.type = data.type
    txn.category = data.category

    db.commit()
    db.refresh(txn)

    return txn


# ✅ DELETE
@router.delete("/{id}")
def delete_transaction(id: int, db: Session = Depends(get_db)):
    txn = db.query(Transaction).filter(Transaction.id == id).first()

    if not txn:
        raise HTTPException(status_code=404, detail="Transaction not found")

    db.delete(txn)
    db.commit()

    return {"message": "Transaction deleted"}



    