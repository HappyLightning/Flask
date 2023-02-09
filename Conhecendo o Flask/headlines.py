import feedparser  # Utiliza RSS.
from flask import Flask
from flask import render_template
from flask import request


app = Flask(__name__)
RSS_FEEDS = {'nasa': 'https://www.nasa.gov/rss/dyn/Gravity-Assist.rss',
             'fox': 'http://feeds.foxnews.com/foxnews/latest',
             'cnn': 'http://rss.cnn.com/rss/edition.rss',
             }


@app.route('/', methods=['GET', 'POST'])
def get_news():
    query = request.form.get('publication')
    if not query or query.lower() not in RSS_FEEDS:
        publication = 'nasa'
    else:
        publication = query.lower()
    feed = feedparser.parse(RSS_FEEDS[publication])
    return render_template('home.html', articles=feed['entries'])


if __name__ == '__main__':
    app.run(port=5000, debug=True)  # Com debug ativado, queremos ver traceback.
