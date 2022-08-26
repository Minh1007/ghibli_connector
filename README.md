# APIs

|App Name|URL|Description|HTTP Verb|Parameters|
|:---:|:---:|---|---|---|
|api|/movies|Get movies|list||

# Install
- python version
3.7.x  


- install python dependencies
```
pip install -r requirements.txt
```

- environment varaiables
environment variable are defined in .env but it is listed in gitignore.
.env_backup is pushed to git repo and rename this file .env before run server 


- django commands to set up project
```
python manage.py migrate
python manage.py runserver
```


# Coding style
Code is written according to the PEP8 conventions and refractored code by python black library.

# Test
A test script is written and it has only one case now for a API to get the movies

- django command to run a test 
```
python manage.py test
```


# Technical solution
- Best solution is provided in this project in order not to call ghibli API on every page load.
 There are two ways.
 
 1. Background task can be created that performs sychronizatioin task which pulls data from ghibli API and store those into database every 1 min.
 Then, movies endpoint of this project never call ghibli API on every page load.
 
 2. When a user call movies API of project, it calls ghibli API and process response like broken data like people field of each film and return response. But also, it tries to save the rendered response from movies API of project into cache.
 On every request, it tries to get the page from cache and return it if a user access this API within a minute.
 If not, it tries to call ghibli API and store it into cache. This is implemented easily by using django decorator and cache.
 Cache timeout for ghibli API can be set by django settings.
 
 In view of performance, the second way is better because API can response so fast by using cache.
 So I choosed second way and implemented project in that way.
 
 # Deployment
 I gonna skip any work related to deployment like dockerization, CI/CD.
 But can also provide the solutions to deploy project automatically and can improve this step
 Wherever production server is running (i.e on a vm or kubernetes cluster), project need to be dockerized and github CI/CD pipeline to be made to build docker image.
 And in next step, additional automated process can be added to pull docker image and set up project. 
   
   
 