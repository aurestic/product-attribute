# -*- coding: utf-8 -*-
# Copyright 2018 Tecnativa - Sergio Teruel, Aures TIC - Almudena De la Puente
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

{
    'name': 'Product Cost Security',
    'summary': 'Product cost security restriction view',
    'version': '8.0.1.0.0',
    'category': 'Product',
    'website': 'https://github.com/OCA/product-attribute',
    'author': 'Tecnativa, Odoo Community Association (OCA), Aures TIC',
    'license': 'AGPL-3',
    'application': False,
    'installable': True,
    'depends': [
        'product',
        'stock_account',
    ],
    'data': [
        'security/product_cost_security.xml',
        'views/product_views.xml',
    ],
}
