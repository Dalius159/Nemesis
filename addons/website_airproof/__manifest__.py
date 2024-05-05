{
   'name': 'Airproof Theme',
   'category': 'Website/Theme',
   'version': '15.0.0',
   "license": "Other proprietary",
   "author": "Your Name",
   "application": True,
   "installable": True,
   "auto_install": False,
   'depends': ['website'],
   'data': [
       'data/presets.xml',
       'views/website_templates.xml',
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