# Oregon Wine


## Overview
Wine is passion in a glass, just as food is passion on a plate. Every wine has a story that makes it unique. The story and passion starts with choices made by the growers from the major decisions like when to trim leaves or when to start harvesting the fruit, down to the smallest decisions like if you will sing to your grapes (yes some still do this). These decisions affect the outcome of wine just as much as the quality of a vineyards soil, amount of rain, and storms that pass overhead. The grower and the winemaker are often one in the same person, however there are also many winemakers that are not growers. 

The winemaker’s passion shows in the choices he makes during fermentation and storage of the wine. Varieties of grape to use, how long each stage of the fermentation will last, what kind of barrels will be used for storing the wine, the quality and timing of maintenience performed on the barrels during storage, even a decision as simple as when to bottle matters.

Now we come to your point in the wine's story. How did the wine bottle get from the winemaker to you and how long did it take? The time and environment that bottle remains in will affect changes in the flavors and quality of the wine. Did you get the wine from the shelf in a store or did you visit a vineyard or tasting room? the path you took to get to that bottle will matter to your part in it's story just as much how it got to you because if you are paying enough attention even your mood and environment while you are drinking the wine will cause each bottle to taste different. 

There are two important pieces of information about the wine industry most people do not know. The First is: the wine you can buy in the grocery store is but a tiny fraction of the wine available and finding it is only as adventurous as you make it. For every winery you see on those shelves there are more than a thousand others making wine worthy of their passion. You could choose to only have the wine from the shelves at the grocery store, or you can look for and visit those with a passion for wine not on the shelves. 

The Second is: wine on those shelves are meant to attract you to their winery’s Tasting Room where they keep the higher quality wine they reserve for their wine club members, and deliberately keep off the grocery store shelves. The quality of wine on those shelves is not the best you can find, nor is it the worst. The quality is meant to be good enough to grab attention and pique your interest to investigate more of their wines, but also a low enough quality they do not want to keep it in their own inventory. You read that correctly, wineries tend to keep the better wines in their inventory and make them available exclusively to those that visit the tasting rooms and their wine club members.

This project was created with the sole purpose in mind of helping those continuing their wine adventure, how you chose to be a part of the next bottle’s story is up to you. 


### Contributors:
- Shaobobei
- MichaylaGilchrist
- DarrinM37

### Data
- Wine Reviews from:
    - Wine Enthusiest
    - Wine Spectator
- Winery and Vineyard loactions pulled from the Google Places API
- Oregon Wine industry information from 

## Instructions
Notes to know before you get started using the web app <a href=http://www.oregonvineyards.wine/>http://www.oregonvineyards.wine/ </a> : 
- By no means does this dataset include all wine, or all wine rated from the review sources we gathered from, however it has alot of wine and the data will expand in the future to include future published reviews; a process not yet automated. The same goes for the vineyards and wineries in our data. There are several I know of and have been to but are not within the dataset. Their data will be added in the future.
- Currently the only filter parameter upon intial load is wine made in Oregon because wine is made all over the world and it was inevitable for some of it to wind up in our data retrieval.
- The checkbox next to the title of the search filter parameter must be checked to be applied to the search results. 
- The "Map Official Tasting Locations" button will load a map of offical tasting locations based on the search results. If you select a checkbox for any wines, only those will be mapped.
- The oregon wine industry "about" web page is hosted here on github and also available on the web app.

## How the project went:

### Goals for the Final Product:
- Estimated completion time 4 weeks.
- Wine reviews page that can be filtered based on wines.
- Vineyard/Tasting Room Locator Map based on filtered results
- About Us Page
- Wine FAQ and FYI Page
- Data will be hosted on AWS cloud service
- Once finished website will be hosted on AWS S3 with the domain:  <a href=http://www.oregonvineyards.wine/>http://www.oregonvineyards.wine/</a>

### First Tasks
To get off start and form a clearer picture of our goal we need data. A list of Oregon vineyards was found during a brainstorming session on the <a href=https://oregontails.org/things-to-do/eat-drink/oregon-wineries-list/>OregonTails.gov</a> website.  
- MichaylaGilchrist
    - Gather Wine FAQ and FYI
- Shaobobei and DarrinM37
    - Gather Wine Reviews
- Bag0niku (myself)
    - Gather Vineyard and Winery 
    - Clean the data that has been gathered by everyone.

### Second Tasks
Gathering data has been troublesome, however some data has been gathered. Enough to start building mock-ups of the different systems we will be using.
- Bag0niku (me)
    - Build SQL database and host on AWS with current data.
    - Build the Flask App to connect the sql database on AWS
- DarrinM37    
    - Start building the webpage to visualize the vineyard locations on a map. 
- MichaylaGilchrist
    - Decide on the specific Oregon Wine Industry content that will be on the Wine FYI/FAQ 
- Shaobobei
    - Continue gathering wine information and reviews


### Third Tasks
Progress has been frustrating and slow. Next tasks are to complete the remaining pieces of previously assigned tasks and start the following:
- MichaylaGilchrist
    - Finish Oregon wine industry analysis
    - work with Shaobobei to visualize the oregon wine industry information on a webpage
- Shaobobei
    - Create an About Us webpage
    - Work with MichaylaGilchrist
- Darrin
    - finish the maping visualization of the wineries and vineyards
- Bag0niku
    - Build Webpage to view and filter the wine list data in a table.  
    
### Fourth Tasks
- Connect the webpages together into one working unit
- Bag0niku
    - Live hosting of the web app on AWS at http://www.oregonvineyards.wine


## Future Features
This project will continue to be built out and gain more features as time progresses. It is meant to help people with their wine adventures.

- Next Basic Features:
    - map directions to tasting rooms.
    - user login to keep preferences and or history.
    - track wines tried/liked/disliked.
    - track tasting rooms visited/liked/disliked.
    - user notes/reviews of tasting rooms and wines.
        - system logistics: "notes" is an unpublished review and may remain that way for as long as the user wishes.

- More Advanced Features sometime later:
    - Ability to build itinerary plan for visiting multiple vineyards, and possibly share.
    - map directions to vineyards in the area without a filtered search.
    - which wineries you are a wine club member of.