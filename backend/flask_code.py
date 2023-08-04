# Flask Imports 
from flask import Flask
from flask import request
from flask_sqlalchemy import SQLAlchemy
from flask_restful import Resource, Api, reqparse
from flask import make_response
from flask_cors import CORS
from flask import jsonify
from flask import render_template

# Celery Import
from celery import Celery
from celery.schedules import crontab

# Other Imports
import os
import requests
import pandas as pd
from json import dumps
from httplib2 import Http

# imports for email
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders

# Caching and Performance Imports
from time import perf_counter
from flask_caching import Cache

##########################################################################################

# Configuration for email
SMPTP_SERVER_HOST = "localhost"
SMPTP_SERVER_PORT = 1025
SENDER_ADDRESS = "admin@localhost"
SENDER_PASSWORD = ""


# Configuration for caching
CACHE_TYPE = "RedisCache"
CACHE_REDIS_HOST = "localhost"
CACHE_REDIS_PORT = 6379


# path for the database
basedir = os.path.abspath(os.path.dirname('21f2000493'))

# Database
app = Flask(__name__)
CORS(app)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'databasea.sqlite')
#app.config["CELERY_BROKER_URL"] = "redis://localhost:6379/1"
#app.config["CELERY_RESULT_BACKEND"] = "redis://localhost:6379/2"


# celery
celery = Celery(app.name, broker_url="redis://localhost:6379/1", result_backend="redis://localhost:6379/2")
celery.conf.update(app.config)


# cache
cache = Cache(app, config={'CACHE_TYPE': CACHE_TYPE, 'CACHE_REDIS_HOST': CACHE_REDIS_HOST, 'CACHE_REDIS_PORT': CACHE_REDIS_PORT})


db = SQLAlchemy()
db.init_app(app)
app.app_context().push()


# API
api = Api(app)


###################################################################################################################
# Database Models


class Blog(db.Model):
  blog_id = db.Column(db.Integer, primary_key = True, nullable = False, autoincrement = True)
  blog_title = db.Column(db.String, nullable = False)
  blog_caption = db.Column(db.String, nullable = False)
  blog_content = db.Column(db.String, nullable = False)
  blog_image_url = db.Column(db.String, nullable = True)
  blog_timestamp = db.Column(db.String, nullable = False)
  blog_likes = db.Column(db.Integer)
  blog_author_id = db.Column(db.Integer, nullable = False)


class User(db.Model):
  user_id = db.Column(db.Integer, primary_key = True, autoincrement = True, nullable = False)
  user_name = db.Column(db.String, unique = True, nullable = False)
  user_followers = db.Column(db.Integer)
  user_desc = db.Column(db.String)
  user_posts = db.Column(db.Integer)
  user_likes = db.Column(db.Integer)


class Followers(db.Model):
  user_id = db.Column(db.Integer,primary_key = True, autoincrement = True, nullable = False)
  user = db.Column(db.Integer, nullable =False)
  follower_id = db.Column(db.Integer)


class Login(db.Model):
  login_id = db.Column(db.Integer, autoincrement = True, primary_key = True, nullable = False)
  username = db.Column(db.String, nullable = False)
  password = db.Column(db.String, nullable = False)
  user_id = db.Column(db.Integer, nullable = False)


class Comments(db.Model):
  comm_id = db.Column(db.Integer, primary_key = True, autoincrement = True, nullable = False)
  comment = db.Column(db.String, nullable = False)
  user_id = db.Column(db.Integer, nullable = False)
  blog_id = db.Column(db.Integer, nullable = False)
  

#####################################################################################################################
# Celery Tasks


celery.conf.beat_schedule = {
    'every-day': {
        'task': 'flask_code.engagement_report',
        'schedule': crontab(hour=13, minute=19),
    },
}
celery.conf.timezone = 'UTC'

