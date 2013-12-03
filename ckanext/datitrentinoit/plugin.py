# -*- coding: utf-8 -*-

## Plugin for http://dati.trentino.it
## Ckan: 2.2a

try:
    from collections import OrderedDict
except ImportError:
    from ordereddict import OrderedDict

from ckan.plugins import (implements, SingletonPlugin, IConfigurer,
                          IConfigurable, IRoutes, IDatasetForm,
                          ITemplateHelpers)
import ckan.lib.base as base
import ckan.plugins.toolkit as plugins_toolkit
import routes.mapper as routes_mapper


static_pages = ['faq', 'acknowledgements', 'legal_notes', 'privacy']
#static_pages = ['faq', 'acknowledgements']

GEO_AREAS = [
    u"Ala",
    u"Albiano",
    u"Aldeno",
    u"Altra area che interessa la Provincia di Trento",
    u"Altra area fuori della Provincia di Trento",
    u"Altro",
    u"Amblar",
    u"Andalo",
    u"Arco",
    u"Avio",
    u"Baselga di Pinè",
    u"Bedollo",
    u"Bersone",
    u"Besenello",
    u"Bieno",
    u"Bleggio Superiore",
    u"Bocenago",
    u"Bolbeno",
    u"Bondo",
    u"Bondone",
    u"Borgo Valsugana",
    u"Bosentino",
    u"Breguzzo",
    u"Brentonico",
    u"Bresimo",
    u"Brez",
    u"Brione",
    u"Caderzone Terme",
    u"Cagnò",
    u"Calavino",
    u"Calceranica al Lago",
    u"Caldes",
    u"Caldonazzo",
    u"Calliano",
    u"Campitello di Fassa",
    u"Campodenno",
    u"Canal San Bovo",
    u"Canazei",
    u"Capriana",
    u"Carano",
    u"Carisolo",
    u"Carzano",
    u"Castel Condino",
    u"Castelfondo",
    u"Castello-Molina di Fiemme",
    u"Castello Tesino",
    u"Castelnuovo",
    u"Cavalese",
    u"Cavareno",
    u"Cavedago",
    u"Cavedine",
    u"Cavizzana",
    u"Cembra",
    u"Centa San Nicolò",
    u"Cimego",
    u"Cimone",
    u"Cinte Tesino",
    u"Cis",
    u"Civezzano",
    u"Cles",
    u"Cloz",
    u"Comano Terme",
    u"Commezzadura",
    u"Comun General de Fascia",
    u"Comunità Alta Valsugana e Bersntol",
    u"Comunità Alto Garda e Ledro",
    u"Comunità della Paganella",
    u"Comunità della Val di Non",
    u"Comunità della Vallagarina",
    u"Comunità della Valle dei Laghi",
    u"Comunità della Valle di Cembra",
    u"Comunità della Valle di Sole",
    u"Comunità delle Giudicarie",
    u"Comunità di Primiero",
    u"Comunità Rotaliana-Koenigsberg",
    u"Comunità territoriale della Val di Fiemme",
    u"Comunità Valsugana e Tesino",
    u"Condino",
    u"Coredo",
    u"Croviana",
    u"Cunevo",
    u"Daiano",
    u"Dambel",
    u"Daone",
    u"Darè",
    u"Denno",
    u"Dimaro",
    u"Don",
    u"Dorsino",
    u"Drena",
    u"Dro",
    u"Faedo",
    u"Fai della Paganella",
    u"Faver",
    u"Fiavè",
    u"Fiera di Primiero",
    u"Fierozzo",
    u"Flavon",
    u"Folgaria",
    u"Fondo",
    u"Fornace",
    u"Frassilongo",
    u"Garniga Terme",
    u"Giovo",
    u"Giustino",
    u"Grauno",
    u"Grigno",
    u"Grumes",
    u"Imer",
    u"Isera",
    u"Ivano-Fracena",
    u"Lardaro",
    u"Lasino",
    u"Lavarone",
    u"Lavis",
    u"Ledro",
    u"Levico Terme",
    u"Lisignago",
    u"Livo",
    u"Lona-Lases",
    u"Luserna",
    u"Magnifica Comunità degli Altipiani cimbri",
    u"Malè",
    u"Malosco",
    u"Massimeno",
    u"Mazzin",
    u"Mezzana",
    u"Mezzano",
    u"Mezzocorona",
    u"Mezzolombardo",
    u"Moena",
    u"Molveno",
    u"Monclassico",
    u"Montagne",
    u"Mori",
    u"Nago-Torbole",
    u"Nanno",
    u"Nave San Rocco",
    u"Nogaredo",
    u"Nomi",
    u"Novaledo",
    u"Ospedaletto",
    u"Ossana",
    u"Padergnone",
    u"Palù del Fersina",
    u"Panchia",
    u"Peio",
    u"Pellizzano",
    u"Pelugo",
    u"Pergine Valsugana",
    u"Pieve di Bono",
    u"Pieve Tesino",
    u"Pinzolo",
    u"Pomarolo",
    u"Pozza di Fassa",
    u"Praso",
    u"Predazzo",
    u"Preore",
    u"Prezzo",
    u"Provincia di Trento",
    u"Rabbi",
    u"Ragoli",
    u"Revò",
    u"Riva del Garda",
    u"Romallo",
    u"Romeno",
    u"Roncegno Terme",
    u"Ronchi Valsugana",
    u"Roncone",
    u"Ronzo-Chienis",
    u"Ronzone",
    u"Roverè della Luna",
    u"Rovereto",
    u"Ruffrè-Mendola",
    u"Rumo",
    u"Sagron Mis",
    u"Samone",
    u"San Lorenzo in Banale",
    u"San Michele all Adige",
    u"Sant Orsola Terme",
    u"Sanzeno",
    u"Sarnonico",
    u"Scurelle",
    u"Segonzano",
    u"Sfruz",
    u"Siror",
    u"Smarano",
    u"Soraga",
    u"Sover",
    u"Spera",
    u"Spiazzo",
    u"Spormaggiore",
    u"Sporminore",
    u"Stenico",
    u"Storo",
    u"Strembo",
    u"Strigno",
    u"Taio",
    u"Tassullo",
    u"Telve",
    u"Telve di Sopra",
    u"Tenna",
    u"Tenno",
    u"Terlago",
    u"Terragnolo",
    u"Terres",
    u"Territorio della Val d Adige",
    u"Terzolas",
    u"Tesero",
    u"Tione di Trento",
    u"Ton",
    u"Tonadico",
    u"Torcegno",
    u"Trambileno",
    u"Transacqua",
    u"Trento",
    u"Tres",
    u"Tuenno",
    u"Valda",
    u"Valfloriana",
    u"Vallarsa",
    u"Varena",
    u"Vattaro",
    u"Vermiglio",
    u"Vervò",
    u"Vezzano",
    u"Vignola-Falesina",
    u"Vigo di Fassa",
    u"Vigolo Vattaro",
    u"Vigo Rendena",
    u"Villa Agnedo",
    u"Villa Lagarina",
    u"Villa Rendena",
    u"Volano",
    u"Zambana",
    u"Ziano di Fiemme",
    u"Zuclo"]


