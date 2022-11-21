# **SHOP K-BEAUTY**


Shop K-Beauty is an e-commerce store for every lover of K-Beauty skincare, hair & body and makeup lines.

![amiresponsive mock-ups of SHOP K-BEAUTY]()

### [Link to the Deployed App]()

![GitHub last commit](https://img.shields.io/github/last-commit/JoyZadan/shop-kbeauty?color=pink&style=for-the-badge)
![GitHub contributors](https://img.shields.io/github/contributors/JoyZadan/shop-kbeauty?color=purple&style=for-the-badge)
![GitHub language count](https://img.shields.io/github/languages/count/JoyZadan/shop-kbeauty?color=blue&style=for-the-badge)
![GitHub top language](https://img.shields.io/github/languages/top/JoyZadan/shop-kbeauty?color=yellow&style=for-the-badge)

# Project Overview

Shop K-Beauty ...


<details>
<summary>
Table of Contents - Click to Expand
</summary>

- [UX DEVELOPMENT](#ux-development)
    - [Strategy](#strategy)
    - [Scope](#scope)
    - [Structure](#structure)
    - [Skeleton](#skeleton)
    - [Features](#features)
- [Technologies Used](#technologies-used)
- [Testing](#testing)
- [Bugs, Issues and Solutions](#bugs-issues-and-solutions)
- [Deployment](#deployment)
- [Credits](#credits)
- [Acknowledgements](#acknowledgements)

</details>

---

# UX Development

## Strategy
### Project Goals
* To develop an App where users can easily find, purchase and add reviews.
* ...

### User Demographic
* Ages 16 and above for viewing, registering and contributing to recipes
* Visitors who are interested in K-Beauty products
* Visitors who are looking for K-Beauty products
* ...

### User Stories
#### First Time Visitor Goals - As a first time user who has not created an account, I want to be able to:
* Immediately understand the main purpose of ...

#### Registered User Goals - As a registered user, I want to be able to:
* ...

#### Site Admin Goals - As an administrator, I want to be able to:
* Have the ability to ...

## Scope
### Feature Ideas Planning
When planning the App features and scope, I drew up an Importance Viability analysis of these features, please see below:

| # | Feature | Importance | Viability |
| --- | --- | --- | --- |
| 1 | ... |  |  |
| 2 | ... |  |  |

Based on the results of the Feature Ideas Planning, I have decided to attempt to implement Features numbers ... for this production release and park the remaining features due to time limitations.

### Functionality Requirements
* ...

## Structure
### Topology Diagrams
...

#### Guest User
![GUEST USER JOURNEY ACROSS THE PALEO RECIPES APP]()

#### Registered User
![REGISTERED USER'S JOURNEY ACROSS THE PALEO RECIPES APP]())

#### Superadmin User
![SUPERADMIN'S PERMISSION AND ACCESS ACROSS THE PALEO RECIPES APP]()

### Database Schema and Structure
Shop K-Beauty is developed using ...

![ERD/DATABASE SCHEMA]()

## Skeleton
### Wireframes
The wireframes created for this project:
- [DESKTOP - INDEX PAGE]()
- ...

### Design
[Bootstrap4]() was used and customised for the front-end development.

#### Colour Scheme
![COLOURS]()

#### Typography
I used Google Fonts to import the fonts I used across the application.
![LATO]()

#### Imagery & UI
![INSERT HERE COLOUR SCHEME]()
The colour scheme and typography used for the Paleo ...

## Features
Breakdown of the features and elements implemented for the App.
### Multi Page Elements
#### Navbar
- ...
- ...

#### Footer
- ...
- ...

#### Home/ Index Page
- ...
- ...

#### Other Pages...
- ...
- ...

#### User and Superadmin Dashboard
- ...
- ...


### Error Handling
The following error handlers were added to the Application to handle possible scenarios requiring specific HTTP Response:
* errorhandler(400) for a Bad Request error
* errorhandler(404) for a 404 Not Found error
* errorhandler(408) for a 408 Request Timeout error
* errorhandler(500) for a 500 Internal Server error

# Technologies Used
* Languages:
    * [DJANGO]() was used ...
    * [DJANGO-ALLAUTH]() was used ...
    * [HTML5](https://en.wikipedia.org/wiki/HTML5) was used for the content and structure of the site.
    * [CSS3](https://en.wikipedia.org/wiki/CSS#CSS_3) was used for the styling of the site.
    * [JavaScript](https://en.wikipedia.org/wiki/JavaScript) was used for the interactivity of the site.
    * [Python](https://www.python.org/) was used for the back end programming of the site.

* [Cloudinary ??? or S3](???) was used to enable users to upload images for their recipes whilst keeping the App safe and secure

* [DB.SQLITE3](https://www.postgresql.org/)
    * SQLITE3 was the relational database used for the project (development).

* [Postgres](https://www.postgresql.org/)
    * Postgres was the relational database used for the project.

* [ELEPHANTSQL](https://www.postgresql.org/)
    * ElephantSQL was used to host the the Postgres DB for the project

* [Flask-PyMongo](https://pypi.org/project/Flask-PyMongo/)
    * Flask-PyMongo provides MongoDB support for Flask applications.

* [pip](https://pip.pypa.io/en/stable/)
    * Pip is the package installer for Python, allowing us to install the packages we need for this site.

* [pillow](https://pip.pypa.io/en/stable/)
    * Pillow is the required Python image library used to enable handling of images.

* [dnspython](https://www.dnspython.org/) -----???
    * Dnspython is a DNS toolkit for python.

* [Balsamiq](https://balsamiq.com/)
    * Balsamiq was used to create the wireframes for this project.

* [Git](https://git-scm.com/)
    * Git was used for version control and saving work in the repository, using the GitPod extension in Google Chrome to commit to GitHub.

* [Bootstrap 4]()
    * Bootstrap is one of the most popular front-end open source toolkit and was used for ease of styling the Earthlings app.

* [Chrome](https://www.google.com/intl/en_uk/chrome/)
    * This project was created in the Google Chrome browser, and as such Chrome was used as the default testing browser.

* [Heroku](https://devcenter.heroku.com/)
    * Heroku is where we deploy this live site. Throughout, we have ensured the version being deployed to Heroku matches the development version by checking features and screen layouts on both versions.

* [GitHub](https://github.com/)
    * GitHub is where we host our site.


## Future Implementation
* Include a ...
* ...


# Testing
## All testing undertaken for this project can be found in the [Testing Document]()

# Bugs, Issues and Solutions
| # | Bugs, Errors and Issues | Solutions |
| :--- | :--- | :--- |
| 1 | Error: You are trying to add a non-nullable field to without a default  | Solution: Choose option 1 from two options provided by Django when making migrations, add timezone.now, then migrate. New error appeared: ```TypeError: Field 'id' expected a number but got datetime.datetime(2022, 11, 20, 13, 54, 36, 590663, tzinfo=<UTC>)```. I then looked for the latest _auto_ file from migrations folder, then changed ```default=got datetime.datetime(2022, 11, 20, 13, 54, 36, 590663, tzinfo=<UTC>)``` to ```default=1```. I was then able to migrate successfully. |
| 2 |   |   |


# Deployment & Local Development

## Deployment to Heroku
To deploy this project, I used Heroku.
1. ...
2. ...

| Key | Value |
| :---: | :---: |
|  |  |
| API_KEY | myapikey |
| API_SECRET | myapisecret |
| IP | 0.0.0.0 |
| PORT | 5000 |
| SECRET_KEY | mysecretkey |
| DATABASE_URL | postgresql |

3. ...
4. ...
5. ...


## Local Development
* How to Fork To fork the repository, use the following steps:
Login or signup to Github and locate the repository.
Click the Fork button in the top right corner
## Making Local Clone
Login or signup to GitHub and locate the GitHub Repository GitHub Repository.
Under the repository name, click "clone" or "download".
To clone the repository using HTTPS, under "Clone with HTTPS", copy the link.
Open the terminal in your preferred code editor and change the current working directory to the location you want to use for the cloned directory.
Type git clone, and then paste the URL you copied in Step 3.
Press Enter. Your clone will be created.

# Credits
## Code

## Content
The product names, images, descriptions and other information were sourced from:
* [SKINSIDER](https://skinsider.co.uk/)
* [STYLEVANA](https://www.stylevana.com/en_GB/)
* [PURESEOUL](https://pureseoul.co.uk/)
* [CULT BEAUTY](https://www.cultbeauty.co.uk/)
* [YESSTYLE](https://www.yesstyle.com/en/home.html)
* [MELON & STARFISH](https://melonandstarfish.com/)
* [K-BEAUTY UK](https://www.k-beauty.co.uk/)
* [UK iHERB](https://uk.iherb.com/)
* [SKINLIBRARY](https://skinlibrary.co.uk/)

The .... for information on the K-Beauty global phenomena.

## Media
* Images used for the project were licensed from Adobe Stock and as per above.

## Resources
1. Code Institute Boutique Ado walkthrough
2. Very Academy
3. Codemy YouTube
4. CodeEx YouTube
5. CodePiep YouTube

# Acknowledgements
A very, very special thanks to my family, especially my daughter Zoe, for your unwavering support and understanding and allowing me the space to focus on my quest to complete my projects and gain my Diploma in Web Application Development (Full Stack).

Special mention and thanks to my mentor, Dario Carrasquel, for his support, invaluable insights and his belief that I can do this well. I am so grateful to have you as my mentor.




# Copyrights
&copy; 2022 SHOP K-BEAUTY by Joy Zadan (An e-commerce Full Stack Developer Project)