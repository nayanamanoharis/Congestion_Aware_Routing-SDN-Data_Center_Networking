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


class Controller(app_manager.RyuApp):
    def __init__(self):
        super(Controller, self).__init__()
        t = threading.Thread(target=self.Client)
        t.start() 
    
    #Referred from the TCP communication Python tutorial 
    def Client(self):
        for y in range(1,17):
            TCP_IP = '20.0.0.'+str(y)
            print "Ip address:", TCP_IP
            TCP_PORT = 5000
            BUFFER_SIZE = 1024
            MESSAGE = "Nayana Client message"            
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            print "Sending POST"
            
            while 1:
                try:
                    s.connect((TCP_IP, TCP_PORT))
                    print "connect successful"
                    break
                except:
                    pass
            print "Ip address:", TCP_IP
            print "port:", TCP_PORT
            s.send(MESSAGE)
            data = s.recv(BUFFER_SIZE)
            s.close()
            print "Receiving:", data 
        
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
        
        self.prepareSwitch(ev.dp)         

        


            
    