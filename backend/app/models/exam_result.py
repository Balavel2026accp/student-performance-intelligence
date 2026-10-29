from sqlalchemy import (
    CheckConstraint,
    Date,
    ForeignKey,
    Index,
    Integer,
    Numeric,
    SmallInteger,
    String,
)
from datetime import date
from decimal import Decimal

from sqlalchemy import Date, ForeignKey, Integer, Numeric, SmallInteger, String
from sqlalchemy.orm import Mapped, mapped_column

from app.db.base import Base


class ExamResult(Base):
    __tablename__ = "exam_results"
    __table_args__ = (
        CheckConstraint(
            "semester BETWEEN 1 AND 12",
            name="ck_exam_results_semester",
        ),
        CheckConstraint(
            "marks_obtained BETWEEN 0 AND maximum_marks",
            name="ck_exam_results_marks",
        ),
        CheckConstraint(
            "maximum_marks > 0",
            name="ck_exam_results_maximum_marks",
        ),
        CheckConstraint(
            "result_status IN ('Pass', 'Fail')",
            name="ck_exam_results_status",
        ),
        Index("ix_results_student_year", "student_id", "academic_year_id"),
        Index("ix_results_subject_year", "subject_id", "academic_year_id"),
    )

    result_id: Mapped[int] = mapped_column(Integer, primary_key=True)
    student_id: Mapped[int] = mapped_column(
        ForeignKey("students.student_id"), nullable=False
    )
    subject_id: Mapped[int] = mapped_column(
        ForeignKey("subjects.subject_id"), nullable=False
    )
    academic_year_id: Mapped[int] = mapped_column(
        ForeignKey("academic_years.academic_year_id"), nullable=False
    )
    semester: Mapped[int] = mapped_column(SmallInteger, nullable=False)
    exam_type: Mapped[str] = mapped_column(String(20), nullable=False)
    marks_obtained: Mapped[Decimal] = mapped_column(
        Numeric(6, 2), nullable=False
    )
    maximum_marks: Mapped[Decimal] = mapped_column(
        Numeric(6, 2), nullable=False
    )
    grade: Mapped[str] = mapped_column(String(5), nullable=False)
    result_status: Mapped[str] = mapped_column(String(10), nullable=False)
    exam_date: Mapped[date] = mapped_column(Date, nullable=False)
