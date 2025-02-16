from sqlalchemy import Column, Integer, Float, String, ForeignKey
from sqlalchemy.orm import relationship
from database import declarative_base

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name = Column(String, nullable=False)
    phone = Column(String, nullable=False)
    address = Column(String, nullable=False)
    relative = Column(String, nullable=False)
    job = Column(String, nullable=False)
    sex = Column(String, nullable=False)
    active = Column(String, nullable=False)
    note = Column(String, nullable=False)
    department_id = Column(Integer, ForeignKey('departments.id'), nullable=True)
    room_id = Column(Integer, ForeignKey('rooms.id'), nullable=True)
    sick_id = Column(Integer, ForeignKey("sicks.id", ondelete="SET NULL"), nullable=True, index=True) 
    doctor_id = Column(Integer, ForeignKey('doctors.id'), nullable=True)

    # Quan hệ
    health_data = relationship("HealthData", back_populates="user")
    sick = relationship("Sick", back_populates="users")  # 1-N với Sick
    room = relationship("Room", back_populates="users")  # 1-N với Room
    bed = relationship("Bed", back_populates="user", uselist=False)  # 1-1 với Bed
    department = relationship("Department", back_populates="users")  # 1-N với Department
    doctor = relationship("Doctor", back_populates="users")  # 1-N với Doctor

class HealthData(Base):
    __tablename__ = "health_data"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    heartRate = Column(Float, nullable=False)
    spo2 = Column(Float, nullable=False)
    
    user_id = Column(Integer, ForeignKey('users.id', ondelete="CASCADE"), nullable=False, index=True)  
    user = relationship("User", back_populates="health_data")

class Doctor(Base):
    __tablename__ = 'doctors'

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name = Column(String, nullable=False)
    phone = Column(String, nullable=False)
    department_id = Column(Integer, ForeignKey('departments.id'), nullable=True)
    position = Column(String, nullable=False)

    users = relationship("User", back_populates="doctor")  
    department = relationship("Department", back_populates="doctors")

class Sick(Base):
    __tablename__ = 'sicks'

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name = Column(String, nullable=False)

    users = relationship("User", back_populates="sick")  

class Room(Base):
    __tablename__ = 'rooms'

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    department_id = Column(Integer, ForeignKey('departments.id'), nullable=True)
    room_number = Column(String, nullable=False)
    phone = Column(String, nullable=False)

    beds = relationship("Bed", back_populates="room")  
    users = relationship("User", back_populates="room")  
    department = relationship("Department", back_populates="rooms")

class Bed(Base):
    __tablename__ = 'beds'
    
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    room_id = Column(Integer, ForeignKey('rooms.id'), nullable=True)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False, unique=True)

    room = relationship("Room", back_populates="beds")  
    user = relationship("User", back_populates="bed")  

class Department(Base):
    __tablename__ = 'departments'

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name = Column(String, nullable=False)

    users = relationship("User", back_populates="department")  # 1-N với User
    doctors = relationship("Doctor", back_populates="department")  # 1-N với Doctor
    rooms = relationship("Room", back_populates="department")  # 1-N với Room
