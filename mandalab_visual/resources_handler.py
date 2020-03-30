import tornado
import tornado.web
from notebook.utils import url_path_join

from mandalab_visual.consts import NOTEBOOK_RES_PATH, LOCAL_RES_PATH


def load_jupyter_server_extension(nb_app):
    """Registers the deepsearch API handler to receive HTTP requests from the frontend extension.
    Parameters
    ----------
    nb_app: notebook.notebookapp.NotebookApp
        Notebook application instance
    """

    web_app = nb_app.web_app
    host_pattern = '.*$'
    route_pattern = url_path_join(web_app.settings['base_url'], NOTEBOOK_RES_PATH + '(.*)')
    web_app.add_handlers(host_pattern, [(route_pattern, tornado.web.StaticFileHandler,
                                        {'path': LOCAL_RES_PATH})])
    nb_app.log.info(f'Registered mandalab\'s StaticFileHandler extension at URL path {route_pattern}')
    # TODO: If using this feature using jupyter gui. create the html in local path- lests say /api/mandalab/graphs (chagne output_html_folder to it).