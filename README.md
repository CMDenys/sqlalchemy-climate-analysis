# sqlalchemy-challenge

Using Python and SQLAlchemy, a basic climate analysis and data exploration of precipitation history was conducted over a period of time in 2016.  

SQLAlchemy create_engine was used to connect to a sqlite database and SQLAlchemy automap_base() was used to reflect the tables into classes and save references to them.  

By using SQLAlchemy’s automap module, mapped classes could be automatically generated and relationships from the database schema could be reflected into a new model and mapped.  This allows data to be manipulated in ORM-style classes.  Finally, Python was linked to the sqlite database.  

Starting from the most recent date, the previous year of both precipitation and station data was retrieved by querying the 12 preceding months of data.  These results were loaded into a Pandas data frame, where summary statistics were generated, and data could be plotted out.

Once an analysis was completed on precipitation and stations, a Flask API was designed based on the queries that were developed in the station analysis.  These were:

- total number of stations in the dataset.
- most active stations.
- what station id had the highest number of observations

The following Routes were created:
- /api/v1.0/precipitation.  This route converts the query results to a dictionary using date as the key and prcp as the value.
- /api/v1.0/stations.  This route returns a JSON list of stations from the dataset.
- /api/v1.0/tobs.  This route queries the dates and temperature observations of the most active station for the last year of data and returns a JSON list of temperature observations (TOBS) for the previous year.
- /api/v1.0/<start> and /api/v1.0/<start>/<end>.  This route returns a JSON list of the minimum temperature, the average temperature, and the max temperature for a given start or start-end range.

