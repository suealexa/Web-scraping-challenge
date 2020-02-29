from flask import Flask, render_template, redirect

# Get Mongo library
import pymongo

# Connect to scrape python file
import scrape_mars

# Create an instance of Flask
app = Flask(__name__)

# Setup mongo connection
conn = "mongodb://localhost:27017"
client = pymongo.MongoClient(conn)

# Route to render index.html template 
@app.route("/")
def home():
    # Find one record of data from the mongo database
    mars_info = mongo.db.mars_info.find_one()
   
    # Return template and data
    return render_template("index.html", mars=mars_info  )


# Route that will trigger the scrape function
@app.route("/scrape")
def scrape():

    mars = mongo.db.mars
    mars_info = scrape_mars.scrape()
    mars.update(
        {},
        mars_info,
        upsert=True
    )
    return redirect("http://localhost:5000/", code=302)



if __name__ == "__main__":
    app.run(debug=True)

