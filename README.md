# Python take-home-test

Expose an API for querying salary data:

- The goal of this exercise is to design a read-only API (REST) that returns one or more records from the provided dataset
- Filter by one or more fields/attributes (e.g. /compensation_data?salary[gte]=120000&zip_code=11201 )
- Sort by one or more fields/attributes (e.g. /compensation_data?sort=last_name)
- Stretch Goal: return a sparse fieldset (e.g. /compensation_data?fields=first_name,last_name,salary)
- Don't worry about any web application concerns other than serializing JSON and returning via a GET request.
