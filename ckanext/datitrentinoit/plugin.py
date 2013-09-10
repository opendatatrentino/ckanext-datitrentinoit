## Plugin for http://dati.trentino.it
## Ckan: 2.2a

from ckan.plugins import (implements, SingletonPlugin, IConfigurer,
                          IRoutes, IDatasetForm, ITemplateHelpers)
import ckan.lib.base as base
import ckan.plugins.toolkit as plugins_toolkit
import routes.mapper as routes_mapper


class DatiTrentinoPlugin(SingletonPlugin):
    """Controller used to load custom templates/resources/pages"""

    implements(IConfigurer)
    implements(IRoutes)

    ## Implementation of IConfigurer :(
    ##------------------------------------------------------------

    def update_config(self, config):
        plugins_toolkit.add_public_directory(config, 'public')
        plugins_toolkit.add_template_directory(config, 'templates')
        plugins_toolkit.add_resource('fanstatic', 'ckanext-datitrentinoit')

    ## Implementation of IRoutes :(
    ##------------------------------------------------------------

    def before_map(self, routes):
        controller = 'ckanext.datitrentinoit.plugin:DatiTrentinoController'
        with routes_mapper.SubMapper(routes, controller=controller) as m:
            m.connect('faq', '/faq', action='faq')
            m.connect('acknowledgements', '/acknowledgements',
                      action='acknowledgements')
        return routes

    def after_map(self, routes):
        return routes


class DatiTrentinoController(base.BaseController):
    """Controller used to add custom pages"""

    def faq(self):
        return base.render('home/faq.html')

    def acknowledgements(self):
        return base.render('home/acknowledgements.html')


class DatiTrentinoFormPlugin(SingletonPlugin,
                             plugins_toolkit.DefaultDatasetForm):
    """
    Custom dataset form plugin for dati.trentino.it
    """

    implements(IDatasetForm)
    implements(ITemplateHelpers)

    _custom_text_fields = {
        'Aggiornamento': {
            'form_help': "es. mensile, giornaliero, annuale",
        },
        'Titolare': {
            'form_help': "es. Provincia Autonoma di Trento",
        },
        'Codifica Caratteri': {
            'form_help': "es. utf-8",
        },
        'Copertura Temporale (Data di fine)': {
            'form_help': "giorno/mese/anno",
        },
        'Copertura Temporale (Data di inizio)': {
            'form_help': "giorno/mese/anno",
        },
        'Data di aggiornamento': {
            'form_help': "giorno/mese/anno",
        },
        'Data di creazione': {
            'form_help': "giorno/mese/anno",
        },
        'Data di pubblicazione': {
            'form_help': "giorno/mese/anno",
        },
        'Descrizione campi': {
            'form_help': "",
        },
        'URL sito': {
            'form_help': "",
        },
    }

    def get_helpers(self):
        return {
            'dti_get_custom_fields': self._dti_get_custom_fields,
        }

    def _dti_get_custom_fields(self):
        return self._custom_text_fields

    def is_fallback(self):
        return True

    def package_types(self):
        return []

    def _modify_package_schema_for_edit(self, schema):
        for field_name in self._custom_text_fields:
            schema[field_name] = [
                plugins_toolkit.get_validator('ignore_missing'),
                plugins_toolkit.get_converter('convert_to_extras'),
            ]

    def _modify_package_schema_for_read(self, schema):
        for field_name in self._custom_text_fields:
            schema[field_name] = [
                plugins_toolkit.get_converter('convert_from_extras'),
                plugins_toolkit.get_validator('ignore_missing'),
            ]

    def create_package_schema(self):
        schema = super(DatiTrentinoFormPlugin, self).create_package_schema()
        self._modify_package_schema_for_edit(schema)
        return schema

    def update_package_schema(self):
        schema = super(DatiTrentinoFormPlugin, self).update_package_schema()
        self._modify_package_schema_for_edit(schema)
        return schema

    def show_package_schema(self):
        schema = super(DatiTrentinoFormPlugin, self).show_package_schema()
        ## todo: Do not remove custom fields from extras when rendering!
        ## but this is used when loading the model too...
        self._modify_package_schema_for_read(schema)
        return schema
