import datetime
import os
from pathlib import Path

from pyvis.network import Network

from mandalab_visual import mandalab

DEFAULT_GRAPH_NAME_FORMAT = "{graph_base}_{name}_{timestamp}.html"


def generate_graph(machine, notebook=False, output_html_folder="graphs", output_html_name=None):
    if not output_html_name:
        timestamp = datetime.datetime.now().strftime("%Y%m%d-%H%M%S")
        output_html_name = DEFAULT_GRAPH_NAME_FORMAT.format(graph_base="machine", name=machine.name, timestamp=timestamp) # TODO: get the name correctly
    pyvis_net = Network(notebook=notebook)
    path = os.path.join(output_html_folder, output_html_name)

    for port in machine.ports:
        _try_build_graph(pyvis_net, port)
    if notebook:
        pyvis_net.show(path)
    else:
        pyvis_net.save_graph(path)
    return pyvis_net


def _try_build_graph(pyvis_net, port):
    if port.network and port.network.name not in pyvis_net.get_nodes():
        _build_graph(pyvis_net, port.network)


def _build_graph(pyvis_net, mandalab_net):
    print("!")
    #pyvis_net.add_node(mandalab_net.name, shape="image", image=str(Path("res/network.png")))
    pyvis_net.add_node(mandalab_net.name, shape="image", image=r"C:\dev\electro\jupyter_mandalab_visual\mandalab_visual\res\network.png")
    #pyvis_net.add_node(mandalab_net.name)
    for port in mandalab_net.partners:
        if isinstance(port, mandalab.Port): # TODO: Handle a network object.
            if port.machine.name not in pyvis_net.get_nodes():
                pyvis_net.add_node(port.machine.name, shape="image", image=r"C:\dev\electro\jupyter_mandalab_visual\mandalab_visual\res\computer.png")
                #pyvis_net.add_node(port.machine.name)
                pyvis_net.add_edge(mandalab_net.name, port.machine.name, title=port.name)

                for machine_port in port.machine.ports:
                    _try_build_graph(pyvis_net, machine_port)
            else:
                pyvis_net.add_edge(mandalab_net.name, port.machine.name, title=port.name)
    """
    # TODO: verify this node does not exist already.
    if mandalab_net.isinstance(mandalab.Network):
        image = Path("res/network.png")
    else:
        image = Path("res/computer.png")
    pyvis_net.add_node(mandalab_net.name, image=image)
    # TODO: add a title for the port names
    # TODO: show os, if locked or not, if locked by me, if turned on or not.
    # TODO: verify this connection does not exist alraedy.
    if last_obj:
        pyvis_net.add_edge(last_obj.name, mandalab_net.name)
    """
