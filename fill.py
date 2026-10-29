
from bs4 import BeautifulSoup

# import requests




html = """<html>

<head><title>Book Store</title></head>

<body>

<h1>Welcome to My Book Store</h1>

<p class="description">Books for learners.</p>

<p class="price">Price: 5000 naira</p>

<a href="https://example.com/books">View books</a>

</body>

</html>"""




soup = BeautifulSoup(html, "html.parser")


print("Title:", soup.title.get_text(strip=True))

print("Heading:", soup.find("h1").get_text(strip=True))

print("Description:", soup.find("p", class_="description").get_text(strip=True))

print("Price:", soup.find("p", class_="price").get_text(strip=True))