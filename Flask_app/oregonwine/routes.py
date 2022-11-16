from flask import render_template, url_for, flash, redirect
from oregonwine import app, engine


vineyards_columns = [ 'place_id','name','business_status','formatted_phone_number',
                      'formatted_address','gmaps_url','website','rating','total_ratings',
                      'street_address','city','province','zipcode','country','brand_id',
                      'center_lat','center_lon','northeast_lat','northeast_lon','southwest_lat','southwest_lon']                       

brand_columns = ['brand_id', 'brand_name']                      






@app.route("/")
@app.route("/home")
def welcome():
    wine_review_columns = ['winery','vintage','designation',
                       'variety','score','category','title','ava','region',
                       'province','country','release_price','review_source','brand_id', 'review_id']
    conn = engine.connect()
    data = [x for x in conn.execute("SELECT * FROM wine_reviews limit 15;")]
    conn.close()
    reviews = list()
    for row in data:
        wine = dict()
        for i, col in enumerate(row):
            wine[wine_review_columns[i]] = col
        
        reviews.append(wine)

    return render_template('home.html', data=reviews)


