import mandalab_visual


def generate_network():
    m1 = mandalab_visual.mandalab.Machine("m1", on=True)
    m1.add_ports(["eth0", "eth1", "eth2"])
    m2 = mandalab_visual.mandalab.Machine("m2", on=False)
    m2.add_ports(["eth0", "eth1", "eth33"])
    m3 = mandalab_visual.mandalab.Machine("m3", on=True, os="windows")
    m3.add_port("eth10")
    net1 = mandalab_visual.mandalab.Network("net1")
    net1.connect(m1.ports[0])
    net1.connect(m2.ports[0])
    net1.connect(m3.ports[0])
    m4 = mandalab_visual.mandalab.Machine("m3", on=False, os="windows")
    m4.add_port("eth10")
    net2 = mandalab_visual.mandalab.Network("net2")
    net2.connect(m4.ports[0])
    net2.connect(m1.ports[1])
    return m1