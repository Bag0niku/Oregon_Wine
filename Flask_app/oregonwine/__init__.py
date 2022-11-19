from flask import Flask 
from sqlalchemy import create_engine
from oregonwine.config import *

## start the app
app = Flask(__name__)
app.config['SECRET_KEY'] = SECRET_KEY
app.config['SQLALCHEMY_DATABASE_URI'] =  db_type + db_user + db_pass + db_project + db_aws

## prepare the database
db_address = db_type + db_user + db_pass + db_project + db_aws
engine = create_engine(db_address)


from oregonwine import routes 

