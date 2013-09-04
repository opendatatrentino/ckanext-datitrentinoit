## Plugin for http://dati.trentino.it
## Ckan: 2.2a

from ckan.plugins import implements, SingletonPlugin, IConfigurer, IRoutes
import ckan.lib.base as base
import ckan.plugins.toolkit as plugins_toolkit
import routes.mapper as routes_mapper


class DatiTrentinoPlugin(SingletonPlugin):

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
    def faq(self):
        return base.render('home/faq.html')

    def acknowledgements(self):
        return base.render('home/acknowledgements.html')
