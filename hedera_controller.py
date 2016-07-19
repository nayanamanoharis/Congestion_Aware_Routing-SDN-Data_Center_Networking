#!/usr/bin/python

from ryu.base import app_manager
from ryu.controller import ofp_event, dpset
from ryu.controller.handler import MAIN_DISPATCHER
from ryu.controller.handler import set_ev_cls
from ryu.lib.ip import ipv4_to_bin
import thread
import socket
import threading
import time

#Referred from Youtube another tutorial cited on the link
class Node(object):
    def __init__ (self, d, n=None):
        self.data = d
        self.next_node =n
    def get_next (self): 
        return self.next_node
    def set_next (self, n):
        self.next_node = n
    def get_data (self):
        return self.data
    def set_data (self, d):
        self.data =d
        
class LinkedList (object):
    def __init__(self, r = None):
        self.root = r
        self.size = 0
    def get_size (self):
        return self.size
    def add (self, d):
        new_node = Node (d, self.root)
        self.root = new_node
        self.size += 1
    def remove (self,d):
        this_node = self.root
        prev_node = None
        while this_node:
            if this_node.get_data() == d:
                if prev_node:
                    prev_node.set_next(this_node.get_next())
                else:
                    self.root = this_node
                self.size -= 1
                return True       #data removed
            else:
                prev_node = this_node
                this_node = this_node.get_next()
            return False #data not found        
    def find (self, d):
        this_node = self.root
        while this_node:
            if this_node.get_data() == d:
                return d
            else:
                this_node = this_node.get_next()
        return None
    
