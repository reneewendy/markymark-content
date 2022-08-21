AUTHOR = 'Wendy Northcutt'
SITENAME = 'Reboot Darwin Awards'
SITEURL = ''

PATH = 'content'
gPAGE_PATHS = ['page']     # static content.
ARTICLE_PATHS = ['article', 'darwin', 'stupid', 'rules']     # generated content.

TIMEZONE = 'America/Los_Angeles'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Darwin Awards', 'https://darwinawards.com/darwin/'),
         ('Honorable Mentions', 'https://darwinawards.com/stupid/'),
         ('Rules', 'https://darwinawards.com/rules/'),
         ('Slush', 'https://darwinawards.com/slush/new'),)

# Social widget
SOCIAL = (('Facebook Darwin', 'https://www.facebook.com/TheDarwinAwards'),
          ('Twitter Darwin', 'https://twitter.com/DarwinAwards'),
          ('Homepage Darwin', 'https://darwinawards.com'),)

THEME_TEMPLATES_OVERRIDES = ['theme/notmyidea/templates']  # works for base.html index.html override.
### Autust 2022 -- STATIC WRONGLY SOURCES FROM ./venv/pelican/lib/python3.8/site-packages/pelican/themes/notmyidea/static/css/main.css
### Failed to source these static files from the local themes directory,
### tried many combinations of settings and paths.
### Currently the best idea I have, is to uncomment static_excludes and
### Ref: https://docs.getpelican.com/en/stable/settings.html
### Ref: https://stackoverflow.com/questions/61040131/why-does-pelican-ignore-static-paths
THEME_STATIC_PATHS = ['theme/notmyidea/static']           # does NOT seem to source css...
# STATIC_EXCLUDES = ['./venv/pelican/lib/python3.8/site-packages/pelican/themes/notmyidea/static/css/main.css']

DEFAULT_PAGINATION = False

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
