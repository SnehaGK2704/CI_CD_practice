from flask import Flask, render_template_string
import requests

app = Flask(__name__)

BASE_URL = "https://jsonplaceholder.typicode.com"


@app.route('/', methods=['GET'])
def home():
    """Display home page with available routes"""
    html = """
    <!DOCTYPE html>
    <html>
    <head>
        <title>JSONPlaceholder API Routes</title>
        <style>
            body {
                font-family: Arial, sans-serif;
                max-width: 800px;
                margin: 50px auto;
                padding: 20px;
                background-color: #f5f5f5;
            }
            h1 {
                color: #333;
                border-bottom: 2px solid #007bff;
                padding-bottom: 10px;
            }
            .route {
                background: white;
                padding: 15px;
                margin: 10px 0;
                border-radius: 5px;
                box-shadow: 0 2px 5px rgba(0,0,0,0.1);
            }
            .route a {
                color: #007bff;
                text-decoration: none;
                font-weight: bold;
            }
            .route a:hover {
                text-decoration: underline;
            }
            .description {
                color: #666;
                margin-top: 5px;
            }
        </style>
    </head>
    <body>
        <h1>Available Routes</h1>
        
        <div class="route">
            <a href="/posts/">/posts/</a>
            <p class="description">This link fetches all the posts from JSONPlaceholder</p>
        </div>
        
        <div class="route">
            <a href="/comments/">/comments/</a>
            <p class="description">This link fetches all the comments from JSONPlaceholder</p>
        </div>
        
        <div class="route">
            <a href="/albums/">/albums/</a>
            <p class="description">This link fetches all the albums from JSONPlaceholder</p>
        </div>
    </body>
    </html>
    """
    return render_template_string(html)


@app.route('/posts/', methods=['GET'])
def get_posts():
    """Fetch all posts from JSONPlaceholder"""
    try:
        response = requests.get(f"{BASE_URL}/posts")
        response.raise_for_status()
        return {"status": "success", "data": response.json()}
    except requests.exceptions.RequestException as e:
        return {"status": "error", "message": str(e)}, 500


@app.route('/comments/', methods=['GET'])
def get_comments():
    """Fetch all comments from JSONPlaceholder"""
    try:
        response = requests.get(f"{BASE_URL}/comments")
        response.raise_for_status()
        return {"status": "success", "data": response.json()}
    except requests.exceptions.RequestException as e:
        return {"status": "error", "message": str(e)}, 500


@app.route('/albums/', methods=['GET'])
def get_albums():
    """Fetch all albums from JSONPlaceholder"""
    try:
        response = requests.get(f"{BASE_URL}/albums")
        response.raise_for_status()
        return {"status": "success", "data": response.json()}
    except requests.exceptions.RequestException as e:
        return {"status": "error", "message": str(e)}, 500


if __name__ == '__main__':
    app.run(debug=True)
