from mininet.topo import Topo

class TestTopo(Topo):
    def __init__(self):
        Topo.__init__(self)

        leftHost = self.addHost('h1')
        rightHost = self.addHost('h2')
        leftSwitch = self.addSwitch('s1')

        self.addLink(leftHost,leftSwitch)
        self.addLink(rightHost,leftSwitch)

topos = { 'mytopo': TestTopo}