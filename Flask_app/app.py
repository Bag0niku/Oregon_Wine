from flask import Flask, jsonify
from sqlalchemy import create_engine
from config import *

## start the app
app = Flask(__name__)

## prepare the database
db_address = db_type + db_user + db_pass + db_project + db_aws
engine = create_engine(db_address)
conn = engine.connect()


wine_review_columns = ['winery','vintage','designation',
                       'variety','score','category','title','ava','region',
                       'province','country','release_price','review_source','brand_id', 'review_id']

vineyards_columns = [ 'place_id','name','business_status','formatted_phone_number',
                      'formatted_address','gmaps_url','website','rating','total_ratings',
                      'street_address','city','province','zipcode','country','brand_id',
                      'center_lat','center_lon','northeast_lat','northeast_lon','southwest_lat','southwest_lon']                       

brand_columns = ['brand_id', 'brand_name']                      
@app.route("/")
def welcome():
    data = [x for x in conn.execute("SELECT * FROM wine_reviews limit 10;")]
    reviews = list()
    for row in data:
        wine = dict()
        for i, col in enumerate(row):
            wine[wine_review_columns[i]] = col
        
        reviews.append(wine)

    return jsonify(reviews)












if __name__ == "__main__":
    app.run(debug=True)