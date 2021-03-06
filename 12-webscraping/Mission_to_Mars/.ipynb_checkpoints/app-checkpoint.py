{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "from flask import Flask, render_template, redirect\n",
    "from flask_pymongo import PyMongo\n",
    "import Mission_to_Mars\n",
    "\n",
    "app = Flask(__name__)\n",
    "\n",
    "# Use flask_pymongo to set up mongo connection\n",
    "app.config[\"MONGO_URI\"] = \"mongodb://localhost:27017/craigslist_app\"\n",
    "mongo = PyMongo(app)\n",
    "\n",
    "# Or set inline\n",
    "# mongo = PyMongo(app, uri=\"mongodb://localhost:27017/craigslist_app\")\n",
    "\n",
    "\n",
    "@app.route(\"/\")\n",
    "def index():\n",
    "    listings = mongo.db.listings.find_one()\n",
    "    return render_template(\"index.html\", listings=listings)\n",
    "\n",
    "\n",
    "@app.route(\"/scrape\")\n",
    "def scraper():\n",
    "    listings = mongo.db.listings\n",
    "    listings_data = scrape_craigslist.scrape()\n",
    "    listings.update({}, listings_data, upsert=True)\n",
    "    return redirect(\"/\", code=302)\n",
    "\n",
    "\n",
    "if __name__ == \"__main__\":\n",
    "    app.run(debug=True)"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "PythonData",
   "language": "python",
   "name": "pythondata"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.6.10"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}
