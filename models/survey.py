from sqlalchemy import Column, DateTime, String, Integer, BigInteger, Boolean, Float

from models.base import Base


class SurveyResult(Base):
    __tablename__ = "survey_result"

    id = Column(BigInteger, primary_key=True)
    timestamp = Column(DateTime(timezone=True))
    employment_type = Column(String)
    company_name = Column(String)
    company_size = Column(String)
    primary_location_country = Column(String)
    primary_location_city = Column(String)
    industry = Column(String)
    privacy_type = Column(String)
    overall_experience_years = Column(String)
    company_experience_years = Column(String)
    job_title = Column(String)
    job_ladder = Column(String)
    job_level = Column(String)
    required_hours_per_week = Column(String)
    actual_hours_per_week = Column(String)
    education_level = Column(String)
    total_salary = Column(Float)
    total_bonus = Column(Float)
    total_equity = Column(Float)
    has_health_insurance = Column(Boolean)
    vacation_weeks = Column(String)
    happiness_comment = Column(String)
    resign_comment = Column(String)
    industry_thoughts = Column(String)
    gender = Column(String)
    top_skills_thoughts = Column(String)
    bootcamp_thoughts = Column(String)