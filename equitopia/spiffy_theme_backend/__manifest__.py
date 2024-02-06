# -*- coding: utf-8 -*-
# Developed by Bizople Solutions Pvt. Ltd.
# See LICENSE file for full copyright and licensing details
{
    'name': 'Spiffy Backend Theme',
    'category': 'Themes/Backend',
    'version': '13.0.0.1',
    'author': 'Bizople Solutions Pvt. Ltd.',
    'website': 'https://www.bizople.com/',
    'summary': 'The ultimate Odoo Backend theme with the most advanced key features of all time. Get your own personalized view while working on the Backend system with a wide range of choices. Spiffy theme has 3 in 1 Theme Style, Progressive Web App, Fully Responsive for all apps, Configurable Apps Icon, App Drawer with global search, RTL & Multi-Language Support, Tree-Form Split view, and many other key features.',
    'description': """ The ultimate Odoo Backend theme with the most advanced key features of all time. Get your own personalized view while working on the Backend system with a wide range of choices. Spiffy theme has 3 in 1 Theme Style, Progressive Web App, Fully Responsive for all apps, Configurable Apps Icon, App Drawer with global search, RTL & Multi-Language Support, Tree-Form Split view, and many other key features. """,
    'depends': ['web', 'base_setup', 'portal', 'resource'],
    'data': [
        'security/ir.model.access.csv',
        'data/backend_config_data.xml',
        'data/global_level_config.xml',
        'views/manifest.xml',
        'views/pwa_offline.xml',
        'views/assets.xml',
        'views/backend_configurator_view.xml',
        'views/backend_configurator_template.xml',
        'views/res_config_setting.xml',
        'views/login_page_style.xml',
        'views/templates_inherit.xml',
        'views/ir_module_view.xml',
        'views/pwa_shortcuts_view.xml',
        'views/menuitems.xml',
    ],
    'demo': [
        'data/spiffy_default_images.xml',
    ],
    'qweb': [
        "static/src/xml/web_inherit.xml",
        "static/src/xml/menu.xml",
        "static/src/xml/bookmark.xml",
        "static/src/xml/base.xml",
        "static/src/xml/controlpanel.xml",
        "static/src/xml/view_button_icons.xml",
    ],
    'live_test_url': 'http://bit.ly/3Oq8T3H',
    'images': [
        'static/description/spiffy_cover.png',
        'static/description/spiffy_screenshot.gif',
    ],
    'sequence': 1,
    'installable': True,
    'application': True,
    'price': 147,
    'license': 'OPL-1',
    'currency': 'EUR',
}
