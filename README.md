# Oregon_Wine
Wine recommender for Oregon wines

## Overview
Using Oregon Wine as the theme, this project will be a team project combining attributes from projects completed in the last few months.

### Contributors:
- Shaobobei
- MichaylaGilchrist
- DarrinM37

## Data
Data Sources are still being determined, some webscraping will be involved.

## Goals for the Final Product:
- Landing page / Index Page   (still do not know what this will be, could be reviews page, the map...etc)
- About Us Page
- Wine FAQ and FYI Page
- Reviews Page that can be filtered, Reviews of wines or Vinyards... Still undecided. (resembles UFO project)
- Wine/vinyard recommender page based on a few inputs including: Red/White, Budget, sweet/Dry
- Map Page: Map of Oregon Vineyards Locations (Vacation Itinerary/weather/Earthquake projects)
    - can be filtered based on the recomender output or apply your own filtering.
- Data will be hosted on AWS cloud service
- Once finished website will be hosted on AWS S3 with the domain:  https://www.oregonvineyards.wine/

## First Tasks
To get off start and form a clearer picture of our goal we need data. A list of Oregon vineyards was found during a brainstorming session on the <a href=https://oregontails.org/things-to-do/eat-drink/oregon-wineries-list/>OregonTails.gov</a> website.  
- Wine FAQ and FYI will be gathered by MichaylaGilchrist
- Wine Reviews will be gathered by Shaobobei and DarrinM37
- Vineyard and Winery locations will be gathered by Bag0niku (myself)
    - Raw data from the google api maps search is saved in 2 csv files. The files will need cleaned before we can use them, only a small portion of each record looks usable to us at first glance.


## Second Tasks
Some data has been gathered. Enough to start building mock-ups of the different systems we will be using.
- Bag0niku (me)
    - Webpage to view and filter the data in a table  (The landing page for now)
- DarrinM37    
    - Webpage to visualize the vineyard locations on a map. (page 2, accessible only weh the maping feature is requested)
- MichaylaGilchrist
    - Decide on the specific content that will be on the Wine FYI/FAQ (eventually page 3, linked on the landing page)
- Shaobobei
    - Continue gathering wine information and reviews



## Third Tasks
- Connect the webpages together into one working unit
- Webpage to visaulize the FYI and FAQ information (page 3, linked on the landingindex page)
- Build the Flask App to connect the sql database on aws
- Create an About Us webpage

## Fourth Tasks
- Not yet visible

