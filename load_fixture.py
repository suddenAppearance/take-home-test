import csv

from models import create_session, SurveyResult

file = open("fixtures/salary_survey.csv", "r")

reader = csv.reader(file)
next(reader)  # skip headers
next(reader)  # skip empty line

session = create_session()

for row in reader:
    data = [element if element != "" else None for element in row]
    for i, element in enumerate(data):
        if element == "Yes":
            data[i] = True
        if element == "No":
            data[i] = False
        if element == "N/A":
            data[i] = None

    columns = [
        "timestamp",
        "employment_type",
        "company_name",
        "company_size",
        "primary_location_country",
        "primary_location_city",
        "industry",
        "privacy_type",
        "overall_experience_years",
        "company_experience_years",
        "job_title",
        "job_ladder",
        "job_level",
        "required_hours_per_week",
        "actual_hours_per_week",
        "education_level",
        "total_salary",
        "total_bonus",
        "total_equity",
        "has_health_insurance",
        "vacation_weeks",
        "happiness_comment",
        "resign_comment",
        "industry_thoughts",
        "gender",
        "top_skills_thoughts",
        "bootcamp_thoughts",
    ]
    session.add(SurveyResult(**dict(zip(columns, data))))
    session.commit()