mylist = LinkedList()
#print("created Linkedlist")    
    
    
class Controller(app_manager.RyuApp):
    def __init__(self):
        super(Controller, self).__init__()
        t = threading.Thread(target=self.Client)
        t.start() 
    
    #Referred from the TCP communication Python tutorial 
    def Client(self):
        data_value = "a"
        des_ip_temp =" "
        des_ip=" "
        act_size_temp = " "
        act_size = " " 
        full_size_temp = " "
        full_size = " "
        int_full_size =0
        int_act_size =0
        esA = [0,0,0,0,0,0,0,0]
        esB = [0,0,0,0,0,0,0,0]
        asA = [0,0,0,0,0,0,0,0]
        asB = [0,0,0,0,0,0,0,0]
        
        while(1):
            for y in range(1,17):
                TCP_IP = '20.0.0.'+str(y)
                #print "Ip address:", TCP_IP
                TCP_PORT = 5000
                BUFFER_SIZE = 1024
                MESSAGE = "Nayana Client message"            
                s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                #n = mylist.root
                #while n != None:
                #        print "EV.DP.ID:=",n.data.id
                #        n = n.next_node

                while 1:
                    try:
                        s.connect((TCP_IP, TCP_PORT))
                        print "connect successful"
                        break
                    except:
                        pass
                s.send(MESSAGE)
                data = s.recv(BUFFER_SIZE)
                print "Receiving:", data
                data_value = data
                #for i in range(0,len(data_value)):
                #    print "index := ",i, "data_value:=",data_value[i]
                for i in range(0,8):
                    des_ip_temp += data_value[i];
                des_ip = des_ip_temp
                des_ip_temp = " "
                #print "des_ip:=",des_ip
                for i in range(32,53):
                    act_size_temp += data_value[i] 
                act_size = act_size_temp
                act_size_temp = " "
                #print "act_size :=", act_size
                for i in range(54,74):
                    full_size_temp += data_value[i]
                full_size = full_size_temp
                full_size_temp = " "
                #print "full_size:=",full_size
                #if (act_size != " " or full_size != " "):
                int_act_size = act_size
                int_full_size = full_size
                div_y = y
                div_y = (y/2)
                div_mul_y = y
                if y%2 == 1:
                    div_y = (y/2)
                    div_y = div_y +1
                #print "div_y",div_y    
                div_agg_y = div_y + 8
                #print "div_agg_y",div_agg_y
                #
                div_mod_1 = div_agg_y +1
                div_mod_0 = div_agg_y -1
                variable = mylist.root
                while variable != None:
                    if variable.data.id == div_y:
                        n1 = variable
                        #print "variable1:=",n1.data.id
                    variable = variable.next_node
                variable = mylist.root    
                while variable != None:
                    if variable.data.id == div_agg_y:
                        n2 = variable
                        #print "variable2:=",n2.data.id        
                    variable = variable.next_node
                variable = mylist.root    
                while variable != None:
                    if variable.data.id == div_mod_1:
                        n3 = variable
                        #print "variable3:=",n3.data.id        
                    variable = variable.next_node  
                variable = mylist.root    
                while variable != None:
                    if variable.data.id == div_mod_0:
                        n4 = variable
                        #print "variable4:=",n4.data.id        
                    variable = variable.next_node                    
                if (int_act_size >= 125000) and (int_full_size >= 125000):
                    #print "ONE LOOP"
                    #print "esA:=",esA
                    #print "esB:=",esB
                    #print "asA:=",asA
                    #print "asB:=",asB
                    if esA[div_y-1] <= esB[div_y-1]:
                        n = n1.data
                        ofproto = n.ofproto
                        ofp_parser = n.ofproto_parser
                        ofp = ofproto
                        match = n.ofproto_parser.OFPMatch(eth_type=0x800)
                        action = n.ofproto_parser.OFPActionOutput(3)
                        inst = [ofp_parser.OFPInstructionActions(ofp.OFPIT_APPLY_ACTIONS, [action])]
                        mod = n.ofproto_parser.OFPFlowMod(
                                datapath=n, match=match, cookie=0,
                                command=ofproto.OFPFC_ADD, idle_timeout=2, hard_timeout=0,
                                priority=1100,
                                flags=ofproto.OFPFF_SEND_FLOW_REM, instructions=inst)
                        n.send_msg(mod)  
                        if asA[div_y-1] <= asB[div_y-1]:    
                            n = n2.data
                            ofproto = n.ofproto
                            ofp_parser = n.ofproto_parser
                            ofp = ofproto                        
                            match = n.ofproto_parser.OFPMatch(eth_type=0x800)
                            action = n.ofproto_parser.OFPActionOutput(3)
                            inst = [ofp_parser.OFPInstructionActions(ofp.OFPIT_APPLY_ACTIONS, [action])]
                            mod = n.ofproto_parser.OFPFlowMod(
                                    datapath=n, match=match, cookie=0,
                                    command=ofproto.OFPFC_ADD, idle_timeout=2, hard_timeout=0,
                                    priority=1100,
                                    flags=ofproto.OFPFF_SEND_FLOW_REM, instructions=inst)
                            n.send_msg(mod) 
                            asA[div_y-1] = asA[div_y-1]+1
                            #print "asA[int]:=",asA
                        if asA[div_y-1] > asB[div_y-1]: 
                            n = n2.data
                            ofproto = n.ofproto
                            ofp_parser = n.ofproto_parser
                            ofp = ofproto                        
                            match = n.ofproto_parser.OFPMatch(eth_type=0x800)
                            action = n.ofproto_parser.OFPActionOutput(4)
                            inst = [ofp_parser.OFPInstructionActions(ofp.OFPIT_APPLY_ACTIONS, [action])]
                            mod = n.ofproto_parser.OFPFlowMod(
                                    datapath=n, match=match, cookie=0,
                                    command=ofproto.OFPFC_ADD, idle_timeout=2, hard_timeout=0,
                                    priority=1100,
                                    flags=ofproto.OFPFF_SEND_FLOW_REM, instructions=inst)
                            n.send_msg(mod) 
                            asB[div_y-1] = asB[div_y-1]+1
                            #print "asB[int]:=",asB
                        esA[div_y-1] = esA[div_y-1]+1
                        #print "esA[int]:=",esA
                    if esA[div_y-1] > esB[div_y-1]:  
                        n = n1.data
                        ofproto = n.ofproto
                        ofp_parser = n.ofproto_parser
                        ofp = ofproto                        
                        match = n.ofproto_parser.OFPMatch(eth_type=0x800)
                        action = n.ofproto_parser.OFPActionOutput(4)
                        inst = [ofp_parser.OFPInstructionActions(ofp.OFPIT_APPLY_ACTIONS, [action])]
                        mod = n.ofproto_parser.OFPFlowMod(
                                datapath=n, match=match, cookie=0,
                                command=ofproto.OFPFC_ADD, idle_timeout=2, hard_timeout=0,
                                priority=1100,
                                flags=ofproto.OFPFF_SEND_FLOW_REM, instructions=inst)
                        n.send_msg(mod)
                        if div_y%2 == 1:
                            if asA[div_y] <= asB[div_y]:
                                n = n3.data
                                ofproto = n.ofproto
                                ofp_parser = n.ofproto_parser
                                ofp = ofproto                        
                                match = n.ofproto_parser.OFPMatch(eth_type=0x800)
                                action = n.ofproto_parser.OFPActionOutput(3)
                                inst = [ofp_parser.OFPInstructionActions(ofp.OFPIT_APPLY_ACTIONS, [action])]
                                mod = n.ofproto_parser.OFPFlowMod(
                                        datapath=n, match=match, cookie=5,
                                        command=ofproto.OFPFC_ADD, idle_timeout=2, hard_timeout=0,
                                        priority=1100,
                                        flags=ofproto.OFPFF_SEND_FLOW_REM, instructions=inst)
                                n.send_msg(mod)
                                asA[div_y] = asA[div_y]+1
                                #print "asA[int]:=",asA
                            if asA[div_y] > asB[div_y]:     
                                n = n3.data
                                ofproto = n.ofproto
                                ofp_parser = n.ofproto_parser
                                ofp = ofproto                        
                                match = n.ofproto_parser.OFPMatch(eth_type=0x800)
                                action = n.ofproto_parser.OFPActionOutput(4)
                                inst = [ofp_parser.OFPInstructionActions(ofp.OFPIT_APPLY_ACTIONS, [action])]
                                mod = n.ofproto_parser.OFPFlowMod(
                                        datapath=n, match=match, cookie=0,
                                        command=ofproto.OFPFC_ADD, idle_timeout=2, hard_timeout=0,
                                        priority=1100,
                                        flags=ofproto.OFPFF_SEND_FLOW_REM, instructions=inst)
                                n.send_msg(mod)
                                asB[div_y] = asB[div_y] +1
                                #print "asB[int]:=",asB
                        if div_y%2 == 0:
                            if asA[div_y-2] <= asB[div_y-2]:
                                n = n4.data
                                ofproto = n.ofproto
                                ofp_parser = n.ofproto_parser
                                ofp = ofproto                        
                                match = n.ofproto_parser.OFPMatch(eth_type=0x800)
                                action = n.ofproto_parser.OFPActionOutput(3)
                                inst = [ofp_parser.OFPInstructionActions(ofp.OFPIT_APPLY_ACTIONS, [action])]
                                mod = n.ofproto_parser.OFPFlowMod(
                                        datapath=n, match=match, cookie=0,
                                        command=ofproto.OFPFC_ADD, idle_timeout=2, hard_timeout=0,
                                        priority=1100,
                                        flags=ofproto.OFPFF_SEND_FLOW_REM, instructions=inst)
                                n.send_msg(mod)
                                asA[div_y-2] = asA[div_y-2] +1
                                #print "asA[int]:=",asA
                            if asA[div_y-2] > asB[div_y-2]:     
                                n = n4.data
                                ofproto = n.ofproto
                                ofp_parser = n.ofproto_parser
                                ofp = ofproto                        
                                match = n.ofproto_parser.OFPMatch(eth_type=0x800)
                                action = n.ofproto_parser.OFPActionOutput(4)
                                inst = [ofp_parser.OFPInstructionActions(ofp.OFPIT_APPLY_ACTIONS, [action])]
                                mod = n.ofproto_parser.OFPFlowMod(
                                        datapath=n, match=match, cookie=0,
                                        command=ofproto.OFPFC_ADD, idle_timeout=2, hard_timeout=0,
                                        priority=1100,
                                        flags=ofproto.OFPFF_SEND_FLOW_REM, instructions=inst)
                                n.send_msg(mod)
                                asB[div_y-2] = asB[div_y-2] +1
                                #print "asB[int]",asB
                        esB[div_y-1] = esB[div_y-1] + 1
                        #print "esB[int]:=",esB
                        #print "esA[value]:=",esA
                        #print "esB[value]:=",esB
                        #print "asA[value]:=",asA
                        #print "asB[value]:=",asB
                act_size = " "
                full_size = " "
                data_value = " "
                data = " "
                s.close()
            esA = [0,0,0,0,0,0,0,0]
            esB = [0,0,0,0,0,0,0,0]
            asA = [0,0,0,0,0,0,0,0]
            asB = [0,0,0,0,0,0,0,0]                
            time.sleep(10)
        
    def prepareSwitch(self, sw):
        ofproto = sw.ofproto
        ofp_parser = sw.ofproto_parser
        ofp = ofproto

        if sw.id >=1 and sw.id <= 8: 
            action1 = sw.ofproto_parser.OFPActionOutput(3)
            action2 = sw.ofproto_parser.OFPActionOutput(4)
            bucket1 = sw.ofproto_parser.OFPBucket(weight=1, actions=[action1]) # Fail 50% of times
            bucket2 = sw.ofproto_parser.OFPBucket(weight=1, actions=[action2])
            group_id = 1
            group_mod = sw.ofproto_parser.OFPGroupMod(
                    datapath=sw, command=ofproto.OFPGC_ADD,
                    type_=ofproto.OFPGT_SELECT, group_id=group_id,
                    buckets=[bucket1, bucket2])
            sw.send_msg(group_mod)       
            match = sw.ofproto_parser.OFPMatch(in_port=1)           # Set the outport, etc.
            group_action = sw.ofproto_parser.OFPActionGroup(group_id)
            inst = [ofp_parser.OFPInstructionActions(ofp.OFPIT_APPLY_ACTIONS, [group_action])]
            mod = sw.ofproto_parser.OFPFlowMod(
                    datapath=sw, match=match, cookie=0,
                    command=ofproto.OFPFC_ADD, idle_timeout=0, hard_timeout=0,
                    priority=1100,
                    flags=ofproto.OFPFF_SEND_FLOW_REM, instructions=inst)
            sw.send_msg(mod)
            match = sw.ofproto_parser.OFPMatch(in_port=2)
            group_action = sw.ofproto_parser.OFPActionGroup(group_id)
            inst = [ofp_parser.OFPInstructionActions(ofp.OFPIT_APPLY_ACTIONS, [group_action])]
            mod = sw.ofproto_parser.OFPFlowMod(
                    datapath=sw, match=match, cookie=0,
                    command=ofproto.OFPFC_ADD, idle_timeout=0, hard_timeout=0,
                    priority=1100,
                    flags=ofproto.OFPFF_SEND_FLOW_REM, instructions=inst)
            sw.send_msg(mod)    

        if sw.id >=9 and sw.id <= 16:  
            action1 = sw.ofproto_parser.OFPActionOutput(3)
            action2 = sw.ofproto_parser.OFPActionOutput(4)
            bucket1 = sw.ofproto_parser.OFPBucket(weight=1, actions=[action1]) # Fail 50% of times
            bucket2 = sw.ofproto_parser.OFPBucket(weight=1, actions=[action2])
            group_id = 2
            group_mod = sw.ofproto_parser.OFPGroupMod(
                    datapath=sw, command=ofproto.OFPGC_ADD,
                    type_=ofproto.OFPGT_SELECT, group_id=group_id,
                    buckets=[bucket1, bucket2])
            sw.send_msg(group_mod)       
            match = sw.ofproto_parser.OFPMatch(in_port=1)           # Set the outport, etc.
            group_action = sw.ofproto_parser.OFPActionGroup(group_id)
            inst = [ofp_parser.OFPInstructionActions(ofp.OFPIT_APPLY_ACTIONS, [group_action])]
            mod = sw.ofproto_parser.OFPFlowMod(
                    datapath=sw, match=match, cookie=0,
                    command=ofproto.OFPFC_ADD, idle_timeout=0, hard_timeout=0,
                    priority=1100,
                    flags=ofproto.OFPFF_SEND_FLOW_REM, instructions=inst)
            sw.send_msg(mod)
            match = sw.ofproto_parser.OFPMatch(in_port=2)
            group_action = sw.ofproto_parser.OFPActionGroup(group_id)
            inst = [ofp_parser.OFPInstructionActions(ofp.OFPIT_APPLY_ACTIONS, [group_action])]
            mod = sw.ofproto_parser.OFPFlowMod(
                    datapath=sw, match=match, cookie=0,
                    command=ofproto.OFPFC_ADD, idle_timeout=0, hard_timeout=0,
                    priority=1100,
                    flags=ofproto.OFPFF_SEND_FLOW_REM, instructions=inst)
            sw.send_msg(mod)            

        if sw.id >=17 and sw.id <= 20: 
                match = sw.ofproto_parser.OFPMatch(eth_type=0x800, ipv4_dst="10.0.0.1")
                action = sw.ofproto_parser.OFPActionOutput(1)
                inst = [ofp_parser.OFPInstructionActions(ofp.OFPIT_APPLY_ACTIONS, [action])]
                mod = sw.ofproto_parser.OFPFlowMod(
                        datapath=sw, match=match, cookie=0,
                        command=ofproto.OFPFC_ADD, idle_timeout=0, hard_timeout=0,
                        priority=1100,
                        flags=ofproto.OFPFF_SEND_FLOW_REM, instructions=inst)
                sw.send_msg(mod) 
                match = sw.ofproto_parser.OFPMatch(eth_type=0x800, ipv4_dst="10.0.0.2")
                action = sw.ofproto_parser.OFPActionOutput(1)
                inst = [ofp_parser.OFPInstructionActions(ofp.OFPIT_APPLY_ACTIONS, [action])]
                mod = sw.ofproto_parser.OFPFlowMod(
                        datapath=sw, match=match, cookie=0,
                        command=ofproto.OFPFC_ADD, idle_timeout=0, hard_timeout=0,
                        priority=1100,
                        flags=ofproto.OFPFF_SEND_FLOW_REM, instructions=inst)
                sw.send_msg(mod)
                match = sw.ofproto_parser.OFPMatch(eth_type=0x800, ipv4_dst="10.0.0.3")
                action = sw.ofproto_parser.OFPActionOutput(1)
                inst = [ofp_parser.OFPInstructionActions(ofp.OFPIT_APPLY_ACTIONS, [action])]
                mod = sw.ofproto_parser.OFPFlowMod(
                        datapath=sw, match=match, cookie=0,
                        command=ofproto.OFPFC_ADD, idle_timeout=0, hard_timeout=0,
                        priority=1100,
                        flags=ofproto.OFPFF_SEND_FLOW_REM, instructions=inst)
                sw.send_msg(mod)
                match = sw.ofproto_parser.OFPMatch(eth_type=0x800, ipv4_dst="10.0.0.4")
                action = sw.ofproto_parser.OFPActionOutput(1)
                inst = [ofp_parser.OFPInstructionActions(ofp.OFPIT_APPLY_ACTIONS, [action])]
                mod = sw.ofproto_parser.OFPFlowMod(
                        datapath=sw, match=match, cookie=0,
                        command=ofproto.OFPFC_ADD, idle_timeout=0, hard_timeout=0,
                        priority=1100,
                        flags=ofproto.OFPFF_SEND_FLOW_REM, instructions=inst)
                sw.send_msg(mod)
                match = sw.ofproto_parser.OFPMatch(eth_type=0x800, ipv4_dst="10.0.0.5")
                action = sw.ofproto_parser.OFPActionOutput(2)
                inst = [ofp_parser.OFPInstructionActions(ofp.OFPIT_APPLY_ACTIONS, [action])]
                mod = sw.ofproto_parser.OFPFlowMod(
                        datapath=sw, match=match, cookie=0,
                        command=ofproto.OFPFC_ADD, idle_timeout=0, hard_timeout=0,
                        priority=1100,
                        flags=ofproto.OFPFF_SEND_FLOW_REM, instructions=inst)
                sw.send_msg(mod) 
                match = sw.ofproto_parser.OFPMatch(eth_type=0x800, ipv4_dst="10.0.0.6")
                action = sw.ofproto_parser.OFPActionOutput(2)
                inst = [ofp_parser.OFPInstructionActions(ofp.OFPIT_APPLY_ACTIONS, [action])]
                mod = sw.ofproto_parser.OFPFlowMod(
                        datapath=sw, match=match, cookie=0,
                        command=ofproto.OFPFC_ADD, idle_timeout=0, hard_timeout=0,
                        priority=1100,
                        flags=ofproto.OFPFF_SEND_FLOW_REM, instructions=inst)
                sw.send_msg(mod)
                match = sw.ofproto_parser.OFPMatch(eth_type=0x800, ipv4_dst="10.0.0.7")
                action = sw.ofproto_parser.OFPActionOutput(2)
                inst = [ofp_parser.OFPInstructionActions(ofp.OFPIT_APPLY_ACTIONS, [action])]
                mod = sw.ofproto_parser.OFPFlowMod(
                        datapath=sw, match=match, cookie=0,
                        command=ofproto.OFPFC_ADD, idle_timeout=0, hard_timeout=0,
                        priority=1100,
                        flags=ofproto.OFPFF_SEND_FLOW_REM, instructions=inst)
                sw.send_msg(mod)
                match = sw.ofproto_parser.OFPMatch(eth_type=0x800, ipv4_dst="10.0.0.8")
                action = sw.ofproto_parser.OFPActionOutput(2)
                inst = [ofp_parser.OFPInstructionActions(ofp.OFPIT_APPLY_ACTIONS, [action])]
                mod = sw.ofproto_parser.OFPFlowMod(
                        datapath=sw, match=match, cookie=0,
                        command=ofproto.OFPFC_ADD, idle_timeout=0, hard_timeout=0,
                        priority=1100,
                        flags=ofproto.OFPFF_SEND_FLOW_REM, instructions=inst)
                sw.send_msg(mod)
                match = sw.ofproto_parser.OFPMatch(eth_type=0x800, ipv4_dst="10.0.0.9")
                action = sw.ofproto_parser.OFPActionOutput(3)
                inst = [ofp_parser.OFPInstructionActions(ofp.OFPIT_APPLY_ACTIONS, [action])]
                mod = sw.ofproto_parser.OFPFlowMod(
                        datapath=sw, match=match, cookie=0,
                        command=ofproto.OFPFC_ADD, idle_timeout=0, hard_timeout=0,
                        priority=1100,
                        flags=ofproto.OFPFF_SEND_FLOW_REM, instructions=inst)
                sw.send_msg(mod) 
                match = sw.ofproto_parser.OFPMatch(eth_type=0x800, ipv4_dst="10.0.0.10")
                action = sw.ofproto_parser.OFPActionOutput(3)
                inst = [ofp_parser.OFPInstructionActions(ofp.OFPIT_APPLY_ACTIONS, [action])]
                mod = sw.ofproto_parser.OFPFlowMod(
                        datapath=sw, match=match, cookie=0,
                        command=ofproto.OFPFC_ADD, idle_timeout=0, hard_timeout=0,
                        priority=1100,
                        flags=ofproto.OFPFF_SEND_FLOW_REM, instructions=inst)
                sw.send_msg(mod)
                match = sw.ofproto_parser.OFPMatch(eth_type=0x800, ipv4_dst="10.0.0.11")
                action = sw.ofproto_parser.OFPActionOutput(3)
                inst = [ofp_parser.OFPInstructionActions(ofp.OFPIT_APPLY_ACTIONS, [action])]
                mod = sw.ofproto_parser.OFPFlowMod(
                        datapath=sw, match=match, cookie=0,
                        command=ofproto.OFPFC_ADD, idle_timeout=0, hard_timeout=0,
                        priority=1100,
                        flags=ofproto.OFPFF_SEND_FLOW_REM, instructions=inst)
                sw.send_msg(mod)
                match = sw.ofproto_parser.OFPMatch(eth_type=0x800, ipv4_dst="10.0.0.12")
                action = sw.ofproto_parser.OFPActionOutput(3)
                inst = [ofp_parser.OFPInstructionActions(ofp.OFPIT_APPLY_ACTIONS, [action])]
                mod = sw.ofproto_parser.OFPFlowMod(
                        datapath=sw, match=match, cookie=0,
                        command=ofproto.OFPFC_ADD, idle_timeout=0, hard_timeout=0,
                        priority=1100,
                        flags=ofproto.OFPFF_SEND_FLOW_REM, instructions=inst)
                sw.send_msg(mod)
                match = sw.ofproto_parser.OFPMatch(eth_type=0x800, ipv4_dst="10.0.0.13")
                action = sw.ofproto_parser.OFPActionOutput(4)
                inst = [ofp_parser.OFPInstructionActions(ofp.OFPIT_APPLY_ACTIONS, [action])]
                mod = sw.ofproto_parser.OFPFlowMod(
                        datapath=sw, match=match, cookie=0,
                        command=ofproto.OFPFC_ADD, idle_timeout=0, hard_timeout=0,
                        priority=1100,
                        flags=ofproto.OFPFF_SEND_FLOW_REM, instructions=inst)
                sw.send_msg(mod) 
                match = sw.ofproto_parser.OFPMatch(eth_type=0x800, ipv4_dst="10.0.0.14")
                action = sw.ofproto_parser.OFPActionOutput(4)
                inst = [ofp_parser.OFPInstructionActions(ofp.OFPIT_APPLY_ACTIONS, [action])]
                mod = sw.ofproto_parser.OFPFlowMod(
                        datapath=sw, match=match, cookie=0,
                        command=ofproto.OFPFC_ADD, idle_timeout=0, hard_timeout=0,
                        priority=1100,
                        flags=ofproto.OFPFF_SEND_FLOW_REM, instructions=inst)
                sw.send_msg(mod)
                match = sw.ofproto_parser.OFPMatch(eth_type=0x800, ipv4_dst="10.0.0.15")
                action = sw.ofproto_parser.OFPActionOutput(4)
                inst = [ofp_parser.OFPInstructionActions(ofp.OFPIT_APPLY_ACTIONS, [action])]
                mod = sw.ofproto_parser.OFPFlowMod(
                        datapath=sw, match=match, cookie=0,
                        command=ofproto.OFPFC_ADD, idle_timeout=0, hard_timeout=0,
                        priority=1100,
                        flags=ofproto.OFPFF_SEND_FLOW_REM, instructions=inst)
                sw.send_msg(mod)
                match = sw.ofproto_parser.OFPMatch(eth_type=0x800, ipv4_dst="10.0.0.16")
                action = sw.ofproto_parser.OFPActionOutput(4)
                inst = [ofp_parser.OFPInstructionActions(ofp.OFPIT_APPLY_ACTIONS, [action])]
                mod = sw.ofproto_parser.OFPFlowMod(
                        datapath=sw, match=match, cookie=0,
                        command=ofproto.OFPFC_ADD, idle_timeout=0, hard_timeout=0,
                        priority=1100,
                        flags=ofproto.OFPFF_SEND_FLOW_REM, instructions=inst)
                sw.send_msg(mod)                

        if sw.id >=9 and sw.id <= 10: 
                a_var = (sw.id-8)
                match = sw.ofproto_parser.OFPMatch(eth_type=0x800, ipv4_dst="10.0.0.1")
                action = sw.ofproto_parser.OFPActionOutput(a_var)
                inst = [ofp_parser.OFPInstructionActions(ofp.OFPIT_APPLY_ACTIONS, [action])]
                mod = sw.ofproto_parser.OFPFlowMod(
                        datapath=sw, match=match, cookie=0,
                        command=ofproto.OFPFC_ADD, idle_timeout=0, hard_timeout=0,
                        priority=1200,
                        flags=ofproto.OFPFF_SEND_FLOW_REM, instructions=inst)
                sw.send_msg(mod) 
                match = sw.ofproto_parser.OFPMatch(eth_type=0x800, ipv4_dst="10.0.0.2")
                action = sw.ofproto_parser.OFPActionOutput(a_var)
                inst = [ofp_parser.OFPInstructionActions(ofp.OFPIT_APPLY_ACTIONS, [action])]
                mod = sw.ofproto_parser.OFPFlowMod(
                        datapath=sw, match=match, cookie=0,
                        command=ofproto.OFPFC_ADD, idle_timeout=0, hard_timeout=0,
                        priority=1200,
                        flags=ofproto.OFPFF_SEND_FLOW_REM, instructions=inst)
                sw.send_msg(mod)        
                match = sw.ofproto_parser.OFPMatch(eth_type=0x800, ipv4_dst="10.0.0.3")
                action = sw.ofproto_parser.OFPActionOutput(3-a_var)
                inst = [ofp_parser.OFPInstructionActions(ofp.OFPIT_APPLY_ACTIONS, [action])]
                mod = sw.ofproto_parser.OFPFlowMod(
                        datapath=sw, match=match, cookie=0,
                        command=ofproto.OFPFC_ADD, idle_timeout=0, hard_timeout=0,
                        priority=1200,
                        flags=ofproto.OFPFF_SEND_FLOW_REM, instructions=inst)
                sw.send_msg(mod)
                match = sw.ofproto_parser.OFPMatch(eth_type=0x800, ipv4_dst="10.0.0.4")
                action = sw.ofproto_parser.OFPActionOutput(3-a_var)
                inst = [ofp_parser.OFPInstructionActions(ofp.OFPIT_APPLY_ACTIONS, [action])]
                mod = sw.ofproto_parser.OFPFlowMod(
                        datapath=sw, match=match, cookie=0,
                        command=ofproto.OFPFC_ADD, idle_timeout=0, hard_timeout=0,
                        priority=1200,
                        flags=ofproto.OFPFF_SEND_FLOW_REM, instructions=inst)
                sw.send_msg(mod)  
        if sw.id >=11 and sw.id <= 12: 
                a_var = (sw.id-10)                
                match = sw.ofproto_parser.OFPMatch(eth_type=0x800, ipv4_dst="10.0.0.5")
                action = sw.ofproto_parser.OFPActionOutput(a_var)
                inst = [ofp_parser.OFPInstructionActions(ofp.OFPIT_APPLY_ACTIONS, [action])]
                mod = sw.ofproto_parser.OFPFlowMod(
                        datapath=sw, match=match, cookie=0,
                        command=ofproto.OFPFC_ADD, idle_timeout=0, hard_timeout=0,
                        priority=1200,
                        flags=ofproto.OFPFF_SEND_FLOW_REM, instructions=inst)
                sw.send_msg(mod) 
                match = sw.ofproto_parser.OFPMatch(eth_type=0x800, ipv4_dst="10.0.0.6")
                action = sw.ofproto_parser.OFPActionOutput(a_var)
                inst = [ofp_parser.OFPInstructionActions(ofp.OFPIT_APPLY_ACTIONS, [action])]
                mod = sw.ofproto_parser.OFPFlowMod(
                        datapath=sw, match=match, cookie=0,
                        command=ofproto.OFPFC_ADD, idle_timeout=0, hard_timeout=0,
                        priority=1200,
                        flags=ofproto.OFPFF_SEND_FLOW_REM, instructions=inst)
                sw.send_msg(mod)
                match = sw.ofproto_parser.OFPMatch(eth_type=0x800, ipv4_dst="10.0.0.7")
                action = sw.ofproto_parser.OFPActionOutput(3-a_var)
                inst = [ofp_parser.OFPInstructionActions(ofp.OFPIT_APPLY_ACTIONS, [action])]
                mod = sw.ofproto_parser.OFPFlowMod(
                        datapath=sw, match=match, cookie=0,
                        command=ofproto.OFPFC_ADD, idle_timeout=0, hard_timeout=0,
                        priority=1200,
                        flags=ofproto.OFPFF_SEND_FLOW_REM, instructions=inst)
                sw.send_msg(mod)
                match = sw.ofproto_parser.OFPMatch(eth_type=0x800, ipv4_dst="10.0.0.8")
                action = sw.ofproto_parser.OFPActionOutput(3-a_var)
                inst = [ofp_parser.OFPInstructionActions(ofp.OFPIT_APPLY_ACTIONS, [action])]
                mod = sw.ofproto_parser.OFPFlowMod(
                        datapath=sw, match=match, cookie=0,
                        command=ofproto.OFPFC_ADD, idle_timeout=0, hard_timeout=0,
                        priority=1200,
                        flags=ofproto.OFPFF_SEND_FLOW_REM, instructions=inst)
                sw.send_msg(mod)
        if sw.id >=13 and sw.id <= 14: 
                a_var = (sw.id-12)                 
                match = sw.ofproto_parser.OFPMatch(eth_type=0x800, ipv4_dst="10.0.0.9")
                action = sw.ofproto_parser.OFPActionOutput(a_var)
                inst = [ofp_parser.OFPInstructionActions(ofp.OFPIT_APPLY_ACTIONS, [action])]
                mod = sw.ofproto_parser.OFPFlowMod(
                        datapath=sw, match=match, cookie=0,
                        command=ofproto.OFPFC_ADD, idle_timeout=0, hard_timeout=0,
                        priority=1200,
                        flags=ofproto.OFPFF_SEND_FLOW_REM, instructions=inst)
                sw.send_msg(mod) 
                match = sw.ofproto_parser.OFPMatch(eth_type=0x800, ipv4_dst="10.0.0.10")
                action = sw.ofproto_parser.OFPActionOutput(a_var)
                inst = [ofp_parser.OFPInstructionActions(ofp.OFPIT_APPLY_ACTIONS, [action])]
                mod = sw.ofproto_parser.OFPFlowMod(
                        datapath=sw, match=match, cookie=0,
                        command=ofproto.OFPFC_ADD, idle_timeout=0, hard_timeout=0,
                        priority=1200,
                        flags=ofproto.OFPFF_SEND_FLOW_REM, instructions=inst)
                sw.send_msg(mod)
                match = sw.ofproto_parser.OFPMatch(eth_type=0x800, ipv4_dst="10.0.0.11")
                action = sw.ofproto_parser.OFPActionOutput(3-a_var)
                inst = [ofp_parser.OFPInstructionActions(ofp.OFPIT_APPLY_ACTIONS, [action])]
                mod = sw.ofproto_parser.OFPFlowMod(
                        datapath=sw, match=match, cookie=0,
                        command=ofproto.OFPFC_ADD, idle_timeout=0, hard_timeout=0,
                        priority=1200,
                        flags=ofproto.OFPFF_SEND_FLOW_REM, instructions=inst)
                sw.send_msg(mod)
                match = sw.ofproto_parser.OFPMatch(eth_type=0x800, ipv4_dst="10.0.0.12")
                action = sw.ofproto_parser.OFPActionOutput(3-a_var)
                inst = [ofp_parser.OFPInstructionActions(ofp.OFPIT_APPLY_ACTIONS, [action])]
                mod = sw.ofproto_parser.OFPFlowMod(
                        datapath=sw, match=match, cookie=0,
                        command=ofproto.OFPFC_ADD, idle_timeout=0, hard_timeout=0,
                        priority=1200,
                        flags=ofproto.OFPFF_SEND_FLOW_REM, instructions=inst)
                sw.send_msg(mod)
        if sw.id >=15 and sw.id <= 16: 
                a_var = (sw.id-14)                 
                match = sw.ofproto_parser.OFPMatch(eth_type=0x800, ipv4_dst="10.0.0.13")
                action = sw.ofproto_parser.OFPActionOutput(a_var)
                inst = [ofp_parser.OFPInstructionActions(ofp.OFPIT_APPLY_ACTIONS, [action])]
                mod = sw.ofproto_parser.OFPFlowMod(
                        datapath=sw, match=match, cookie=0,
                        command=ofproto.OFPFC_ADD, idle_timeout=0, hard_timeout=0,
                        priority=1200,
                        flags=ofproto.OFPFF_SEND_FLOW_REM, instructions=inst)
                sw.send_msg(mod) 
                match = sw.ofproto_parser.OFPMatch(eth_type=0x800, ipv4_dst="10.0.0.14")
                action = sw.ofproto_parser.OFPActionOutput(a_var)
                inst = [ofp_parser.OFPInstructionActions(ofp.OFPIT_APPLY_ACTIONS, [action])]
                mod = sw.ofproto_parser.OFPFlowMod(
                        datapath=sw, match=match, cookie=0,
                        command=ofproto.OFPFC_ADD, idle_timeout=0, hard_timeout=0,
                        priority=1200,
                        flags=ofproto.OFPFF_SEND_FLOW_REM, instructions=inst)
                sw.send_msg(mod)
                match = sw.ofproto_parser.OFPMatch(eth_type=0x800, ipv4_dst="10.0.0.15")
                action = sw.ofproto_parser.OFPActionOutput(3-a_var)
                inst = [ofp_parser.OFPInstructionActions(ofp.OFPIT_APPLY_ACTIONS, [action])]
                mod = sw.ofproto_parser.OFPFlowMod(
                        datapath=sw, match=match, cookie=0,
                        command=ofproto.OFPFC_ADD, idle_timeout=0, hard_timeout=0,
                        priority=1200,
                        flags=ofproto.OFPFF_SEND_FLOW_REM, instructions=inst)
                sw.send_msg(mod)
                match = sw.ofproto_parser.OFPMatch(eth_type=0x800, ipv4_dst="10.0.0.16")
                action = sw.ofproto_parser.OFPActionOutput(3-a_var)
                inst = [ofp_parser.OFPInstructionActions(ofp.OFPIT_APPLY_ACTIONS, [action])]
                mod = sw.ofproto_parser.OFPFlowMod(
                        datapath=sw, match=match, cookie=0,
                        command=ofproto.OFPFC_ADD, idle_timeout=0, hard_timeout=0,
                        priority=1200,
                        flags=ofproto.OFPFF_SEND_FLOW_REM, instructions=inst)
                sw.send_msg(mod) 

        if(sw.id == 1):
                match = sw.ofproto_parser.OFPMatch(eth_type=0x800, ipv4_dst="10.0.0.1")
                action = sw.ofproto_parser.OFPActionOutput(1)
                inst = [ofp_parser.OFPInstructionActions(ofp.OFPIT_APPLY_ACTIONS, [action])]
                mod = sw.ofproto_parser.OFPFlowMod(
                        datapath=sw, match=match, cookie=0,
                        command=ofproto.OFPFC_ADD, idle_timeout=0, hard_timeout=0,
                        priority=1200,
                        flags=ofproto.OFPFF_SEND_FLOW_REM, instructions=inst)
                sw.send_msg(mod) 
                match = sw.ofproto_parser.OFPMatch(eth_type=0x800, ipv4_dst="10.0.0.2")
                action = sw.ofproto_parser.OFPActionOutput(2)
                inst = [ofp_parser.OFPInstructionActions(ofp.OFPIT_APPLY_ACTIONS, [action])]
                mod = sw.ofproto_parser.OFPFlowMod(
                        datapath=sw, match=match, cookie=0,
                        command=ofproto.OFPFC_ADD, idle_timeout=0, hard_timeout=0,
                        priority=1200,
                        flags=ofproto.OFPFF_SEND_FLOW_REM, instructions=inst)
                sw.send_msg(mod)
        if(sw.id == 2):
                match = sw.ofproto_parser.OFPMatch(eth_type=0x800, ipv4_dst="10.0.0.3")
                action = sw.ofproto_parser.OFPActionOutput(1)
                inst = [ofp_parser.OFPInstructionActions(ofp.OFPIT_APPLY_ACTIONS, [action])]
                mod = sw.ofproto_parser.OFPFlowMod(
                        datapath=sw, match=match, cookie=0,
                        command=ofproto.OFPFC_ADD, idle_timeout=0, hard_timeout=0,
                        priority=1200,
                        flags=ofproto.OFPFF_SEND_FLOW_REM, instructions=inst)
                sw.send_msg(mod)
                match = sw.ofproto_parser.OFPMatch(eth_type=0x800, ipv4_dst="10.0.0.4")
                action = sw.ofproto_parser.OFPActionOutput(2)
                inst = [ofp_parser.OFPInstructionActions(ofp.OFPIT_APPLY_ACTIONS, [action])]
                mod = sw.ofproto_parser.OFPFlowMod(
                        datapath=sw, match=match, cookie=0,
                        command=ofproto.OFPFC_ADD, idle_timeout=0, hard_timeout=0,
                        priority=1200,
                        flags=ofproto.OFPFF_SEND_FLOW_REM, instructions=inst)
                sw.send_msg(mod)  
        if(sw.id == 3):                
                match = sw.ofproto_parser.OFPMatch(eth_type=0x800, ipv4_dst="10.0.0.5")
                action = sw.ofproto_parser.OFPActionOutput(1)
                inst = [ofp_parser.OFPInstructionActions(ofp.OFPIT_APPLY_ACTIONS, [action])]
                mod = sw.ofproto_parser.OFPFlowMod(
                        datapath=sw, match=match, cookie=0,
                        command=ofproto.OFPFC_ADD, idle_timeout=0, hard_timeout=0,
                        priority=1200,
                        flags=ofproto.OFPFF_SEND_FLOW_REM, instructions=inst)
                sw.send_msg(mod) 
                match = sw.ofproto_parser.OFPMatch(eth_type=0x800, ipv4_dst="10.0.0.6")
                action = sw.ofproto_parser.OFPActionOutput(2)
                inst = [ofp_parser.OFPInstructionActions(ofp.OFPIT_APPLY_ACTIONS, [action])]
                mod = sw.ofproto_parser.OFPFlowMod(
                        datapath=sw, match=match, cookie=0,
                        command=ofproto.OFPFC_ADD, idle_timeout=0, hard_timeout=0,
                        priority=1200,
                        flags=ofproto.OFPFF_SEND_FLOW_REM, instructions=inst)
                sw.send_msg(mod)
        if(sw.id == 4):        
                match = sw.ofproto_parser.OFPMatch(eth_type=0x800, ipv4_dst="10.0.0.7")
                action = sw.ofproto_parser.OFPActionOutput(1)
                inst = [ofp_parser.OFPInstructionActions(ofp.OFPIT_APPLY_ACTIONS, [action])]
                mod = sw.ofproto_parser.OFPFlowMod(
                        datapath=sw, match=match, cookie=0,
                        command=ofproto.OFPFC_ADD, idle_timeout=0, hard_timeout=0,
                        priority=1200,
                        flags=ofproto.OFPFF_SEND_FLOW_REM, instructions=inst)
                sw.send_msg(mod)
                match = sw.ofproto_parser.OFPMatch(eth_type=0x800, ipv4_dst="10.0.0.8")
                action = sw.ofproto_parser.OFPActionOutput(2)
                inst = [ofp_parser.OFPInstructionActions(ofp.OFPIT_APPLY_ACTIONS, [action])]
                mod = sw.ofproto_parser.OFPFlowMod(
                        datapath=sw, match=match, cookie=0,
                        command=ofproto.OFPFC_ADD, idle_timeout=0, hard_timeout=0,
                        priority=1200,
                        flags=ofproto.OFPFF_SEND_FLOW_REM, instructions=inst)
                sw.send_msg(mod)
        if(sw.id == 5):                 
                match = sw.ofproto_parser.OFPMatch(eth_type=0x800, ipv4_dst="10.0.0.9")
                action = sw.ofproto_parser.OFPActionOutput(1)
                inst = [ofp_parser.OFPInstructionActions(ofp.OFPIT_APPLY_ACTIONS, [action])]
                mod = sw.ofproto_parser.OFPFlowMod(
                        datapath=sw, match=match, cookie=0,
                        command=ofproto.OFPFC_ADD, idle_timeout=0, hard_timeout=0,
                        priority=1200,
                        flags=ofproto.OFPFF_SEND_FLOW_REM, instructions=inst)
                sw.send_msg(mod) 
                match = sw.ofproto_parser.OFPMatch(eth_type=0x800, ipv4_dst="10.0.0.10")
                action = sw.ofproto_parser.OFPActionOutput(2)
                inst = [ofp_parser.OFPInstructionActions(ofp.OFPIT_APPLY_ACTIONS, [action])]
                mod = sw.ofproto_parser.OFPFlowMod(
                        datapath=sw, match=match, cookie=0,
                        command=ofproto.OFPFC_ADD, idle_timeout=0, hard_timeout=0,
                        priority=1200,
                        flags=ofproto.OFPFF_SEND_FLOW_REM, instructions=inst)
                sw.send_msg(mod)
        if(sw.id == 6):                
                match = sw.ofproto_parser.OFPMatch(eth_type=0x800, ipv4_dst="10.0.0.11")
                action = sw.ofproto_parser.OFPActionOutput(1)
                inst = [ofp_parser.OFPInstructionActions(ofp.OFPIT_APPLY_ACTIONS, [action])]
                mod = sw.ofproto_parser.OFPFlowMod(
                        datapath=sw, match=match, cookie=0,
                        command=ofproto.OFPFC_ADD, idle_timeout=0, hard_timeout=0,
                        priority=1200,
                        flags=ofproto.OFPFF_SEND_FLOW_REM, instructions=inst)
                sw.send_msg(mod)
                match = sw.ofproto_parser.OFPMatch(eth_type=0x800, ipv4_dst="10.0.0.12")
                action = sw.ofproto_parser.OFPActionOutput(2)
                inst = [ofp_parser.OFPInstructionActions(ofp.OFPIT_APPLY_ACTIONS, [action])]
                mod = sw.ofproto_parser.OFPFlowMod(
                        datapath=sw, match=match, cookie=0,
                        command=ofproto.OFPFC_ADD, idle_timeout=0, hard_timeout=0,
                        priority=1200,
                        flags=ofproto.OFPFF_SEND_FLOW_REM, instructions=inst)
                sw.send_msg(mod)
        if(sw.id == 7):                 
                match = sw.ofproto_parser.OFPMatch(eth_type=0x800, ipv4_dst="10.0.0.13")
                action = sw.ofproto_parser.OFPActionOutput(1)
                inst = [ofp_parser.OFPInstructionActions(ofp.OFPIT_APPLY_ACTIONS, [action])]
                mod = sw.ofproto_parser.OFPFlowMod(
                        datapath=sw, match=match, cookie=0,
                        command=ofproto.OFPFC_ADD, idle_timeout=0, hard_timeout=0,
                        priority=1200,
                        flags=ofproto.OFPFF_SEND_FLOW_REM, instructions=inst)
                sw.send_msg(mod) 
                match = sw.ofproto_parser.OFPMatch(eth_type=0x800, ipv4_dst="10.0.0.14")
                action = sw.ofproto_parser.OFPActionOutput(2)
                inst = [ofp_parser.OFPInstructionActions(ofp.OFPIT_APPLY_ACTIONS, [action])]
                mod = sw.ofproto_parser.OFPFlowMod(
                        datapath=sw, match=match, cookie=0,
                        command=ofproto.OFPFC_ADD, idle_timeout=0, hard_timeout=0,
                        priority=1200,
                        flags=ofproto.OFPFF_SEND_FLOW_REM, instructions=inst)
                sw.send_msg(mod)
        if(sw.id == 8):        
                match = sw.ofproto_parser.OFPMatch(eth_type=0x800, ipv4_dst="10.0.0.15")
                action = sw.ofproto_parser.OFPActionOutput(1)
                inst = [ofp_parser.OFPInstructionActions(ofp.OFPIT_APPLY_ACTIONS, [action])]
                mod = sw.ofproto_parser.OFPFlowMod(
                        datapath=sw, match=match, cookie=0,
                        command=ofproto.OFPFC_ADD, idle_timeout=0, hard_timeout=0,
                        priority=1200,
                        flags=ofproto.OFPFF_SEND_FLOW_REM, instructions=inst)
                sw.send_msg(mod)
                match = sw.ofproto_parser.OFPMatch(eth_type=0x800, ipv4_dst="10.0.0.16")
                action = sw.ofproto_parser.OFPActionOutput(2)
                inst = [ofp_parser.OFPInstructionActions(ofp.OFPIT_APPLY_ACTIONS, [action])]
                mod = sw.ofproto_parser.OFPFlowMod(
                        datapath=sw, match=match, cookie=0,
                        command=ofproto.OFPFC_ADD, idle_timeout=0, hard_timeout=0,
                        priority=1200,
                        flags=ofproto.OFPFF_SEND_FLOW_REM, instructions=inst)
                sw.send_msg(mod)                

    
    # the rest of the code
    @set_ev_cls(dpset.EventDP)
    def switchStatus(self, ev):
        print("Switch %s: %s!" %
              (ev.dp.id, "connected" if ev.enter else "disconnected"))
        
        mylist.add(ev.dp)
        self.prepareSwitch(ev.dp) 
             

        

    