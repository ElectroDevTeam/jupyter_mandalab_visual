from mandalab import *


def generate_network():
    m1 = Machine("m1", on=True)
    m1.add_ports(["eth0", "eth1", "eth2"])
    m2 = Machine("m2", on=False)
    m2.add_ports(["eth0", "eth1", "eth33"])
    m3 = Machine("m3", on=True, os="windows")
    m3.add_port("eth10")
    net1 = Network("net1")
    net1.connect(m1.ports[0])
    net1.connect(m2.ports[0])
    net1.connect(m3.ports[0])
    m4 = Machine("m3", on=False, os="windows")
    m4.add_port("eth10")
    net2 = Network("net2")
    net2.connect(m4.ports[0])
    net2.connect(m1.ports[1])
    return m1