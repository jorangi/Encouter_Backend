from sqlalchemy.orm import Session
from typing import List
from database import get_db
from schemas import UnitSchema
from fastapi import FastAPI, Depends, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from models import Unit

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://138.2.109.131:5173",
        "http://localhost:5173",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
    expose_headers=["*"]
)


@app.get("/api/units", response_model=List[UnitSchema])
def get_units(db: Session = Depends(get_db)):
    return db.query(Unit).all()

@app.post('/api/units', response_model=UnitSchema)
def create_unit(unit: UnitSchema, db: Session = Depends(get_db)):
    db_unit = Unit(**unit.model_dump(exclude={"updated_at"}))
    db.add(db_unit)
    db.commit()
    db.refresh(db_unit)
    return db_unit

@app.put("/api/units/{unit_id}", response_model=UnitSchema)
def update_unit(unit_id: str, unit: UnitSchema, db: Session = Depends(get_db)):
    db_unit = db.query(Unit).filter(Unit.id == unit_id).first()
    if not db_unit:
        raise HTTPException(status_code=404, detail="Unit not found")
    update_data = unit.model_dump(exclude={"updated_at", "id"})
    for key, value in update_data.items():
        setattr(db_unit, key, value)
    db.commit()
    db.refresh(db_unit)
    return db_unit

@app.delete("/api/units/{unit_id}")
def delete_unit(unit_id: str, db: Session = Depends(get_db)):
    db_unit = db.query(Unit).filter(Unit.id == unit_id).first()
    if not db_unit:
        raise HTTPException(status_code=404, detail="Unit not found")
    db.delete(db_unit)
    db.commit()
    return {"message": "Successfully deleted"}