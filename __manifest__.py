{
    'name': 'Gestion des étudiants',
    'version': '1.0',
    'category': 'Education',
    'summary': 'Module de gestion des étudiants',
    'author': 'Abdelhakim Benbouanane',
    'website': 'https://www.example.com',
    'depends': ['base'],
    'data': [
        'views/etudiant_view.xml',
        'views/cours_view.xml',
        'views/professeur_view.xml',
        'security/ir.model.access.csv',
    ],
    'installable': True,
    'application': True,
}
