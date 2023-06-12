## Beautiful Soup - Web Scraping with Python

### Part 1: HTML Basics

Before we dive into web scraping, let's start by understanding the basics of HTML, the language used to structure web pages. HTML stands for HyperText Markup Language and is the standard markup language for creating web pages.

### HTML Document Hierarchy:

HTML documents are organized in a hierarchical structure. At the top level, we have the `<html>` tag, which contains two main sections: the `<head>` and the `<body>`. The `<head>` section typically contains meta-information about the document, such as the title and linking to external CSS or JavaScript files. The `<body>` section contains the visible content of the web page.

Inside the `<body>` section, we have various HTML tags that define the structure and content of the page. Some common tags include:

- `<h1>`, `<h2>`, `<h3>`, etc.: Heading tags used for titles and headings.
- `<p>`: Paragraph tag used for regular text content.
- `<a href="url">`: Anchor tag used for creating hyperlinks.
- `<ul>` and `<ol>`: Unordered and ordered lists.
- `<li>`: List item tag used within `<ul>` or `<ol>`.
- `<table>`: Table tag used for organizing tabular data.
- `<tr>`: Table row tag.
- `<td>`: Table data/cell tag.

These are just a few examples of HTML tags. There are many more tags available for various purposes, but these basics will be enough for our introduction.

### Part 2: Introduction to Beautiful Soup

`Beautiful Soup` is a Python library that allows us to extract data from HTML and XML files. It provides a convenient way to parse and navigate through the HTML document structure, making it easier to extract specific information.

To get started with `Beautiful Soup`, you'll need to install it first. You can install it using `pip` by running the following command in your terminal:

```python
pip install beautifulsoup4
```

Once installed, you can import `BeautifulSoup` in your Python script as follows:

```python
from bs4 import BeautifulSoup
```

### Part 3: Web Scraping with Beautiful Soup

Now that we have a basic understanding of HTML and have `Beautiful Soup` installed, let's see how we can use it to scrape tabular data from a web page.

1. Import the required libraries:

```python
from bs4 import BeautifulSoup
import requests
```

2. Fetch the HTML content of the web page:

```python
url = "URL_OF_THE_WEB_PAGE"
response = requests.get(url)
html_content = response.content
```

3. Create a `BeautifulSoup` object:

```python
soup = BeautifulSoup(html_content, 'html.parser')
```

4. Find the table element on the web page:

Inspect the web page using your browser's developer tools or view the page source to identify the table you want to scrape. Look for the HTML tags (`<table>`, `<tr>`, `<td>`, etc.) that define the table structure.

```python
table = soup.find('table')
```

5. Extract data from the table:

Once you have the table element, you can use `Beautiful Soup` methods to extract the data you need. For example, to extract all the rows (`<tr>`) from the table:

```python
rows = table.find_all('tr')
```

Sure! Continuing from where we left off:

6. Process the extracted data:

Loop through the rows and extract the relevant information from each row. For example, you can extract the data from each cell (`<td>`) within a row:

```python
for row in rows:
    cells = row.find_all('td')
    for cell in cells:
        # Process the cell data as needed
        print(cell.text)
```

You can access the text content of an element using the `.text` attribute.

7. Further processing and saving the data:

You can perform additional processing on the extracted data, such as cleaning, formatting, or saving it to a file or database for further analysis.

Here's a complete example that demonstrates how to scrape a table from a web page:

```python
from bs4 import BeautifulSoup
import requests

url = "URL_OF_THE_WEB_PAGE"
response = requests.get(url)
html_content = response.content

soup = BeautifulSoup(html_content, 'html.parser')
table = soup.find('table')

rows = table.find_all('tr')
for row in rows:
    cells = row.find_all('td')
    for cell in cells:
        # Process the cell data as needed
        print(cell.text)
```

Remember to replace `"URL_OF_THE_WEB_PAGE"` with the actual URL of the web page you want to scrape.

That's it! With the help of `Beautiful Soup`, you can navigate through the HTML structure and extract the desired information from web pages. Feel free to explore the library's documentation for more advanced features and techniques.

Keep in mind that when scraping websites, you should respect the website's terms of service and consider the legality and ethics of your scraping activities.

<sub>Source: CHAT GPT!! (with some changes for accuracy)</sub>
