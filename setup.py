from setuptools import setup, find_packages

version = '0.1'

entry_points = {
    'ckan.plugins': [
        "datitrentinoit = ckanext.datitrentinoit.plugin:DatiTrentinoPlugin",
    ],
}

setup(
    name='ckanext-datitrentinoit',
    version=version,
    description="CKAN customizations for dati.trentino.it",
    long_description="CKAN customizations for dati.trentino.it",
    author="Samuele Santi",
    author_email="samuele.santi@trentorise.eu",
    url='http://dati.trentino.it',
    license='Affero GPL',
    classifiers=[],
    packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
    namespace_packages=['ckanext', 'ckanext.datitrentinoit'],
    include_package_data=True,
    zip_safe=False,
    install_requires=[],
    entry_points=entry_points,
)
