from flask import render_template, url_for, flash, redirect, jsonify, request
from oregonwine import app, engine
from oregonwine.forms import WineFilter


vineyards_columns = [ 'place_id','name','business_status','formatted_phone_number',
                      'formatted_address','gmaps_url','website','rating','total_ratings',
                      'street_address','city','province','zipcode','country','brand_id',
                      'center_lat','center_lon','northeast_lat','northeast_lon','southwest_lat','southwest_lon']                       

brand_columns = ['brand_id', 'brand_name']                      






@app.route("/")
@app.route("/home")
def welcome():

    form = WineFilter()

    wine_review_columns = ['winery','vintage','variety','designation',
                       'score','category','title','ava','region',
                       'province','country','release_price','review_source','brand_id', 'review_id']
    conn = engine.connect()
    response = [x for x in conn.execute("SELECT * FROM wine_reviews limit 15;")]
    conn.close()
    reviews = list()
    for row in response:
        wine = dict()
        for i, col in enumerate(row):
            wine[wine_review_columns[i]] = col
        reviews.append(wine)

    form.vintage.choices = list(set([row['vintage'] for row in reviews]))
    form.category.choices = list(set([row['category'] for row in reviews]))   
    form.min_score.choices = list(set([row['score'] for row in reviews]))
    form.max_score.choices = list(set([row['score'] for row in reviews]))
    form.region.choices = list(set([row['region'] for row in reviews]))   
    form.min_price.choices = list(set([row['release_price'] for row in reviews]))
    form.variety.choices = list(set([row['variety'] for row in reviews]))   
    form.max_score.choices = list(set([row['score'] for row in reviews]))


    return render_template('home.html', data=reviews, form=form)


@app.route("/api/v1.0/")
def api():

    wine_review_columns = ['winery','vintage','variety','designation',
                       'score','category','title','ava','region',
                       'province','country','release_price','review_source','brand_id', 'review_id']
    conn = engine.connect()
    response = [x for x in conn.execute("SELECT * FROM wine_reviews limit 15;")]
    conn.close()
    reviews = list()
    for row in response:
        wine = dict()
        for i, col in enumerate(row):
            wine[wine_review_columns[i]] = col
        reviews.append(wine)
    return jsonify(reviews=reviews)


@app.route("/update")
def update():
    region = request.args['region'].get()
    category = request.args['category'].get()
    variety = request.args['variety'].get()
    vintage = request.args['vintage'].get()

    return str([region, category, variety, vintage] )



    
