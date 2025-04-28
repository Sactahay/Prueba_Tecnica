# -*- coding: utf-8 -*-
{
    'name': "Proyectos de Investigación",
    'summary': """
        Módulo para gestionar proyectos de investigación.
    """,
    'description': """
        Este módulo permite la gestión integral de proyectos de investigación,
        incluyendo información detallada, investigadores, estados, presupuesto
        y generación de informes.
    """,
    'author': "Jairo Sac",
    'website': "Tu Sitio Web",
    'category': 'Project',
    'version': '1.0',
    'depends': ['base', 'mail'],
    'data': [
        'security/research_project_security.xml',
        'security/ir.model.access.csv',
        'data/ir_sequence_data.xml',
        'views/research_project_views.xml',
        'reports/research_project_reports.xml',
    ],
    'demo': [],
    'installable': True,
    'application': True,
    'auto_install': False,
}