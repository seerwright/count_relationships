# Count Relations on Girthy Data
Given data that is about 33 million records in one 
table and 168 million records in another table, join the tables
on a single key and report out the counts of Relations
for each user bin.

The challenge is that the data may be too large to work with. The 
goal of this repo is to show that it is not too big with the right 
tools. This repo runs on a laptop running Linux with 32 GB memory.

## Approach
1. Create mock data. This is done with `generate_data.py`.
2. Join and report. This is done with `analyze_data.ipynb`.

## Limitations
* I don't know what the data look like that someone might apply this technique to. The actual data, schema, and relations matter for performance.
* This example uses DuckDB, an in-memory database, and basic SQL. It should be portable to most databases, but different databases may have different SQL implementations and/or resource management. 
* Not a limitation, but one gotcha is that I may have misunderstood the nature of the problem. I.e. I might have solved a different problem than the one that needs to be solved. 

## Performance
* Data generation. Reproducing the data can be done by simplying running `python generate_data.py` after you've installed the necessary packages via pip. A rough estimate on the time required to generate data:
  * About 2 minutes to generate and write user data. The resulting file will be `table_users.csv` and will be approximately 2.2 GB. 
  * About 3 minutes to generate and write the related data. The resulting file will be `table_user_brands.csv` and will be approximately 5.1 GB.
* Joining and reporting. This analysis can be done with the notebook by running `jupyter notebook` and opening the `analyze_data.ipynb` file. 
  * Each cell is self explanatory. Just run them in order.
  * Loading the data into memory will take less than a minute.
  * Running the SQL join will also take less than a minute. 
  * The bins with counts are reported on the last cell of the notebook.

## How to run
You can just look at the notebook in Github to see the results. There is no need to regengerate the data. 

If you want to regenerate the data:
1. Clone the repo
2. Create a Python virtual environment in the project directory
3. Source the new venv
4. Install packages via pip:
   * jupyter
   * pandas
   * pyarrow
   * duckdb
   * numpy
5. Run `generate_data.py`
6. Run Jupyter and open `analyze_data.ipynb`

## Table Schemas
### Users table (33 million rows)
* user_id: int64
* first_name: str
* last_name: str
* email: str
* favorite_color: str
* birth_year: int64
* is_adult: bool

### User_Brands table (160-170 million rows, stochastic)
* user_brand_id: int64
* user_id: int64
* brand_event_name: str