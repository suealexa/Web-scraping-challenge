from flask import Flask, render_template, redirect

# Connect to scrape python file
import scrape_mars

# Get Mongo library
import pymongo

# Create an instance of Flask
app = Flask(__name__)

# Setup mongo connection
conn = "mongodb://localhost:27017"
client = pymongo.MongoClient(conn)

# Route to render index.html template 
@app.route("/")
def home():

    
    # Return template and data
    return render_template("index.html", )


# Route that will trigger the scrape function
@app.route("")
def ():

   # Run the scrape function
    mars_data = scrape_mars.scrape_info()

       

    # Redirect back to home page
    return redirect("/")


if __name__ == "__main__":
    app.run(debug=True)

