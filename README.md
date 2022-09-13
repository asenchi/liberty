# Liberty Song Application

[https://liberty.pages.dev][]

## Introduction

In an effort to make managing songs for worship easier to manage the Liberty
Christian Church AV team built an application to manage songs and display for
them for church gatherings.

The application is a basic Python Flask application and the songs have been
distilled into a YAML format for ease of use around structures, keys, and
speeds (though the last two have not been maintained).

Songs are displayed on a black background with white text to make them easier
to see for the church's use case.

## Using the application

The application relies on the browser to supply most of the features. For
example, searching for songs is as simple as searching a web page in your
browser. Below is listed common actions and how to do them:

- **Search for a song**: Use the browser search
- **Open multiple songs**: Open each song into a tab and then use the browser
  keybindings to switch tabs/songs.
- **Move between "slides" within a song**: Songs may have multiple "slides",
  you can use the arrow keys to switch between these. Slides are listed at the
  bottom right hand corner.

## Common Keybindings

You can use the following keybindings to move around the site:

- 't': This will take you to the table of contents in the current tab.
- 'b': Blank out a page and display a black screen.
- 'left arrow': Previous slide
- 'right arrow': Next slide

## Adding songs

There is a link at the top of the table of contents for
['Help'](http://libertycc.herokuapp.com/help) and details the song structure.
Each song should be in a separate file within the `songs` directory and should
contain the song title (which is the first line of the song by convention) with
underscores replacing spaces. Songs are saved as a `.txt` file even though they
are YAML data structures.

### Two important things to remember

#### YAML Formatting of song structures

In order to format the song properly we use the [YAML literal block
scalar](https://yaml-multiline.info) (`|`) followed by whitespace on each line
(typically a single `space`).

Here is an example:

```
v1: |
 This is the first line of a verse
 This is the second
```

Note the leading `space`!

This will display properly on the page because of the `|` symbol (which treats
text as it is written) and the leading `space` on each line. This is VERY
IMPORTANT for displaying songs properly.

#### Song titles

Song titles are important in two places (a flaw in our design):

1. The name of the file
2. The name contained in the song file

Always use underscores to separate the name of the song in the file name and ensure it is a `.txt` file.

## A note about speed and key

There was a valiant attempt at trying to sort songs by key or speed, however
this never materialized. Most songs are listed as speed "z" or key "z". This
practice is continued with new songs.

## Deploying to Cloudflare

This site is now deployed to Cloudflare Pages: [https://liberty.pages.dev][]

## [DEPRECATED] Deploying to Heroku

1. GITHUB: Fork the [asenchi/libery](https://github.com/asenchi/liberty) application to your own user.
2. HEROKU: [Sign up for an account](https://heroku.com)
3. HEROKU: Using the dashboard, create a new application (choose a unique name for your application).
4. HEROKU: Connect the application to GitHub (make sure to choose your user/repo and **DO NOT USE** asenchi/liberty)
5. HEROKU: Select 'Enable Automatic Deploys' and ensure it is set to 'master' branch
6. HEROKU: Perform a 'Manual deploy' by choosing the 'master' branch and clicking 'Deploy Branch'

[https://liberty.pages.dev]: https://liberty.pages.dev
