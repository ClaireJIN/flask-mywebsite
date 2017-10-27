from app import db
from app.models import Role, User, Post
db.drop_all()
db.create_all()
Role.insert_roles()
User.generate_fake()
Post.generate_fake() 
