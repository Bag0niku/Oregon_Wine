import pandas as pd
from flask import render_template, url_for, flash, redirect, jsonify, request
from oregonwine import app, engine
from oregonwine.forms import WineFilter
from oregonwine.build_map import *



def sql_query(statement, table, columns='*'):
    if columns == '*':
        if table == 'wine_reviews':
                columns = ['winery','vintage','variety','designation','score','category','title','ava','region',
                        'province','country','release_price','review_source','brand_id', 'review_id']
        elif table == 'vineyards':
                columns = [ 'place_id','name','business_status','formatted_phone_number','formatted_address', "",
                        'website','rating','total_ratings', 'street_address','city','province','zipcode','country', "location_name", 
                        'center_lat','center_lon','northeast_lat','northeast_lon','southwest_lat','southwest_lon''brand_id', 'gmaps_url']                       

        elif table == 'brand':    
                columns = ['brand_id', 'brand_name']                      
    else:
        pass

    conn = engine.connect()
    response = [x for x in conn.execute(statement)]
    conn.close()
    reviews = list()
    for row in response:
        wine = dict()
        for i, col in enumerate(row):
            wine[columns[i]] = col
        
        if table == 'wine_reviews':
            wine['checkbox_id'] = str(wine['review_id']) + "_" + str(wine['brand_id'])
        
        reviews.append(wine)
    return reviews


def convert_search_paramaters(form):
        select = "SELECT * FROM wine_reviews WHERE (province = 'Oregon') "

        if form.min_price_bool.data and form.max_price_bool.data:
            if form.min_price_select.data != form.max_price_select.data:
                # SQL KEYWORD BETWEEN NOT WORKING "Error: No operator matches the given name and argument types "
                # select += f" AND (release_price BETWEEN {form.min_price_select.data} AND {form.max_price_select.data} ) "
                select += f" AND ((release_price >= {form.min_price_select.data}) AND (release_price <= {form.max_price_select.data} )) "
            else:
                select += f" AND (release_price = {form.max_price_select.data} ) "
        elif form.min_price_bool.data:
            select += f" AND (release_price >= {form.min_price_select.data})"
        elif form.max_price_bool.data:
            select += f" AND (release_price <= {form.max_price_select.data})"
        else:
            pass

        if form.min_score_bool.data and form.max_score_bool.data:
            if form.min_score_select.data != form.max_score_select.data:
                # SQL KEYWORD BETWEEN STILL NOT WORKING "Error: No operator matches the given name and argument types "
                select += f" AND ((score >= {form.min_score_select.data}) AND (score <= {form.max_score_select.data} )) "
            else:
                select += f" AND (score = {form.min_score_select.data})"
        elif form.min_score_bool.data:
            select += f" AND (score >= {form.min_score_select.data})"
        elif form.max_score_bool.data:
            select += f" AND (score <= {form.max_score_select.data})"
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

        if form.sort_by_bool.data:
            select += f" ORDER BY {form.sort_by.data} "
        elif form.sort_desc_bool.data:
            select += f" ORDER BY {form.sort_by.data} DESC "

        ## End of checking for filters to apply
        select += " ;"

        return select



@app.route("/about")
def about():
    return redirect('https://bag0niku.github.io/Oregon_Wine/')



@app.route("/", methods=['GET','POST'])
@app.route("/wine", methods=['GET','POST'])
def wine_list():

    form = WineFilter()

    
    select_wine = "SELECT * FROM wine_reviews WHERE province = 'Oregon' ;"
    
    response = sql_query(statement=select_wine, table='wine_reviews')
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

        select_wine = convert_search_paramaters(form=form)

        ## New SQL Query with the search filter applied.
        response = sql_query(statement=select_wine, table='wine_reviews')
        if len(response) == 0 :
            return render_template("no-results.html", form=form)
        review_brand = [x for x in pd.DataFrame(response)['checkbox_id']]
        brand_list = list(pd.DataFrame(response)['brand_id'].unique())
        brand_list = str(brand_list)[1:-1].replace(", ", ",")

        return render_template('wine.html', data=response, form=form, result_count=len(response), review_brand=review_brand, brand_list=brand_list)

    else:
        brand_list = list(pd.DataFrame(response)['brand_id'].unique())
        brand_list = str(brand_list)[1:-1].replace(", ", ",")
        review_brand = [x for x in pd.DataFrame(response)['checkbox_id']]

        return render_template('wine.html', data=response, form=form, result_count=len(response), review_brand=review_brand, brand_list=brand_list)


@app.route("/map/<filter>")
def show_map(filter=None):
        
    filter = filter.split(",")
    columns = ['name','formatted_phone_number','formatted_address', 'website',
               'center_lat','center_lon', 'brand_id', 'gmaps_url']


    select_vineyards = """Select name, formatted_phone_number, formatted_address, website,
                                 center_lat, center_lon, brand_id, gmaps_url
                          FROM vineyards
                          WHERE (province = 'OR') """

    if filter != None:

        brand = " AND ("
        for i, x in enumerate(filter):
            if i >0:
                brand += " OR "
            
            brand += f"(brand_id = {x})"
        
        select_vineyards += " " + brand + ')'
    else:
        pass

    select_vineyards += " ;"
    # response = sql_query(statement=select_vineyards, table='vineyards', columns=columns )
    df = pd.read_sql(select_vineyards, con=engine, columns=columns)
    map = make_map(df)
    markers = make_markers(df)
    markers.add_to(map)

    return map._repr_html_()




def veiw_map(brand_list):
    ## turn the brand_list into a SQL WHERE clasue to add to a the show map filter 

    return redirect(url_for('found', filter=filter))
