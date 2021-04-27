# One Page Portfolio
A portfolio that displays a customizable message along with a showcase of programming projects.  

## Deployment
Dependencies must be installed through `pip -r requirements.txt`.  
One Page Portfolio can be run locally for testing purposes through the following commands:  
- `python manage.py migrate`
- `python manage.py collectstatic`
- `python manage.py runserver`  
Debugging should be turned on in portfolio/settings.py to help diagnose problems when changes are made.  
  
Deployment to heroku can be done by creating a new app, enabling the heroku-postgresql addon (free version), changing the `heroku_deploy` variable to True in portfolio/settings.py and deploying through the heroku cli or github repository. Debugging must be turned off for heroku deployment.  
  
## Configuring
Adding projects and changing the landing message is done through the admin panel at {projecturl}/admin. A superuser must be created to log-in to the admin panel through command line using `python manage.py createsuperuser`. Navbar links can be edited at projects/templates/project_index.html  
Default images for projects and the user are provided, but additional photos must be added to the corresponding directories.  
  
## Fields
- Project: Every field but 'title' and 'slug' is optional.
  - title: The name of the project.
  - short: A few words describing the project.
  - description: A long description that display on the project's modal popup.
  - technology: Languages and tools used in creating the project.
  - image: A image of the project in action.
  - url: A url to the project's source code repository.
  - demo: A url that points to a live demo version of the project.
  - slug: A unique project identifier that is auto-generated. May be changed manually to avoid conflicts when adding two projects with the same title.  
   
- LandingMessage: Every field but 'name' is optional.
  - name: Your name.
  - header:  A short headline describing your skills and/or experience.
  - description: Can be used as a welcoming message or a further elaboration on skills and experience.
  - image: An image that represents you.
