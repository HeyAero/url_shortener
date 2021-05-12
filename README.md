# URL Shortener
By Elwin & Aaron

***

## 

Welcome!

Our web app allows users to submit an existing url and receive a shortened version of it.  After submission, users can click directly on the generated hyperlink, or copy the shortened url to their clipboard and manually paste into their browser.  Read on for further instructions.

***

## User installations and instructions

- Fork and clone this repo to your local machine
- `cd` into the repo and run the following commands:
    - Launch virtual environment: `pipenv shell`
    - Install required dependencies: `pipenv install -r "requirements.txt"` and `pipenv install`
    - Initialise the database: `python inid_db.py`
    - Run dev environment: `pipenv run dev`
- Visit `http://localhost:5000` to view the app in development mode!
- Once using the app, enter a url name in the form field (make sure you include `http://` at the beginning of your input)

### Things to try

- Submit an existing url
- Use the copy to clipboard button to manually copy and paste the shortened url into your browser
- Visit a path that doesn't exist (there should be a custom error message)
    - You can do this by submitting an invalid url and clicking the generated hyperlink, or by adding a non-existent path to the base url
        e.g. http://localhost/blah

***

## Task requirements:
- [x] Users should be able to enter a url into an input box on your website's front page
- [x] Your backend will then generate a shortened path at which a User can access their url
- [x] You must implement Python in some capacity in this application
- [x] Store this shortened path and it's longer counterpart in a database
- [x] No login should be required to create a shortened URL
- [x] If User tries to access your website with a path you have stored in your database, they should get rerouted to the URL it relates to
- [x] If User tries to access your website with a path you do not have stored in your database, they should get rerouted to the homepage where they can create a new short URL

***

## Changelog

As of first release, there have been no file changes.  To view all changes made since the beginning of the project, please refer to the commit history on github

## Exisiting bugs

As of writing, there do not appear to be any!

## Test suites

We have not added test suites yet, but this is a future possibility.

***

## Wins and challenges

### Wins

- We have a fully functional app
- We have added functionality whereby users can copy and paste the link directly to their browser
- Neat, minimalistic styling

### Challenges

- Initialising the database:
    - We achieved this by moving the init_db functionality to a separate file and running it independently of the main app

- Copy link functionality
    - We achieved this by carefully reading through online resources

- Overriding Bootstrap styling to center main content
    - We solved this issue by removing semantic elements from our HTML templates, as these come with default margins and padding when using Bootstrap.
    - We also used `margin: 0; padding: 0` where appropriate

***

## Future features

- More detailed styling
- A fully functional test suite with minimum 60% coverage 

***

### Contact us

Would you like to provide some feedback?  Or inform us of a bug?

Feel free to contact us by visiting the Github profiles of either of the collaborators (HeyAero and ecarlos09).
