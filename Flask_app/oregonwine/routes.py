from flask import render_template, url_for, flash, redirect, jsonify, request
from oregonwine import app, engine
from oregonwine.forms import WineFilter
import pandas as pd


vineyards_columns = [ 'place_id','name','business_status','formatted_phone_number',
                      'formatted_address','gmaps_url','website','rating','total_ratings',
                      'street_address','city','province','zipcode','country','brand_id',
                      'center_lat','center_lon','northeast_lat','northeast_lon','southwest_lat','southwest_lon']                       

brand_columns = ['brand_id', 'brand_name']                      






@app.route("/", methods=['GET','POST'])
@app.route("/home", methods=['GET','POST'])
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

    df = pd.DataFrame(reviews)


    form.vintage.choices = list(df['vintage'].dropna().unique())
    form.vintage.choices.sort(reverse=True)
    form.category.choices = list(df['category'].dropna().unique()) # list(set([row['category'] for row in reviews]))   
    form.category.choices.sort()
    form.min_score.choices = list(list(df['score'].dropna().unique()))
    form.min_score.choices.sort()
    form.max_score.choices = list(list(df['score'].dropna().unique()))
    form.max_score.choices.sort(reverse=True)
    form.region.choices = list(list(df['region'].dropna().unique())) # list(set([row['region'] for row in reviews]))   
    form.region.choices.sort()
    form.min_price.choices = list(list(df['release_price'].dropna().unique()))
    form.min_price.choices.sort()
    form.variety.choices = list(list(df['variety'].dropna().unique())) # list(set([row['variety'] for row in reviews]))   
    form.variety.choices.sort()
    form.max_price.choices = list(df['release_price'].dropna().unique())
    form.max_price.choices.sort(reverse=True)

    if request.method == 'POST':
        return f"""<h1>Form info:</h1>
                  <p>Min Price: {form.min_price.data}</p>
                  <p>Max Price: {form.max_price.data}</p>
                  <p>Min Score: {form.min_score.data}</p>
                  <p>Max Score: {form.max_score.data}</p>
                  <p>Category: {form.category.data}</p>
                  <p>Variety: {form.variety.data}</p>
                  <p>Vintage: {form.vintage.data}</p>
        
               """
    else:
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



    