class DatiTrentinoPlugin(SingletonPlugin):
    """Controller used to load custom templates/resources/pages"""

    implements(IConfigurer)
    implements(IConfigurable)
    implements(IRoutes)
    implements(ITemplateHelpers)

    ## Implementation of IConfigurer :(
    ##------------------------------------------------------------

    def update_config(self, config):
        plugins_toolkit.add_public_directory(config, 'public')
        plugins_toolkit.add_template_directory(config, 'templates')
        plugins_toolkit.add_resource('fanstatic', 'ckanext-datitrentinoit')

    ## Implementation of IConfigurable :(
    ##------------------------------------------------------------

    def configure(self, config):
        self.ga_conf = {
            'id': config.get('googleanalytics.id'),
            'domain': config.get('googleanalytics.domain'),
        }

    ## Implementation of IRoutes :(
    ##------------------------------------------------------------

    def before_map(self, routes):
        controller = 'ckanext.datitrentinoit.plugin:DatiTrentinoController'
        with routes_mapper.SubMapper(routes, controller=controller) as m:
            for page_name in static_pages:
                page_slug = page_name.replace('_', '-')
                m.connect(page_name, '/' + page_slug, action=page_name)
        return routes

    def after_map(self, routes):
        return routes

    ## Implementation of ITemplateHelpers :(
    ##------------------------------------------------------------

    def get_helpers(self):
        return {
            'dti_ga_site_id': self._get_ga_site_id,
            'dti_ga_site_domain': self._get_ga_site_domain,
        }

    def _get_ga_site_id(self):
        return self.ga_conf['id']

    def _get_ga_site_domain(self):
        return self.ga_conf['domain']


class DatiTrentinoController(base.BaseController):
    """Controller used to add custom pages"""


for page_name in static_pages:
    def get_action(name):
        def action(self):
            return base.render('pages/{0}.html'.format(name))
        return action
    action = get_action(page_name)
    action.__name__ = page_name
    setattr(DatiTrentinoController, page_name, action)


class DatiTrentinoFormPlugin(SingletonPlugin,
                             plugins_toolkit.DefaultDatasetForm):
    """
    Custom dataset form plugin for dati.trentino.it
    """

    implements(IDatasetForm)
    implements(ITemplateHelpers)

    _custom_text_fields = OrderedDict([
        ('Titolare', {
            'form_help': "es. Provincia Autonoma di Trento",
        }),
        ('Descrizione campi', {
            'form_help': "",
        }),
        ('Copertura Geografica', {
            'form_help': "es. Comune di Trento",
            'options': [''] + GEO_AREAS,
        }),
        ('Copertura Temporale (Data di inizio)', {
            'form_help': "giorno/mese/anno",
        }),
        ('Copertura Temporale (Data di fine)', {
            'form_help': "giorno/mese/anno",
        }),
        ('Aggiornamento', {
            'form_help': "es. mensile, giornaliero, annuale",
        }),

        ('Data di creazione', {
            'form_help': "giorno/mese/anno",
        }),
        ('Data di pubblicazione', {
            'form_help': "giorno/mese/anno",
        }),
        ('Data di aggiornamento', {
            'form_help': "giorno/mese/anno",
        }),

        ('Codifica Caratteri', {
            'form_help': "Esempio: utf-8, latin-1, pc-850.",
        }),

        ('URL sito', {
            'form_help': "",
        }),
    ])

    def get_helpers(self):
        return {
            'dti_get_custom_fields': self._dti_get_custom_fields,
            'dti_geo_areas': GEO_AREAS,
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
