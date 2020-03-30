import datetime
from pyvis.network import Network
from mandalab_visual.consts import *

DEFAULT_GRAPH_NAME_FORMAT = "{graph_base}_{name}_{timestamp}.html"


def guess_if_running_in_notebook():
    try:
        from IPython import get_ipython
        if get_ipython() is None or 'IPKernelApp' not in get_ipython().config:
            return False
    except ImportError:
        return False
    return True


def generate_graph(machine, notebook=None, show=True, output_html_folder="graphs", output_html_name=None):
    """
    This function receives a machine and generate a network graph representing the network that the machine is in.
    :param machine: The mandalab machine to start the graph with.
    :param notebook: If None, will try to guess it.
    :param show: Show the output, or just save it to the output_html_folder. The html file will be generated any way.
    :param output_html_folder: The folder to save the output html file to.
    :param output_html_name: If None will generate automatic.
    :return: If Show=True, the output of show() (if using ipython or jupyter this must be thrown).
    """
    create_folder(output_html_folder)
    path = get_output_file_path(machine, output_html_folder, output_html_name)

    if notebook is None:
        notebook = guess_if_running_in_notebook()
    resources = NOTEBOOK_RES_PATH if notebook else LOCAL_RES_PATH  # can be Url, or local path.

    pyvis_net = Network(notebook=notebook)
    for port in machine.ports:
        _try_build_graph_from_port(pyvis_net, port, resources)

    if show:
        return pyvis_net.show(path)
    pyvis_net.save_graph(path)


def get_output_file_path(machine, output_html_folder, output_html_name):
    if not output_html_name:
        timestamp = datetime.datetime.now().strftime("%Y%m%d-%H%M%S")
        output_html_name = DEFAULT_GRAPH_NAME_FORMAT.format(graph_base="machine", name=machine.name,
                                                            timestamp=timestamp)  # TODO: get the name correctly
    path = os.path.join(output_html_folder, output_html_name)
    return path


def create_folder(output_html_folder):
    if not os.path.exists(output_html_folder):
        os.makedirs(output_html_folder)


def _try_build_graph_from_port(pyvis_net, port, resources):
    if port.network and port.network.name not in pyvis_net.get_nodes():
        _build_graph_from_network(pyvis_net, port.network, resources)


def get_machine_logo(machine):
    return COMPUTER_FILE_FORMAT.format(os=machine.os, status="on" if machine.on else "off")


def _build_graph_from_network(pyvis_net, mandalab_net, resources):
    pyvis_net.add_node(mandalab_net.name, shape="image", image=resources + NETWORK_FILE)
    for port in mandalab_net.ports:
        if port.machine.name not in pyvis_net.get_nodes():
            pyvis_net.add_node(port.machine.name, shape="image", image=resources + get_machine_logo(port.machine))
            pyvis_net.add_edge(mandalab_net.name, port.machine.name, title=port.name)

            for machine_port in port.machine.ports:
                _try_build_graph_from_port(pyvis_net, machine_port, resources)
        else:
            pyvis_net.add_edge(mandalab_net.name, port.machine.name, title=port.name)
