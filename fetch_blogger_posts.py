import requests
import os

# Aapka Blogger Blog ID aur API KEY
BLOG_ID = "7514934287514709504"
API_KEY = "AIzaSyCgeecqrz43BWNJ9SpTpPqgLnCyG89tiq4"

def get_posts():
    url = f"https://www.googleapis.com/blogger/v3/blogs/{7514934287514709504}/posts?key={AIzaSyCgeecqrz43BWNJ9SpTpPqgLnCyG89tiq4}"
    response = requests.get(url)
    if response.status_code != 200:
        print("Failed to fetch posts:", response.text)
        return []
    posts = response.json().get("items", [])
    return posts

def generate_html(posts):
    html = """<!DOCTYPE html>
<html>
<head>
  <title>All Blogger Posts</title>
</head>
<body>
  <h1>All Blogger Posts</h1>
  <ul>
"""
    for post in posts:
        html += f'    <li><a href="{post["url"]}" target="_blank">{post["title"]}</a></li>\n'
    html += """  </ul>
</body>
</html>
"""
    return html

if __name__ == "__main__":
    posts = get_posts()
    html = generate_html(posts)
    # Make sure 'posts' folder exists
    os.makedirs("posts", exist_ok=True)
    with open("posts/index.html", "w", encoding="utf-8") as f:
        f.write(html)