@celery.task()
def engagement_report():
    
    data_user = len(db.session.query(User).all())
    data_blog = len(db.session.query(Blog).all())
    data_comments = len(db.session.query(Comments).all())
    res = []
    res.append(["data_user", "data_blog", "data_comments"])
    res.append([data_user, data_blog, data_comments])

    df = pd.DataFrame(res)
    df.to_csv('engagementreport.csv', index=False)
    
    return {}

  


@celery.task()
def export_data_to_csv(id):

    data = db.session.query(Blog).filter(Blog.blog_author_id == int(id)).all()
    res = []
    for i in data:
      res.append([i.blog_id, i.blog_title, i.blog_caption, i.blog_image_url, i.blog_likes, i.blog_content, i.blog_author_id])
    
    df = pd.DataFrame(res)
    df.to_csv('exportreport.csv', index=False)

    return {}





#######################################################################################################################################




# sending email
def send_email(to_address, subject, message, attachment_file):

  msg = MIMEMultipart()
  msg['From'] = SENDER_ADDRESS
  msg['To'] = to_address
  msg["Subject"] = subject

  msg.attach(MIMEText(message, 'html'))

  if attachment_file is not None:
    part = MIMEBase('application', "octet-stream")
    part.set_payload(open(attachment_file, "rb").read())
    encoders.encode_base64(part)
    part.add_header('Content-Disposition', f'attachment; filename= {attachment_file}')
    msg.attach(part)

  s = smtplib.SMTP(host = SMPTP_SERVER_HOST, port = SMPTP_SERVER_PORT)
  s.login(SENDER_ADDRESS, SENDER_PASSWORD)
  s.send_message(msg)
  s.quit()

  return {}




########################################################################################################################################
# Cache Functions

@cache.cached(timeout=7, key_prefix='get_all_blog_data')
def get_all_blog_data():
    data = db.session.query(Blog).all()
    return data


@cache.memoize(timeout=15)
def get_my_blog_data(id):
    data = db.session.query(Blog).filter(Blog.blog_id == int(id)).first()
    return data



########################################################################################################################################


# API


# Api used at Login Page
class LoginApi(Resource):
  
  def get(Resource, username):
    data = db.session.query(Login).filter(Login.username == username).first()
    return{"password" : data.password, "user_id": data.user_id}
  
  def post(self):
    username = request.json['username']
    password = request.json['password']
    
    data = db.session.query(User).all()
    
    newuser = Login(username = username, password= password, user_id = int(data[-1].user_id)+1)
    db.session.add(newuser)
    db.session.commit()
    return 201
    
api.add_resource(LoginApi, "/login/<username>", "/login/new")



# Api to get user by user_id and to create new user
class Userdata(Resource):
  
  def get(self, id):
    data = db.session.query(User).filter(User.user_id == int(id)).first()
    return{"user_name" : data.user_name}
  
  def post(self):
    user_name = request.json['user_name']
    data = db.session.query(User).all()
    
    newuser = User(user_id = int(data[-1].user_id)+1, user_name = user_name, user_desc = "New User", user_followers = 0, user_likes = 0, user_posts = 0)
    db.session.add(newuser)
    db.session.commit()
    return 201
  
api.add_resource(Userdata, "/user/<id>", "/user/new")



# Api to get blog by blog_id
class Page(Resource):

  def get(self,id):
    start = perf_counter()
    
    data = get_my_blog_data(id)             # cached data

    stop = perf_counter()
    print(stop-start)

    return{"blog_id": data.blog_id, "blog_title":data.blog_title, "blog_caption": data.blog_caption, "blog_content": data.blog_content, "blog_timestamp": data.blog_timestamp, "blog_image_url": data.blog_image_url, "blog_author_id": data.blog_author_id, "blog_likes": data.blog_likes}

api.add_resource(Page, "/page/<id>")



