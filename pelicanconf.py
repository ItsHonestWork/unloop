from __future__ import unicode_literals
AUTHOR = 'ItsHonestWork'
SITENAME = 'Unloop'
SITE_SUBTITLE = 'Dare to Break the Cycle'
SITE_DESCRIPTION = 'Unloop empowers you to track and understand your OCD patterns with ease. Log and analyze your triggers, obsessions, and rituals privately — and take the first step toward freedom.'
SITEURL = ""

OUTPUT_PATH = "public"
PATH = "content"
PAGE_PATHS = ['pages']
STATIC_PATHS = ['static/assets/img/']
RELATIVE_URLS = False
TIMEZONE = 'Europe/Berlin'
DEFAULT_DATE_FORMAT = '%a %d %B %Y'
DEFAULT_LANG = 'en'
DIRECT_TEMPLATES = ['index']
NAV_POSITION = 'centered'  # 'top' or 'centered'

THEME = 'theme/'
THEME_STATIC_PATHS = ['static']
READERS = {'html': None}

# Header external links
HEADER_EXTERNAL_LINKS = [
    {'name': 'GitHub', 'url': 'https://github.com/ItsHonestWork/unloop', 'icon': 'bi-github'},
    # Add more external links as needed
]

# Footer content
FOOTER_CONTENT = {
    'about': 'Unloop is designed to help users with Obsessive-Compulsive Disorder (OCD) log and analyze their patterns efficiently and privately.',
    'contact': '',
    'links': [
    ]
}

# New variable for the page title at the logo place
PAGE_TITLE = ''
