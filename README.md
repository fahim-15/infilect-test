# infilect-test

## Problem Statement

### Python Developer Assignment
Infilect Technologies Private Limited
In this assignment, you are going to build a full-fledged web backend that exposes data (mainly photos)
through APIs. The assignment has two parts. 1) Collecting data and creating your local database 2)
Developing a python Django based backed that will serve the data through RESTful APIs.
For back-end development, we will prefer you if you use Python, Django, SQLite database. Don’t use
php/mysql or any old-school scripting languages/dbs. Note that you will have to write code to
download the data from Flickr API (as described below), store the data into DB, and then expose your
APIs. We have given you sample Flickr APIs that you will need to replicate or enhance when you design
your own application server logic.
Note: Candidates who design and complete all the items with bonus points are most likely to get full-time
employment offer letters with industry-grade salary and equity.
You are about to build an end-to-end version of the Flickr website back-end. When developing backend, please pay attention to db-schema design, Django/web-server API design, writing API logic,
comments to code snippets, extensibility, etc. Include deployment scripts for us to run your solution
quickly.

#### Task 1:
Create a Django project with a SQLite local database. Download images from Flickr API (as discussed
below and fill your database)
Note: You may need to get your own API key if the one in the below sample is not working.

Get Photos from a Group:
https://www.flickr.com/services/api/flickr.groups.pools.getPhotos.html
https://www.flickr.com/services/api/explore/flickr.groups.pools.getPhotos

Example: Use group_id: 80641914@N00
https://api.flickr.com/services/rest/?method=flickr.groups.pools.getPhotos&api_key=678049b504767
e1ad84695ceb8a9fc83&group_id=80641914%40N00&format=json&nojsoncallback=1&api_sig=38e8
bd961be279e8fa22f80eaa73ce8a

Get Photos using ID:
https://www.flickr.com/services/api/flickr.photos.getInfo.html
https://www.flickr.com/services/api/explore/flickr.photos.getInfo

Example: photo_id: 25591028047
https://api.flickr.com/services/rest/?method=flickr.photos.getInfo&api_key=678049b504767e1ad846
95ceb8a9fc83&photo_id=25591028047&format=json&nojsoncallback=1&api_sig=1d9bc918ce3c078c
59b0838475e5a574

You need to create your database models in such a way it mimics these APIs. Store close to 100-
150 images, 4-5 groups and 1 User.

#### Task 2:
Once you have created your database, we require you to develop the following RESTful APIs using
Django Rest Framework.
1) /api/v1/login/ -- This API when called with an username and password should
return a Token
2) /api/v1/groups/ -- This API when called with the appropriate USER TOKEN using
DRF token authentication should return all the groups that below to the user with
details such as group name, group id, number of photos etc.
3) /api/v1/group/<ID> -- This API when called with the appropriate USER TOKEN
using DRF token authentication should return all the photos <ID> belonging to the
group
4) /api/v1/photos/?group=<GID> -- This API when called with the appropriate USER
TOKEN using DRF token authentication and supplying a group id should return all
the photos belonging to the group
5) /api/v1/photos/<ID> -- This API when called with the appropriate USER TOKEN
using DRF token authentication should return details of the photo
6) /api/v1/logout – This API when called with the appropriate USER TOKEN using DRF
token authentication should logout the user and deactivate the token. Using the
same token to authenticate should fail.
  
#### Main considerations
1) Create one username and password and inform us when you are sending your code.
We will use the username/password to authenticate using you login API.
2) APIs 2-6 should all take user token and work only in authenticated mode. If no user
token is passed, it should appropriately show “Authentication Required error”
3) APIs 2, 3, 5 should be properly paginated. Use pagination techniques like limit-offset
pagination to paginate the results. Ideal page size – 30 items
4) For user login and logout – either implement your own methods or use frameworks
like Django Rest Auth (preferable)
5) Permission to access any record should be only by the user who is associated with the
record
6) Use DRF routers to configure all your APIs
7) Take care of REST API version based on Django rest framework versioning methods.
8) As much as you can, create your code is a simple Model, Serializer, ViewSet format.
Structure your code such that it is modular and easy to read and extend 
9) Comment where ever appropriate and make your code easily understandable
10) Provide your output as a runnable Django app. This means

 * a. A proper requirements.txt file with all the pip dependencies should be
present. We will create a virtualenv and install only the dependencies that you
provide in the requirements file. The Django app should run within the
virtualenv.
  * b. The populated SQLite database should be included and properly configured in
Django settings
  * c. Any other tools or deployment script should be included
Testing your app

We will run your Django app under the virtualenv which has all the libraries you have
specified in your requirements file using 
python manage.py runserver 0.0.0.0:8000 and your
app should be available on the machine we run and all the APIs should be fully functional.
