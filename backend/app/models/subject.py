from sqlalchemy import CheckConstraint, Integer, Numeric, SmallInteger, String
from decimal import Decimal

from sqlalchemy import Integer, Numeric, SmallInteger, String
from sqlalchemy.orm import Mapped, mapped_column

from app.db.base import Base


class Subject(Base):
    __tablename__ = "subjects"
    __table_args__ = (
        CheckConstraint(
            "semester BETWEEN 1 AND 12",
            name="ck_subjects_semester",
        ),
        CheckConstraint(
            "credits > 0",
            name="ck_subjects_credits",
        ),
        CheckConstraint(
            "maximum_marks > 0 AND pass_marks BETWEEN 0 AND maximum_marks",
            name="ck_subjects_marks",
        ),
    )

    subject_id: Mapped[int] = mapped_column(Integer, primary_key=True)
    subject_code: Mapped[str] = mapped_column(
        String(30), unique=True, nullable=False
    )
    subject_name: Mapped[str] = mapped_column(
        String(150), nullable=False
    )
    department: Mapped[str] = mapped_column(String(20), nullable=False)
    semester: Mapped[int] = mapped_column(SmallInteger, nullable=False)
    credits: Mapped[Decimal] = mapped_column(
        Numeric(3, 1), nullable=False
    )
    maximum_marks: Mapped[Decimal] = mapped_column(
        Numeric(6, 2), nullable=False
    )
    pass_marks: Mapped[Decimal] = mapped_column(
        Numeric(6, 2), nullable=False
    )
