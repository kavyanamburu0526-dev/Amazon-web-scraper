from flask import Flask, render_template, request
from scraper import scrape_amazon
app = Flask(__name__)
@app.route("/", methods=["GET", "POST"])
def home():
    product = None
    error = None
    if request.method == "POST":
        url = request.form.get("url")
        if not url:
            error = "Please enter an Amazon URL."

        elif "amazon." not in url:
            error = "Please enter a valid Amazon URL."
        else:
            try:
                product = scrape_amazon(url)
                if "error" in product:
                    error = product["error"]
                    product = None
            except Exception as e:
                error = f"Something went wrong: {e}"
    return render_template(
        "index.html",
        product=product,
        error=error
    )
if __name__ == "__main__":
    app.run(debug=True)