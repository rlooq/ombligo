AUTHOR = 'Rafa Luque'
SITENAME = 'Ombligo de la galaxia'
SITEURL = 'https://www.ombligodelagalaxia.es'
THEME = 'theme'

PATH = 'content'

TIMEZONE = 'Europe/Madrid'
DEFAULT_DATE_FORMAT = '%d-%m-%Y'
DEFAULT_LANG = 'es'
GOOGLE_ANALYTICS = "GOOGLE ANALYTICS"

SITESUBTITLE = ""
BIO = "Blog personal y almacén de relatos muy cortos, poesía y otros juegos lingüísticos."
PROFILE_IMAGE = 'calling.jpg'
FOOTER_TEXT = '© 2022. Rafa Luque. Todos los derechos reservados.'
COLOR_THEME = '0x'
DIRECT_TEMPLATES = ['index', 'archives']
CATEGORY_SAVE_AS = ''
TAG_SAVE_AS = ''
AUTHOR_SAVE_AS = ''
ARCHIVES_SAVE_AS = 'archive.html'
SUMMARY_MAX_LENGTH = 36
DISPLAY_PAGES_ON_MENU = False
MENUITEMS = (
        ('¿Qué es esto?', 'https://www.ombligodelagalaxia.es/pages/que-es-esto.html'),
        ('Archivo', 'https://www.ombligodelagalaxia.es/archive.html'),
        ('In English', 'https://www.highnoon-ruffles.com'),
        )

FONT_AWESOME_JS = 'https://kit.fontawesome.com/829b54ddaf.js'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

FEED_DOMAIN = SITEURL
STATIC_PATHS = ['images', 'extras']
EXTRA_PATH_METADATA = {
    'extras/robots.txt': {'path': 'robots.txt'},
    'extras/favicon.ico': {'path': 'favicon.ico'},
    'extras/favicon-16x16.png': {'path': 'favicon-16x16.png'},
    'extras/favicon-32x32.png': {'path': 'favicon-32x32.png'},
}


PLUGINS = ['sitemap']

SITEMAP = {
    'format': 'xml',
    'priorities': {
        'articles': 0.6,
        'indexes': 0.5,
        'pages': 0.4
    },
    'changefreqs': {
        'articles': 'weekly',
        'indexes': 'weekly',
        'pages': 'monthly'
    }
}

# Social widget
SOCIAL = (('twitter', 'https://twitter.com/rafa_luque'),
        ('instagram', 'https://www.instagram.com/randomlooq/'),
        ('github', 'https://github.com/rlooq'),
        ('email', 'rlooq@yahoo.com')
        )

DEFAULT_PAGINATION = False

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True
