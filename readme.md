HTTP with Flask
===============

Learning Objectives
-------------------

After completing this assignment, students will be able to:

- Describe the purpose and function of HTTP
- Use flask to return static and dynamic pages in response to `GET` requests
- Render images in HTML pages

Tasks
-----

Clone this repository in order to access the starter code for a simple `flask` application. Add the following enhancements:

1. Modify the root route to return a description of the app that uses the include HTML `template`. Simply replace `{content}` within the template to include your page.
2. Modify the `template` to include an appropriate title.
3. Add an `<li>` to the template body that acts as navigation between all pages.
4. Create an `add` route that requires to `int` value within it's path that will be added. For example, a request to `/add/2/3` should return a page with the content `2 + 3 = 5`.
5. Create a `reverse` route displays the reverse of the `q` `GET` parameter. For example, a request to `/reverse?q=abcd` should return a page with the content `abcd reversed in dcba`.