# Api to get data about the user by name
class Profile(Resource):

  def get(self, name):

    data = db.session.query(User).filter(User.user_name == name).first()
    count_posts = len(db.session.query(Blog).filter(Blog.blog_author_id == data.user_id).all())
    count_followers = len(db.session.query(Followers).filter(Followers.user == data.user_id).all())
    count_likes_data = db.session.query(Blog).filter(Blog.blog_author_id == data.user_id).all()
    count_likes = 0
    for i in count_likes_data:
      count_likes = count_likes + i.blog_likes

    return{"user_name": data.user_name, "user_followers": count_followers, "user_posts": count_posts, "user_likes": count_likes, "user_desc":data.user_desc, "user_id": data.user_id}
  
api.add_resource(Profile, "/profiledata/<name>")



# Api to get blog data for feed page and add new blog
class Blogdata(Resource):

  def get(self, id):

    start = perf_counter()
    followers_data = db.session.query(Followers).filter(Followers.user == id).all()
    data = get_all_blog_data()           # cached data

    f = []
    for j in followers_data:
      f.append(int(j.follower_id))

    res_data = []
    for i in data:
      if(i.blog_author_id in f):

        res_data.append([i.blog_id, i.blog_title, i.blog_content, i.blog_caption, i.blog_image_url, i.blog_timestamp, i.blog_likes, i.blog_author_id])

    stop = perf_counter()
    print(stop-start)

    return(res_data)
 

  def post(self):
    blog_title = request.json['title']
    blog_caption = request.json['caption']
    blog_image_url = request.json['image_url']
    blog_content = request.json['content']
    blog_author_id = request.json["author"]

    newblog = Blog(blog_title = blog_title, blog_caption= blog_caption, blog_image_url = blog_image_url, blog_content= blog_content, blog_timestamp = "18-04-2023",blog_likes = 0, blog_author_id = int(blog_author_id))
    db.session.add(newblog)
    db.session.commit()
    return 201

api.add_resource(Blogdata,"/blogdata/<id>", "/blogdata/add") 



# Api to get blogs written by logged in user
class Mydata(Resource):
  def get(self, id):
    start = perf_counter()
    data = get_all_blog_data()
    res_data = []
    for i in data:
      if(i.blog_author_id == int(id)):

        res_data.append([i.blog_id, i.blog_title, i.blog_content, i.blog_caption, i.blog_image_url, i.blog_timestamp, i.blog_likes, i.blog_author_id])
    
    stop = perf_counter()
    print(stop-start)

    return(res_data)
    
api.add_resource(Mydata, "/mydata/<id>")



# Api to add like to a blog by blog_id
class UpdateLikes(Resource):
  def put(self, id):
    data = db.session.query(Blog).filter(Blog.blog_id == id).first()
    data.blog_likes += 1
    db.session.commit()
    return {}

api.add_resource(UpdateLikes, "/updatelikes/<id>")



# Api to add follower to a user by user_id
class Followerinput(Resource):
  def post(self):
    user = request.json['user']
    name = request.json['name']

    data = db.session.query(User).filter(User.user_name == name).first()

    newfollo = Followers(user = int(user), follower_id = int(data.user_id))
    db.session.add(newfollo)
    db.session.commit()
    return 201

api.add_resource(Followerinput, "/followerapi")



# Api to update and delete blog by blog_id
class Deleteblog(Resource):
  def delete(self, id):
    data = db.session.query(Blog).filter(Blog.blog_id == int(id)).first()
    db.session.delete(data)
    db.session.commit()

    return {}
  

  def put(self, id):
    data = db.session.query(Blog).filter(Blog.blog_id == int(id)).first()

    blog_title = request.json['title']
    blog_caption = request.json['caption']
    blog_image_url = request.json['image_url']

    data.blog_title = blog_title
    data.blog_caption = blog_caption
    data.blog_image_url = blog_image_url
    db.session.commit()
    
    return{}

api.add_resource(Deleteblog, "/deleteblog/<id>")



# Api to export blog -- to be deleted
class Exportreport(Resource):
  def get(self, id):
    # Retrieve the data from the database
    start = perf_counter()
    data = db.session.query(Blog).all()
    res = []
    for i in data:
      res.append([i.blog_id, i.blog_title, i.blog_caption, i.blog_image_url, i.blog_likes, i.blog_content, i.blog_author_id])
    
    df = pd.DataFrame(res)
    df.to_csv('exportreport.csv', index=False)

    stop = perf_counter()
    print(stop-start)

    return {}
  
