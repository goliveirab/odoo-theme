{
  'name':'Tutorial theme',
  'description': 'A first theme for Odoo',
  'version':'1.0',
  'author':'goliveirab',

  'data': [
      'views/assets.xml',
      'views/layout.xml',
      'views/pages.xml',
  ],
  'category': 'Theme/Creative',
  'depends': [
      'website',
      'website_less',
  ],
  'application': True,
}
