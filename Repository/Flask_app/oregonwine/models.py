from oregonwine import db

class Brand(db.Model):

   brand_id = db.Column(db.Integer, primary_key=True)
   brand_name = db.Column(db.String, nullable=False)
   tasting_room = db.relationship("Vineyards", backref='winery', lazy=True)
   wine = db.relationship("WineReviews", backref='winery', lazy=True)


class Vineyards(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    place_id = db.Column(db.String)
    business_name = db.Column(db.String, nullable=False)
    business_status = db.Column(db.String)
    formatted_phone_number = db.Column(db.String)
    formatted_address = db.Column(db.String)
    gmaps_url = db.Column(db.String)
    website = db.Column(db.String)
    rating = db.Column(db.Integer)
    total_ratings = db.Column(db.Integer)
    street_address = db.Column(db.String)
    city = db.Column(db.String)
    province = db.Column(db.String)
    zipcode = db.Column(db.String)
    country = db.Column(db.String)
    center_lat = db.Column(db.Float)
    center_lon = db.Column(db.Float)
    northeast_lat = db.Column(db.Float)
    northeast_lon = db.Column(db.Float)
    southwest_lat = db.Column(db.Float)
    southwest_lon = db.Column(db.Float)
    brand_id = db.Column(db.Integer, db.ForeignKey('brand.brand_id'))


class WineReviews(db.Model):
    review_id = db.Column(db.Integer, primary_key=True)
    winery = db.Column(db.String, nullable=False)
    vintage = db.Column(db.String, nullable=False)
    variety = db.Column(db.String, nullable=False)
    designation = db.Column(db.String)
    score = db.Column(db.Integer, nullable=False)
    category = db.Column(db.String, nullable=False)
    title = db.Column(db.String, nullable=False)
    ava = db.Column(db.String)
    region = db.Column(db.String, nullable=False)
    province = db.Column(db.String, nullable=False)
    country = db.Column(db.String, nullable=False)
    release_price = db.Column(db.String, nullable=False)
    review_source = db.Column(db.String, nullable=False)
    brand_id = db.Column(db.Integer, db.ForeignKey('brand.brand_id'))
    