api.add_resource(Exportreport, "/exportreport/<id>")



# Api for the follower data page
class Followerpagedata(Resource):
  def get(self, id):
    
    data_follow = db.session.query(Followers).filter(Followers.user == id).all()
    already_follow = []
    for i in data_follow:
      already_follow.append(int(i.follower_id))

    data_allusers = db.session.query(User).all()
    not_follow = []
    for i in data_allusers:
      if(i.user_id not in already_follow):
        not_follow.append(int(i.user_id))
    list_af = []
    list_cf = []

    for i in data_allusers:
      if(i.user_id in already_follow):
        list_af.append([i.user_id, i.user_name, i.user_desc, True])
      if(i.user_id in not_follow and i.user_id != int(id)):
        list_cf.append([i.user_id, i.user_name, i.user_desc, False])

    res = {
      "already_follow": list_af,
      "can_follow": list_cf
    }

    return res
  
  
  def delete(self, id, follower_id):
    data = db.session.query(Followers).filter(Followers.user == int(id), Followers.follower_id == int(follower_id)).first()
    db.session.delete(data)
    db.session.commit()
    return {}
  
  
  def post(self):
    user = request.json['user']
    follower_id = request.json['follower_id']

    newfollo = Followers(user = int(user), follower_id = int(follower_id))
    db.session.add(newfollo)
    db.session.commit()
    return 201

api.add_resource(Followerpagedata, "/followerpagedata/<id>", "/followerpagedata/<id>/<follower_id>", '/followerpagedata')



# Api to see or add a comment to a blog
class Commentdata(Resource):

  def get(self, blog_id):

    data_comm = db.session.query(Comments).filter(Comments.blog_id == int(blog_id)).all()
    data_user = db.session.query(User).all()

    res = []
    for i in data_comm:
      for j in data_user:
        if(i.user_id == j.user_id):
          res.append([i.comm_id, i.comment, j.user_name, i.blog_id, i.user_id])
          

    return res
  
  def post(self):
    user_name = request.json['author']
    blog_id = request.json['blog_id']
    comment = request.json['comment']

    data = db.session.query(User).filter(User.user_name == user_name).first()


    newcomm = Comments(user_id = int(data.user_id), blog_id = int(blog_id), comment = comment)
    db.session.add(newcomm)
    db.session.commit()

    return 201

api.add_resource(Commentdata, "/commentdata/<blog_id>", "/commentdata")



# Api to send celery task
class export_data_as_csv(Resource):
  def get(self, id):
    export_data_to_csv.delay(id)
    return {}



api.add_resource(export_data_as_csv, "/exportdata/<id>")



class email_the_data(Resource):

  def get(self):
    receiver = "example@mail.com"
    subject = "Blog"
    attachment_file = "exportreport.csv"
    message = render_template('email_temp.html')

    send_email(receiver, subject, message=message, attachment_file=attachment_file)
    return {}

api.add_resource(email_the_data, "/email_the_data")



class webhook(Resource):

  def post(self):

    title = request.json['title']
    bot_mes = "Hii, I have posted a new blog. Please check it out. The title is " + title
    url = 'https://chat.googleapis.com/v1/spaces/AAAAY9ac3Wg/messages?key=AIzaSyDdI0hCZtE6vySjMm-WEfRq3CPzqKqqsHI&token=pTpNjVl8Xj4DIm-eBtM4jdnDo94kx9fzma52OGIANxc%3D'
    bot_message = {
        'text': bot_mes}
    message_headers = {'Content-Type': 'application/json; charset=UTF-8'}
    http_obj = Http()
    response = http_obj.request(
        uri=url,
        method='POST',
        headers=message_headers,
        body=dumps(bot_message),
    )
    print(response)
    
api.add_resource(webhook, "/webhook")





if __name__ == '__main__':
  app.run(debug = True)
