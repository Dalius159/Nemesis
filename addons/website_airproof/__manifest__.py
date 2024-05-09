{
   'name': 'Airproof Theme',
   'category': 'Website/Theme',
   'version': '15.0.0',
   "license": "Other proprietary",
   "author": "Your Name",
   "application": True,
   "installable": True,
   "auto_install": False,
   'depends': ['base','website','website_blog'],
   'data': [
       'data/presets.xml',
       'data/images.xml',
       'data/menu.xml',
       'data/pages/about_us.xml',
       'views/website_templates.xml',
       'views/snippets/s_airproof_snippet.xml',
       'views/snippets/options.xml',
   ],
   'assets': {
       'web._assets_primary_variables': [
            ('append', 'website_airproof/static/src/scss/primary_variables.scss'),
        ],
        'web._assets_frontend_helpers': [
            ('append', 'website_airproof/static/src/scss/bootstrap_overridden.scss'),
        ],
        'web.assets_frontend': [
            'website_airproof/static/src/scss/theme.scss',
        ],
   },
}