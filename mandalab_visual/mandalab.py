
class Machine:
    def __init__(self, name, ports=None):
        self.name = name
        self.ports = ports if ports else []

    def add_port(self, name: str):
        self.ports.append(Port(self, name))

    def add_ports(self, names: list):
        for name in names:
            self.add_port(name)


class Network:
    def __init__(self, name):
        self.name = name
        self.partners = []

    def _connect(self, obj):
        self.partners.append(obj)

    def connect(self, partner):
        self._connect(partner)
        partner._connect(self)


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
