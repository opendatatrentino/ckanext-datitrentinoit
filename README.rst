Ckan plugin for dati.trentino.it
################################

Ckan_ plugin containing customizations for http://dati.trentino.it

.. _Ckan: http://ckan.org

Installation
============

1. Install this package
2. Add ``datitrentinoit`` to Ckan plugins


Translations
============

* Install babel + jinja (contains a babel extractor)
* Use babel commands: ``extract_messages``, ``init_catalog``,
  ``update_catalog``, ``compile_catalog``.
* ~~We need to figure out a way to:~~

  * ~~Inject own translations in the global namespace~~
  * ~~Use our ``ckanext-datitrentinoit`` translations along with the
    ones from the Ckan core.~~


**Update:** problems with translations now solved: see this project
https://github.com/opendatatrentino/ckan-custom-translations
