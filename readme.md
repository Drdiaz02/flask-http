HTTP with Flask
===============

![HTTP Logo](https://upload.wikimedia.org/wikipedia/commons/thumb/5/5b/HTTP_logo.svg/330px-HTTP_logo.svg.png)

Learning Objectives
-------------------

After completing this assignment, students will be able to:

- Describe the purpose and function of HTTP
- Use flask to return static and dynamic pages in response to `GET` requests
- Render images in HTML pages

Tasks
-----

Clone this repository in order to access the starter code for a simple `flask` application. Add the following enhancements:

1. Modify the root route to show different content using the provided HTML `template`. Simply replace `{content}` within the template to include the HTML for your page.
2. Modify the `template` to include an appropriate title.
3. Create an `add` route that requires two `int` value within its path that will be added. For example, a request to `/add/2/3` should return a page with the content `2 + 3 = 5` inside the HTML `template`.
4. Create a `reverse` route displays the reverse of the `q` `GET` parameter. For example, a request to `/reverse?q=abcd` should return a page with the content `abcd reversed is dcba` inside the HTML `template`.
5. Create a route called `sunset.jpg` that returns `sunset.jpg`. You should should use the `send_file` function provided by Flask.
6. Modify the root page to include the image `sunset.jpg`
7. Add a route to server `mars.png`
8. Update the application to use this as the favicon for all pages.

Usage
-----

In order to run the handout code, you will need Python 3 and Flask installed. Flask includes [detailed installation instructions](https://flask.palletsprojects.com/en/stable/installation/), but it is available on PyPI and should be installable via pip like most other packages.

Once flask is installed, you should be able to run the handout code as:

```sh
python app.py
```

Image Credits
-------------

- https://en.wikipedia.org/wiki/Sunset#/media/File:MarsSunset.jpg
- https://en.wikipedia.org/wiki/File:Mars_-_August_30_2021_-_Flickr_-_Kevin_M._Gill.png
