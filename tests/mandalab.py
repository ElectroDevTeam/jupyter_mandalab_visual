
class Machine:
    def __init__(self, name, ports=None, on=False, os="linux"):
        self.name = name
        self.ports = ports if ports else []
        self.on = on
        self.os = os

    def add_port(self, name: str):
        self.ports.append(Port(self, name))

    def add_ports(self, names: list):
        for name in names:
            self.add_port(name)


class Network:
    def __init__(self, name):
        self.name = name
        self.ports = []

    def _connect(self, obj):
        self.ports.append(obj)

    def connect(self, port):
        self._connect(port)
        port._connect(self)


class Port:
    def __init__(self, machine: Machine, name):
        self.name = name
        self.machine = machine
        self.network = None

    def _connect(self, network):
        self.network = network

    def connect(self, network):
        self._connect(network)
        network._connect(self)
