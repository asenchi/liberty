# Liberty Song Application

## Introduction

In an effort to make managing songs for worship easier to manage the Liberty
Christian Church AV team built an application to manage songs and display for
them for church gatherings.

The application is a basic Python Flask application and the songs have been
distilled into a YAML format for ease of use around structures, keys, and
speeds (though the last two have not been maintained).

Songs are displayed on a black background with white text to make them easier
to see for the church's use case.

## Deploying to Heroku

1. GITHUB: Fork the [asenchi/libery](https://github.com/asenchi/liberty) application to your own user.
2. HEROKU: [Sign up for an account](https://heroku.com)
3. HEROKU: Using the dashboard, create a new application (choose a unique name for your application).
4. HEROKU: Connect the application to GitHub (make sure to choose your user/repo and **DO NOT USE** asenchi/liberty)
5. HEROKU: Select 'Enable Automatic Deploys' and ensure it is set to 'master' branch
6. HEROKU: Perform a 'Manual deploy' by choosing the 'master' branch and clicking 'Deploy Branch'
