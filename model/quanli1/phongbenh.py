from database import SessionLocal
from models import Room
from sqlalchemy.orm import selectinload
def add_rooms(name: str, department_id:int, note:str):
    """Thêm user mới vào database."""
    with SessionLocal() as db:
        new_record = Room(room_number=name,department_id=department_id,phone=note)
        db.add(new_record)
        db.commit()
        db.refresh(new_record)
        print(f"sick ID: {new_record.id}")

def get_all_room():
    """Lấy toàn bộ dữ liệu từ bảng Room."""
    with SessionLocal() as db:
        sick_records = (db.query(Room)
            .options(
                selectinload(Room.users),
                selectinload(Room.department),
            )
            .all()
        )
        return sick_records
def delete_rooms(id:int):
    with SessionLocal() as db:
        doctor = db.query(Room).filter(Room.id == id).first()
        db.delete(doctor)
        db.commit()
