from database import SessionLocal
from models import Department
from sqlalchemy.orm import selectinload

def add_1_khoa(name: str):
    """Thêm user mới vào database."""
    with SessionLocal() as db:
        new_record = Department(name=name)
        db.add(new_record)
        db.commit()
        db.refresh(new_record)
        print(f"sick ID: {new_record.id}")


def get_all_khoa():
    with SessionLocal() as db:
        departments = (
            db.query(Department)
            .options(
                selectinload(Department.users),
                selectinload(Department.doctors),
                selectinload(Department.rooms)
            )
            .all()
        )
        print(departments)
    return departments

