from sqlalchemy import Column, String, Boolean, DateTime, Enum as SQLAEnum
from sqlalchemy.dialects.postgresql import UUID
from datetime import datetime, timezone
from enums.userRoles import UserRoles
from .base import Base

class User(Base):
    __tablename__ = "user"
    id = Column(UUID(as_uuid=True), primary_key=True, index=True)
    email = Column(String(255), unique=True, index=True, nullable=False)
    role = Column(SQLAEnum(UserRoles), nullable=False, default=UserRoles.employee)
    created_at = Column(DateTime(timezone=True), default=lambda: datetime.now(timezone.utc))