# DataProject Django rest framework

## Aim
Plot dynamic graph using Django API.

## Requirements
1. Internet Browser
2. Internet Connection
3. Python Version 3.7+
4. Postgresql
5. List of all the dependencies in **requirements.txt**

## How To Get Data
1. To download the data [click here](https://www.kaggle.com/manasgarg/ipl/version/5). Here you will get two data files.
2. Third data file is present in the project itself.


## How To Run
1. Clone the project `https://gitlab.com/mountblue/cohort-14-python/ankit_singh/dataproject-django-rest-framework`
2. Copy and paste the two downloaded CSV files in the **project directory**.
3. Open a terminal in the project directory.
4. Create a virtual environment for the project.
    * Run `python3 -m virtualenv env` to create virtualenv.
    * Run `source env/bin/activate`.
5. Install all the dependencies. Run `pip install -r requirements.txt`
6. Setup role and database in Postgres.
    * Run `sudo -u postgres psql`
    * Create role and database `\i create.sql;`
    * To close postgres `\q`
7. Run `python manage.py migrate` in the project terminal to create tables.
8. Run `python manage.py dataset umpire.csv deliveries.csv matches.csv` in terminal.
9. Run `python manage.py runserver`.
10. Click on the link which is coming is the terminal.
11. For clean up role and database.
    * Run `sudo -u postgres psql`
    * Drop role and database `\i drop.sql;`
    * To close postgres `\q`

**Note**: Don't plot graphs when you are logged in as admin.