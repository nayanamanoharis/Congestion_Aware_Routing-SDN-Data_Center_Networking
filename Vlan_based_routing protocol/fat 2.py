from mininet.topo import Topo

class FatTopo(Topo):
    def __init__(self):
        Topo.__init__(self)

        swId = 0;

        self.hosts_ = [
                self.addHost('h%d' % hostId, ip='10.0.0.%d/27' % hostId)
                for hostId in range(16)]

        self.edge_switches_ = [
                self.addSwitch('es%d' % switchId, dpid=("%0.2X" % (switchId+1)))
                for switchId in range(8)]
        
        self.aggregate_switches_ = [
                self.addSwitch('as%d' % switchId, dpid=("%0.2X" % (switchId+9)))
                for switchId in range(8)]

        self.core_switches_ = [
                self.addSwitch('cs%d' % switchId, dpid=("%0.2X" % (switchId+17)))
                for switchId in range(4)]

        self.hostLinks_odd_ = [
                self.addLink('h%d' % ((2*eId)+1), 'es%d' % (eId),0,2)
                for eId in range(8)]
 
        self.hostLinks_even_ = [
                self.addLink('h%d' % (2*eId), 'es%d' % (eId),0,1)
                for eId in range(8)]

        self.eswitch_to_aswitch_Links1_ = [
                self.addLink('es%d' % eId, 'as%d' % (eId), 3,1)
                for eId in range(8)]

        self.eswitch_to_aswitch_Links2_ = [
                self.addLink('es%d' % (2*eId), 'as%d' % ((2*eId)+1), 4,2)
                for eId in range(4)]

        self.eswitch_to_aswitch_Links3_ = [
                self.addLink('es%d' % ((2*eId)+1), 'as%d' % (2*eId), 4,2)
                for eId in range(4)]

        self.c2alinks1 =self.addLink('cs0' , 'as0' , 1,3)
        self.c2alinks1 =self.addLink('cs0' , 'as2' , 2,3)
        self.c2alinks1 =self.addLink('cs0' , 'as4' , 3,3)
        self.c2alinks1 =self.addLink('cs0' , 'as6' , 4,3)
        self.c2alinks1 =self.addLink('cs1' , 'as0' , 1,4)
        self.c2alinks1 =self.addLink('cs1' , 'as2' , 2,4)
        self.c2alinks1 =self.addLink('cs1' , 'as4' , 3,4)
        self.c2alinks1 =self.addLink('cs1' , 'as6' , 4,4)
        self.c2alinks1 =self.addLink('cs2' , 'as1' , 1,3)
        self.c2alinks1 =self.addLink('cs2' , 'as3' , 2,3)
        self.c2alinks1 =self.addLink('cs2' , 'as5' , 3,3)
        self.c2alinks1 =self.addLink('cs2' , 'as7' , 4,3)
        self.c2alinks1 =self.addLink('cs3' , 'as1' , 1,4)
        self.c2alinks1 =self.addLink('cs3' , 'as3' , 2,4)
        self.c2alinks1 =self.addLink('cs3' , 'as5' , 3,4)
        self.c2alinks1 =self.addLink('cs3' , 'as7' , 4,4)
                       


    @classmethod
    def create(cls):
        return cls()

topos = {'fattopo': FatTopo.create}





        
        
        
