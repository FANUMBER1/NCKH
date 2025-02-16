from database import SessionLocal
from models import Sick

def add_sick(name: str):
    """Thêm user mới vào database."""
    with SessionLocal() as db:
        new_record = Sick(name=name)
        db.add(new_record)
        db.commit()
        db.refresh(new_record)
        print(f"sick ID: {new_record.id}")

def get_all_sick():
    """Lấy toàn bộ dữ liệu từ bảng Sick."""
    with SessionLocal() as db:
        sick_records = db.query(Sick).all()
        return sick_records
