<p><h1> i18n :fire:</h1></p>

<p><h2>Description :house:</h2></p>
In this project, I began to learn about i8n(Internationalization).
Internationalization (i18n) is the process of designing and developing software applications in a way that makes them adaptable to different languages, cultures, and regions without requiring changes to the core codebase. The term "i18n" is derived from the fact that there are 18 letters between the "i" and the "n" in the word "internationalization."
<br>
The goal of i18n is to create applications that can be easily localized for different locales (language and cultural settings) without modifying the application's functionality. This involves separating text, formatting, and other locale-specific content from the application's source code.

## Learning Objectives:

<br>
- Learn how to parametrize Flask templates to display different languages
- Learn how to infer the correct locale based on URL parameters, user settings or request headers
- Learn how to localize timestamps

## Tasks :pencil:

| Task                                             | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| ------------------------------------------------ | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------- |
| [0. Basic Flask app](./0-app.py)                 | First you will setup a basic Flask app in `0-app.py`. Create a single `/` route and an index.html template that simply outputs “Welcome to Holberton” as page title `(<title>) `and “Hello world” as header `(<h1>)`.                                                                                                                                                                                                                                             |
| [1. Basic Babel setup](./-app.py)                | Then instantiate the Babel object in your app. Store it in a module-level variable named babel.<br>In order to configure available languages in our app, you will create a Config class that has a LANGUAGES class attribute equal to ["en", "fr"].<br>Use Config to set Babel’s default locale ("en") and timezone ("UTC").<br>Use that class as config for your Flask app.                                                                                      |
| [2. Get locale from request](./2-app.py)         | Create a get_locale function with the babel.localeselector decorator.<br>Use request.accept_languages to determine the best match with our supported languages.                                                                                                                                                                                                                                                                                                   |
| [3. Parametrize templates](./3-app.py)           | Use the \_ or gettext function to parametrize your templates.<br>Use the message IDs home_title and home_header.<br>Create a babel.cfg file containing                                                                                                                                                                                                                                                                                                            |
| [4. Force locale with URL parameter](./4-app.py) | In this task, you will implement a way to force a particular locale by passing the locale=fr parameter to your app’s URLs.<br>In your get_locale function, detect if the incoming request contains locale argument and ifs value is a supported locale, return it.<br>.If not or if the parameter is not present, resort to the previous default behavior.<br>Now you should be able to test different translations by visiting `http://127.0.0.1:5000?locale=[fr | en]`.<br>Visiting `http://127.0.0.1:5000/?locale=fr` should display this level 1 heading: |
| [5. Mock logging in](./5-app.py)                 | Creating a user login system is outside the scope of this project.<br>To emulate a similar behavior, copy the following user table in `5-app.py`<br> ```users = {                                                                                                                                                                                                                                                                                                 |

    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},

| }```.                                        | <br>                                                                                                                                                                                                                                                                                                                                                                                                                           |
| -------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| [6. Use user locale](./6-app.py)             | Change your get_locale function to use a user’s preferred local if it is supported.<br>The order of priority should be<br>Locale from URL parameters<br>Locale from user settings<br>Locale from request header<br>Default locale<br>Test by logging in as different use                                                                                                                                                       |
| [7. Infer appropriate time zone](./7-app.py) | Define a get_timezone function and use the babel.timezoneselector decorator.<br>The logic should be the same as get_locale:<br>Find timezone parameter in URL parameters<br>Find time zone from user settings<br>Default to UTC<br>Before returning a URL-provided or user time zone, you must validate that it is a valid time zone. To that, use pytz.timezone and catch the pytz.exceptions.UnknownTimeZoneError exception. |
| [8. Display the current time](./app.py)      | Based on the inferred time zone, display the current time on the home page in the default format. For example:<br>Jan 21, 2020, 5:55:39 AM or 21 janv. 2020 à 05:56:28<br>Use the following translations                                                                                                                                                                                                                       |

## Author

[Betini Akarandut](www.github.com/betiniakarandut)
