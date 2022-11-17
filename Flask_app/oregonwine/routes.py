from flask import render_template, url_for, flash, redirect, jsonify, request
from oregonwine import app, engine
from oregonwine.forms import WineFilter
import pandas as pd


def sql_query(statement, table):
    if table == 'wine_reviews':
        columns = ['winery','vintage','variety','designation',
                       'score','category','title','ava','region',
                       'province','country','release_price','review_source','brand_id', 'review_id']
    elif table == 'vineyards':
        columns = [ 'place_id','name','business_status','formatted_phone_number','formatted_address','gmaps_url',
                    'website','rating','total_ratings', 'street_address','city','province','zipcode','country','brand_id',
                      'center_lat','center_lon','northeast_lat','northeast_lon','southwest_lat','southwest_lon']                       

    elif table == 'brand':    
        columns = ['brand_id', 'brand_name']                      

    conn = engine.connect()
    response = [x for x in conn.execute(statement)]
    conn.close()
    reviews = list()
    for row in response:
        wine = dict()
        for i, col in enumerate(row):
            wine[columns[i]] = col
        reviews.append(wine)
    return reviews



@app.route("/", methods=['GET','POST'])
@app.route("/home", methods=['GET','POST'])
def welcome():

    form = WineFilter()

    
    response = sql_query(statement="SELECT * FROM wine_reviews ;", table='wine_reviews')
    
    df = pd.DataFrame(response)

    form.winery_select.choices = list(df['winery'].dropna().unique())
    form.winery_select.choices.sort()
    form.vintage_select.choices = [int(x) for x in df['vintage'].dropna().unique()]
    form.vintage_select.choices.sort(reverse=True)
    form.category_select.choices = list(df['category'].dropna().unique()) # list(set([row['category'] for row in reviews]))   
    form.category_select.choices.sort()
    form.min_score_select.choices = [int(x) for x in df['score'].dropna().unique()]
    form.min_score_select.choices.sort()
    form.max_score_select.choices = [int(x) for x in df['score'].dropna().unique()]
    form.max_score_select.choices.sort(reverse=True)
    form.region_select.choices = [x for x in df['region'].dropna().unique()] # list(set([row['region'] for row in reviews]))   
    form.region_select.choices.sort()
    form.min_price_select.choices = [int(x) for x in df['release_price'].dropna().unique()]
    form.min_price_select.choices.sort()
    form.variety_select.choices = list(df['variety'].dropna().value_counts().index) # list(set([row['variety'] for row in reviews]))   
    form.variety_select.choices.sort()
    form.max_price_select.choices = [int(x) for x in df['release_price'].dropna().unique()]
    form.max_price_select.choices.sort(reverse=True)

    if request.method == 'POST':
        select = "SELECT * FROM wine_reviews WHERE (province = 'Oregon') "
        spam = [form.min_price_bool.data, form.max_price_bool.data, form.min_score_bool.data, form.max_score_bool.data, 
                form.category_bool.data, form.variety_bool.data, form.vintage_bool.data, form.region_bool.data ]


        if form.min_price_bool.data and form.max_price_bool.data:
            if form.min_price_select.data != form.max_price_select.data:
                # BETWEEN KEYWORD NOT WORKING "Error: No operator matches the given name and argument types "
                # select += f" AND (release_price BETWEEN {form.min_price_select.data} AND {form.max_price_select.data} ) "
                select += f" AND ((release_price >= {form.min_price_select.data}) AND (release_price <= {form.max_price_select.data} )) "
            else:
                select += f" AND (release_price = {form.max_price_select.data} ) "
        elif form.min_price_bool.data:
            select += f" AND (release_price >= {form.min_price_select.data})"
        elif form.max_price_bool.data:
            select += f" AND (release_price <= {form.min_price_select.data})"
        else:
            pass

        if form.min_score_bool.data and form.max_score_bool.data:
            if form.min_score_select.data != form.max_score_select.data:
                select += f" AND (score BETWEEN {form.min_score_select.data} AND {form.max_score_select.data} ) "
            else:
                select += f" AND (score = {form.min_price_select.data})"
        elif form.min_score_bool.data:
            select += f" AND (score >= {form.min_price_select.data})"
        elif form.max_score_bool.data:
            select += f" AND (score <= {form.min_price_select.data})"
        else:
            pass

        if form.category_bool.data:
            select += f" AND ( category = '{form.category_select.data}')"
        else:
            pass

        if form.variety_bool.data:
            select += f" AND (variety = '{form.variety_select.data}')"
        else:
            pass
        
        if form.vintage_bool.data:
            select += f" AND (vintage = {form.vintage_select.data})"
        else:
            pass
        
        if form.region_bool.data:
            select += f" AND (region = '{form.region_select.data}')"
        else:
            pass

        if form.winery_bool.data:
            select += f" AND (winery = '{form.winery_select.data}')"
        else:
            pass

        ## End of checking for filters to apply
        select += " ;"

        ## New SQL Query with the search filter applied.
        response = sql_query(statement=select, table='wine_reviews')



        return render_template('home.html', data=response, form=form, result_count=len(response))


    else:
        return render_template('home.html', data=response, form=form, result_count=len(response))


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

    df = pd.DataFrame(reviews)
    return jsonify(data= reviews) # df.to_json())


@app.route("/update")
def update():
    region = request.args['region'].get()
    category = request.args['category'].get()
    variety = request.args['variety'].get()
    vintage = request.args['vintage'].get()

    return str([region, category, variety, vintage] )



    
