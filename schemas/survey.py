from datetime import datetime

from pydantic import BaseModel


class SurveyResultSchema(BaseModel):
    id: int
    timestamp: datetime | None
    employment_type: str | None
    company_name: str | None
    company_size: str | None
    primary_location_country: str | None
    primary_location_city: str | None
    industry: str | None
    privacy_type: str | None
    overall_experience_years: str | None
    company_experience_years: str | None
    job_title: str | None
    job_ladder: str | None
    required_hours_per_week: str | None
    actual_hours_per_week: str | None
    education_level: str | None
    total_salary: float | None
    total_bonus: float | None
    total_equity: int | None
    has_health_insurance: bool | None
    vacation_weeks: str | None
    happiness_comment: str | None
    resign_comment: str | None
    industry_thoughts: str | None
    gender: str | None
    top_skills_thoughts: str | None
    bootcamp_thoughts: str | None

    class Config:
        orm_mode = True
