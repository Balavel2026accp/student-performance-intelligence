from datetime import date

from sqlalchemy import Boolean, CheckConstraint, Date, Integer, String
from sqlalchemy.orm import Mapped, mapped_column

from app.db.base import Base


class AcademicYear(Base):
    __tablename__ = "academic_years"

    __table_args__ = (
        CheckConstraint(
            "end_date >= start_date",
            name="ck_academic_year_dates",
        ),
    )

    academic_year_id: Mapped[int] = mapped_column(Integer, primary_key=True)
    year_name: Mapped[str] = mapped_column(String(20), unique=True, nullable=False)
    start_date: Mapped[date] = mapped_column(Date, nullable=False)
    end_date: Mapped[date] = mapped_column(Date, nullable=False)
    is_current: Mapped[bool] = mapped_column(Boolean, nullable=False, default=False)
