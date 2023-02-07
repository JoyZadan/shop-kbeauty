# **Shop K-Beauty Deployment**

![amiresponsive mock-ups of SHOP K-BEAUTY](./documentation/responsiveness/am-i-responsive-new.png)

<br/>

**[Link to the Deployed Site](https://shop-k-beauty-django-joy-zadan.herokuapp.com/)**

---
Shop K-Beauty is deployed on Heroku.

## **Deployment Steps**
1. **Install the project requirements by creating a Pipfile**
In the terminal, enter the command ```pip3 freeze > requirements.txt ``` and a file with all the requirements will be created.

2. **Create an external database on ElephantSQL.com**
The sqlite3 database that came with Django and which we have been using is only available for use in development. We need to create a new database that is suitable for production.
* Go to [ElephantSQL.com](https://www.elephantsql.com/) and click *Get a managed database today* button.
* Select Tiny Turtle by pressing the *Try now for FREE* button
* Select *Log in with GitHub* and authorize ElephantSQL with your selected GitHub account
* In the create new team form:
    * Add a *team name* (your own name is fine)
    * Read and agree to the Terms of Service
    * Select *Yes* for GDPR
    * Provide your email address
    * Click *Create Team*
* Click *Create New Instance*

If you already have an account, after logging in to ElephantSQL:
* Set up your plan
    * Give your plan a **Name** (This is commonly the name of the project)
    * Select *Select Region*
    * Select a region and data center (Choose the one closest to you)
    * Click *Review*
    * Check that your details are correct and then click *Create New Instance*
    * Return to the dashboard and click on the *database instance name*
    * Copy the database url

3. **Set up Heroku**
* Go to [Heroku.com](https://www.heroku.com/) and log in
* Choose the New button and from the dropdown, select *Create new app*
* Add your preferred app name and select your location and click the create app button
* Add the **DATABASE_URL** Config Var by going to the settings tab
* Click *Reveal Config Vars*
* Add a Config Var **DATABASE_URL** and paste your ElephantSQL database URL in as the value

4. **Connect the external database to GitPod**
* In your **env.py** file add a new key, **DATABASE_URL** and give it the value of the copied database URL <br/>
```bash
os.environ.setdefault("DATABASE_URL", "the_copied_database_url")
```
* Install the **dj-database-url** package version 0.5.0 and **psycopg2** in the terminal with **pip3** to allow us to parse the URL we have copied above to a format that Django can work with: <br/>
```bash
pip3 install dj_database_url==0.5.0 psycopg2
```
and remember to add both to your **requirements.txt** file with: <br/>
```bash
pip3 freeze --local > requirements.txt
```
* At the top of the **settings.py** file, import **dj_database_url** underneath the import for os <br/>
```python
import os
import dj_database_url
```
* In the **settings.py** file, comment out the default database setting and replace it to use the **DATABASE_URL** environment variable <br/>
```python
DATABASES = {
    'default': dj_database_url.parse(os.environ.get('DATABASE_URL'))
}
```
* Run the showmigrations command in the terminal to confirm you are connected to the external database
```bash
python3 manage.py showmigrations
```
**Note:** this does not transfer the data, only the database structure
* If you are connected to the external database, you should see a list of migrations, but none of them are checked off
* Run the migrate command in the terminal
```bash
python3 manage.py migrate
```
**FIXTURES**
If you did not use fixtures to populate your database, but instead manually added all your data via the Django admin, we now need to *transfer* the data from GitPod to your new database and we are going to do this using the **dumpdata** command.


If you used fixtures for your project, you can start to load in the fixtures here.
**Note:** the order in which you load the fixtures is very important. This is the order we need to follow for this project:
1. load the maincategories
```bash
python3 manage.py loaddata maincategories
```
2. load the categories
```bash
python3 manage.py loaddata categories
```
3. load the subcategories
```bash
python3 manage.py loaddata subcategories
```
4. load the brands
```bash
python3 manage.py loaddata brands
```
5. finally, we can load the products
```bash
python3 manage.py loaddata products
```
If you also created product reviews, you would need to first:
6. create a superuser for your new database
```bash
python3 manage.py createsuperuser
```
Follow the steps to create your superuser username and password.





* Run the project to test everything is connected correctly:
```bash
python3 manage.py runserver
```
