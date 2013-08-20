## Plugin for http://dati.trentino.it

from ckan.plugins import implements, IConfigurer, SingletonPlugin
import ckan.plugins.toolkit as plugins_toolkit


class DatiTrentinoPlugin(SingletonPlugin):

    implements(IConfigurer)

    def update_config(self, config):
        plugins_toolkit.add_public_directory(config, 'public')
        plugins_toolkit.add_template_directory(config, 'templates')
        plugins_toolkit.add_resource('fanstatic', 'ckanext-datitrentinoit')
