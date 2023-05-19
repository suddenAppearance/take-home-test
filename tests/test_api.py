import pytest


@pytest.mark.parametrize(
    "filters",
    (
        {},  # no filters
        {"id": 1},
        {"has_health_insurance": 'null'},  # eq NULL
        {"has_health_insurance": False},  # eq bool
        {"total_salary": 61800},  # eq int
        {"total_salary[gte]": 10000},  # gte int
        {"total_salary[lte]": 10000},  # lte int
        {"primary_location_city": "London"},  # eq str
    )
)
@pytest.mark.parametrize(
    "sort",
    (
        None,
        "id",
        "id desc",
        "id asc desc",

        "total_salary",  # int
        "company_name",  # str
        "has_health_insurance",  # bool
        ["total_salary", "company_name"]  # multiple
    )
)
@pytest.mark.parametrize(
    "fields",
    (
        None,
        "id",
        "company_name",
        ["company_name", "vacations_weeks"]
    )
)
def test_get_all(client, filters, sort, fields):
    params = filters
    if sort:
        params["sort"] = sort
    if fields:
        params["fields"] = fields
    response = client.get("/api/v1/compensation_data", params=filters)
