from flask import Flask, render_template, redirect
import scrape_costa

# Create an instance of Flask
app = Flask(__name__)

# Route to render index.html template 
@app.route("/")
def home():

    
    # Return template and data
    return render_template("index.html", )


# Route that will trigger the scrape function
@app.route("")
def ():

    # Run the scrape function
    costa_data = scrape_costa.scrape_info()

       

    # Redirect back to home page
    return redirect("/")


if __name__ == "__main__":
    app.run(debug=True)

