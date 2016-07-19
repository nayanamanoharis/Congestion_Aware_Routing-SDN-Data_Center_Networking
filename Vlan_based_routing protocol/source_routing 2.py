from ryu.base import app_manager
from ryu.controller import ofp_event, dpset
from ryu.controller.handler import MAIN_DISPATCHER
from ryu.controller.handler import set_ev_cls
from ryu.lib.ip import ipv4_to_bin

class Controller(app_manager.RyuApp):
    def prepareSwitch(self, sw):
        ofproto = sw.ofproto
        
       
        switch1_eth1_vlan = [1,16,2,3,18,19,32,48,33,49,4,5,6,7,8,9,10,11,12,13,14,15,20,21,22,23,24,25,26,27,28,29,30,31,64,65,80,81,96,97,112,113,128,129,144,145,160,161,176,177,192,193,208,209,224,225,240,241]
        switch1_eth1_outport = [2,1,3,3,3,3,1,1,2,2,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2]
        switch1_eth1_inport = [1,2,1,1,2,2,3,3,3,3,1,1,1,1,1,1,1,1,1,1,1,1,2,2,2,2,2,2,2,2,2,2,2,2,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3]
        switch2_eth1_vlan = [35,50,2,3,18,19,32,48,33,49,36,37,38,39,40,41,42,43,44,45,46,47,52,53,54,55,56,57,58,59,60,61,62,63,66,67,82,83,98,99,114,115,130,131,146,147,162,163,178,179,194,195,210,211,226,227,242,243]
        switch2_eth1_outport = [2,1,1,2,1,2,4,4,4,4,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2]
        switch2_eth1_inport = [1,2,4,4,4,4,1,2,1,2,1,1,1,1,1,1,1,1,1,1,1,1,2,2,2,2,2,2,2,2,2,2,2,2,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4]
        switch3_eth1_vlan=[69,84,70,86,71,87,100,116,101,117,4,5,20,21,36,37,52,53,64,65,66,67,72,73,74,75,76,77,78,79,80,81,82,83,88,89,90,91,92,93,94,95,164,165,180,181,196,197,212,213,228,229,244,245,132,133,148,149]
        switch3_eth1_outport = [2,1,3,3,3,3,1,1,2,2,1,2,1,2,1,2,1,2,3,3,3,3,4,4,4,4,4,4,4,4,3,3,3,3,4,4,4,4,4,4,4,4,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2]
        switch3_eth1_inport = [1,2,1,2,1,2,3,3,3,3,3,3,3,3,4,4,4,4,1,1,1,1,1,1,1,1,1,1,1,1,2,2,2,2,2,2,2,2,2,2,2,2,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3]
        switch4_eth1_vlan = [103,118,70,86,71,87,100,116,101,117,6,7,22,23,36,37,38,39,52,53,54,55,38,39,54,55,96,97,98,99,104,105,106,107,108,109,110,111,112,113,114,115,120,121,122,123,124,125,126,127,166,167,182,183,198,199,214,215,230,231,246,247,134,135,150,151]
        switch4_eth1_outport = [2,1,1,1,2,2,4,4,4,4,1,2,1,2,2,2,1,1,2,2,1,1,1,2,1,2,4,4,4,4,3,3,3,3,3,3,3,3,4,4,4,4,3,3,3,3,3,3,3,3,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2]
        switch4_eth1_inport = [1,2,4,4,4,4,1,2,1,2,4,4,4,4,3,3,3,3,3,3,3,3,3,3,3,3,1,1,1,1,1,1,1,1,1,1,1,1,2,2,2,2,2,2,2,2,2,2,2,2,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4]
        switch5_eth1_vlan = [137,152,138,154,139,155,168,169,184,185,8,9,24,25,40,41,56,57,72,73,88,89,104,105,120,121,128,129,130,131,132,133,134,135,140,141,142,143,144,145,146,147,148,149,150,151,156,157,158,159,200,201,216,217,232,233,248,249]
        switch5_eth1_outport = [2,1,4,4,4,4,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,3,3,3,3,3,3,3,3,4,4,4,4,3,3,3,3,3,3,3,3,4,4,4,4,1,2,1,2,1,2,1,2]
        switch5_eth1_inport = [1,2,1,2,1,2,4,4,4,4,3,3,3,3,4,4,4,4,4,4,4,4,4,4,4,4,1,1,1,1,1,1,1,1,1,1,1,1,2,2,2,2,2,2,2,2,2,2,2,2,3,3,3,3,3,3,3,3]
        switch6_eth1_vlan = [171,186,138,154,139,155,168,169,184,185,10,11,26,27,42,43,58,59,74,75,90,91,106,107,122,123,160,161,162,163,164,165,166,167,172,173,174,175,176,177,178,179,180,181,182,183,188,189,190,191,202,203,218,219,234,235,250,251]
        switch6_eth1_outport = [2,1,1,1,2,2,3,3,3,3,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,4,4,4,4,4,4,4,4,3,3,3,3,4,4,4,4,4,4,4,4,3,3,3,3,1,2,1,2,1,2,1,2]
        switch6_eth1_inport = [1,2,3,3,3,3,1,1,2,2,4,4,4,4,3,3,3,3,3,3,3,3,3,3,3,3,1,1,1,1,1,1,1,1,1,1,1,1,2,2,2,2,2,2,2,2,2,2,2,2,4,4,4,4,4,4,4,4]
        switch7_eth1_vlan = [205,220,206,207,222,223,236,237,252,253,12,13,28,29,44,45,60,61,76,77,92,93,108,109,124,125,140,141,156,157,172,173,188,189,192,193,194,195,196,197,198,199,200,201,202,203,208,209,210,211,212,213,214,215,216,217,218,219]
        switch7_eth1_outport = [2,1,4,4,4,4,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3]
        switch7_eth1_inport = [1,2,1,1,2,2,4,4,4,4,3,3,3,3,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,1,1,1,1,1,1,1,1,1,1,1,1,2,2,2,2,2,2,2,2,2,2,2,2]
        switch8_eth1_vlan = [239,254,206,207,222,223,236,237,252,253,14,15,30,31,46,47,62,63,78,79,94,95,110,111,126,127,142,143,158,159,174,175,190,191,224,225,226,227,228,229,230,231,232,233,234,235,240,241,242,243,244,245,246,247,248,249,250,251]
        switch8_eth1_outport = [2,1,1,2,1,2,3,3,3,3,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4]
        switch8_eth1_inport = [1,2,3,3,3,3,1,1,2,2,4,4,4,4,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,1,1,1,1,1,1,1,1,1,1,1,1,2,2,2,2,2,2,2,2,2,2,2,2]
        AGswitch0_eth1_vlan = [2,3,18,19,32,48,33,49,4,5,6,7,12,13,14,15,20,21,22,23,28,29,30,31,8,9,10,11,24,25,26,27,64,65,66,67,80,81,82,83,96,97,98,99,112,113,114,115,128,129,130,131,144,145,146,147,160,161,162,163,176,177,178,179,192,193,194,195,208,209,210,211,224,225,226,227,240,241,242,243]
        AGswitch0_eth1_outport = [2,2,2,2,1,1,1,1,3,3,3,3,4,4,4,4,3,3,3,3,4,4,4,4,4,4,4,4,4,4,4,4,1,1,2,2,1,1,2,2,1,1,2,2,1,1,2,2,1,1,2,2,1,1,2,2,1,1,2,2,1,1,2,2,1,1,2,2,1,1,2,2,1,1,2,2,1,1,2,2]
        AGswitch0_eth1_inport = [1,1,1,1,2,2,2,2,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3]
        AGswitch1_eth1_vlan = [36,37,38,39,40,41,42,43,44,45,46,47,52,53,54,55,56,57,58,59,60,61,62,63]
        AGswitch1_eth1_outport =[3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3] 
        AGswitch1_eth1_inport = [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
        AGswitch2_eth1_vlan = [70,86,71,87,100,116,101,117,4,5,6,7,20,21,22,23,64,65,66,67,80,81,82,83,96,97,98,99,112,113,114,115,132,133,134,135,148,149,150,151,164,165,166,167,180,181,182,183,196,197,198,199,212,213,214,215,228,229,230,231,244,245,246,247]
        AGswitch2_eth1_outport = [2,2,2,2,1,1,1,1,1,1,2,2,1,1,2,2,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,1,1,2,2,1,1,2,2,1,1,2,2,1,1,2,2,1,1,2,2,1,1,2,2,1,1,2,2,1,1,2,2]
        AGswitch2_eth1_inport = [1,1,1,1,2,2,2,2,3,3,3,3,3,3,3,3,1,1,1,1,1,1,1,1,2,2,2,2,2,2,2,2,4,4,4,4,4,4,4,4,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3]  
        AGswitch3_eth1_vlan = [36,37,38,39,52,53,54,55,72,73,74,75,76,77,78,79,88,89,90,91,92,93,94,95,104,105,106,107,108,109,110,111,120,121,122,123,124,125,126,127]
        AGswitch3_eth1_outport =[2,2,1,1,2,2,1,1,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4] 
        AGswitch3_eth1_inport = [3,3,3,3,3,3,3,3,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
        AGswitch4_eth1_vlan = [8,9,10,11,24,25,26,27,128,129,130,131,132,133,134,135,144,145,146,147,148,149,150,151,160,161,162,163,164,165,166,167,176,177,178,179,180,181,182,183,200,201,202,203,216,217,218,219,232,233,234,235,248,249,250,251]
        AGswitch4_eth1_outport =[1,1,2,2,1,1,2,2,3,3,3,3,4,4,4,4,3,3,3,3,4,4,4,4,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,1,1,2,2,1,1,2,2,1,1,2,2,1,1,2,2] 
        AGswitch4_eth1_inport = [4,4,4,4,4,4,4,4,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3]
        AGswitch5_eth1_vlan = [138,154,139,155,168,169,184,185,40,41,42,43,56,57,58,59,72,73,74,75,88,89,90,91,104,105,106,107,120,121,122,123,140,141,142,143,156,157,158,159,172,173,174,175,188,189,190,191]
        AGswitch5_eth1_outport = [1,1,1,1,2,2,2,2,2,2,1,1,2,2,1,1,2,2,1,1,2,2,1,1,2,2,1,1,2,2,1,1,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4]
        AGswitch5_eth1_inport = [2,2,2,2,1,1,1,1,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,4,4,4,4,4,4,4,4,2,2,2,2,2,2,2,2,1,1,1,1,1,1,1,1]
        AGswitch6_eth1_vlan = [12,13,14,15,28,29,30,31,192,193,194,195,196,197,198,199,200,201,202,203,208,209,210,211,212,213,214,215,216,217,218,219,224,225,226,227,228,229,230,231,232,233,234,235,240,241,242,243,244,245,246,247,248,249,250,251]
        AGswitch6_eth1_outport =[1,1,2,2,1,1,2,2,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3] 
        AGswitch6_eth1_inport = [4,4,4,4,4,4,4,4,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2]
        AGswitch7_eth1_vlan = [206,207,222,223,236,237,252,253,44,45,46,47,60,61,62,63,76,77,78,79,92,93,94,95,108,109,110,111,124,125,126,127,140,141,142,143,156,157,158,159,172,173,174,175,188,189,190,191]
        AGswitch7_eth1_outport = [1,1,1,1,2,2,2,2,2,2,1,1,2,2,1,1,2,2,1,1,2,2,1,1,2,2,1,1,2,2,1,1,2,2,1,1,2,2,1,1,2,2,1,1,2,2,1,1]
        AGswitch7_eth1_inport = [2,2,2,2,1,1,1,1,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4]

        COswitch0_eth1_vlan = [4,5,6,7,20,21,22,23,64,65,66,67,80,81,82,83,96,97,98,99,112,113,114,115,128,129,130,131,144,145,146,147,160,161,162,163,164,165,166,167,176,177,178,179,180,181,182,183,192,193,194,195,196,197,198,199,200,201,202,203,208,209,210,211,212,213,214,215,216,217,218,219,224,225,226,227,228,229,230,231,232,233,234,235,240,241,242,243,244,245,246,247,248,249,250,251]
        COswitch0_eth1_outport =[2,2,2,2,2,2,2,2,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,2,2,2,2,1,1,1,1,2,2,2,2,1,1,1,1,2,2,2,2,3,3,3,3,1,1,1,1,2,2,2,2,3,3,3,3,1,1,1,1,2,2,2,2,3,3,3,3,1,1,1,1,2,2,2,2,3,3,3,3] 
        COswitch0_eth1_inport = [1,1,1,1,1,1,1,1,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4]  
        COswitch1_eth1_vlan = [8,9,10,11,12,13,14,15,24,25,26,27,28,29,30,31,132,133,134,135,148,149,150,151]
        COswitch1_eth1_outport =[3,3,3,3,4,4,4,4,3,3,3,3,4,4,4,4,2,2,2,2,2,2,2,2] 
        COswitch1_eth1_inport = [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,3,3,3,3,3,3,3,3]    
        COswitch2_eth1_vlan = [36,37,38,39,40,41,42,43,44,45,46,47,52,53,54,55,56,57,58,59,60,61,62,63,72,73,74,75,76,77,78,79,88,89,90,91,92,93,94,95]
        COswitch2_eth1_outport =[2,2,2,2,3,3,3,3,4,4,4,4,2,2,2,2,3,3,3,3,4,4,4,4,3,3,3,3,4,4,4,4,3,3,3,3,4,4,4,4] 
        COswitch2_eth1_inport = [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2] 
        COswitch3_eth1_vlan = [104,105,106,107,108,109,110,111,120,121,122,123,124,125,126,127,140,141,142,143,156,157,158,159,172,173,174,175,188,189,190,191]
        COswitch3_eth1_outport =[3,3,3,3,4,4,4,4,3,3,3,3,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4] 
        COswitch3_eth1_inport =[2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3]       

        
        i=0;
        j=0;
        for j in range(3):
            if sw.id == 1: 
                for i in range(58): 
                    match = sw.ofproto_parser.OFPMatch(in_port=switch1_eth1_inport[i], dl_type=0x806,dl_vlan = switch1_eth1_vlan[i])
                    action = sw.ofproto_parser.OFPActionOutput(switch1_eth1_outport[i])
                    mod = sw.ofproto_parser.OFPFlowMod(
                        datapath=sw, match=match, cookie=0,
                        command=ofproto.OFPFC_ADD, idle_timeout=0, hard_timeout=0,
                        priority=1000,
                        flags=ofproto.OFPFF_SEND_FLOW_REM, actions=[action])
                    sw.send_msg(mod)
                    match = sw.ofproto_parser.OFPMatch(in_port=switch1_eth1_inport[i], dl_type=0x800,dl_vlan= switch1_eth1_vlan[i])
                    action = sw.ofproto_parser.OFPActionOutput(switch1_eth1_outport[i])
                    mod = sw.ofproto_parser.OFPFlowMod(
                        datapath=sw, match=match, cookie=0,
                        command=ofproto.OFPFC_ADD, idle_timeout=0, hard_timeout=0,
                        priority=1000,
                        flags=ofproto.OFPFF_SEND_FLOW_REM, actions=[action])
                    sw.send_msg(mod)
            if sw.id == 2:
                for i in range(58):
                    match = sw.ofproto_parser.OFPMatch(in_port=switch2_eth1_inport[i], dl_type=0x806,dl_vlan=switch2_eth1_vlan[i])
                    action = sw.ofproto_parser.OFPActionOutput(switch2_eth1_outport[i])
                    mod = sw.ofproto_parser.OFPFlowMod(
                        datapath=sw, match=match, cookie=0,
                        command=ofproto.OFPFC_ADD, idle_timeout=0, hard_timeout=0,
                        priority=1000,
                        flags=ofproto.OFPFF_SEND_FLOW_REM, actions=[action])
                    sw.send_msg(mod)
                    match = sw.ofproto_parser.OFPMatch(in_port=switch2_eth1_inport[i], dl_type=0x800,dl_vlan=switch2_eth1_vlan[i])
                    action = sw.ofproto_parser.OFPActionOutput(switch2_eth1_outport[i])
                    mod = sw.ofproto_parser.OFPFlowMod(
                        datapath=sw, match=match, cookie=0,
                        command=ofproto.OFPFC_ADD, idle_timeout=0, hard_timeout=0,
                        priority=1000,
                        flags=ofproto.OFPFF_SEND_FLOW_REM, actions=[action])
                    sw.send_msg(mod)
            if sw.id == 3:
                for i in range(58):
                    match = sw.ofproto_parser.OFPMatch(in_port=switch3_eth1_inport[i], dl_type=0x806,dl_vlan=switch3_eth1_vlan[i])
                    action = sw.ofproto_parser.OFPActionOutput(switch3_eth1_outport[i])
                    mod = sw.ofproto_parser.OFPFlowMod(
                        datapath=sw, match=match, cookie=0,
                        command=ofproto.OFPFC_ADD, idle_timeout=0, hard_timeout=0,
                        priority=1000,
                        flags=ofproto.OFPFF_SEND_FLOW_REM, actions=[action])
                    sw.send_msg(mod)
                    match = sw.ofproto_parser.OFPMatch(in_port=switch3_eth1_inport[i], dl_type=0x800,dl_vlan=switch3_eth1_vlan[i])
                    action = sw.ofproto_parser.OFPActionOutput(switch3_eth1_outport[i])
                    mod = sw.ofproto_parser.OFPFlowMod(
                        datapath=sw, match=match, cookie=0,
                        command=ofproto.OFPFC_ADD, idle_timeout=0, hard_timeout=0,
                        priority=1000,
                        flags=ofproto.OFPFF_SEND_FLOW_REM, actions=[action])
                    sw.send_msg(mod)  
            if sw.id == 4:
                for i in range(66):
                    match = sw.ofproto_parser.OFPMatch(in_port=switch4_eth1_inport[i], dl_type=0x806,dl_vlan=switch4_eth1_vlan[i])
                    action = sw.ofproto_parser.OFPActionOutput(switch4_eth1_outport[i])
                    mod = sw.ofproto_parser.OFPFlowMod(
                        datapath=sw, match=match, cookie=0,
                        command=ofproto.OFPFC_ADD, idle_timeout=0, hard_timeout=0,
                        priority=1000,
                        flags=ofproto.OFPFF_SEND_FLOW_REM, actions=[action])
                    sw.send_msg(mod)
                    match = sw.ofproto_parser.OFPMatch(in_port=switch4_eth1_inport[i], dl_type=0x800,dl_vlan=switch4_eth1_vlan[i])
                    action = sw.ofproto_parser.OFPActionOutput(switch4_eth1_outport[i])
                    mod = sw.ofproto_parser.OFPFlowMod(
                        datapath=sw, match=match, cookie=0,
                        command=ofproto.OFPFC_ADD, idle_timeout=0, hard_timeout=0,
                        priority=1000,
                        flags=ofproto.OFPFF_SEND_FLOW_REM, actions=[action])
                    sw.send_msg(mod)  
            if sw.id == 5:
                for i in range(58):
                    match = sw.ofproto_parser.OFPMatch(in_port=switch5_eth1_inport[i], dl_type=0x806,dl_vlan=switch5_eth1_vlan[i])
                    action = sw.ofproto_parser.OFPActionOutput(switch5_eth1_outport[i])
                    mod = sw.ofproto_parser.OFPFlowMod(
                        datapath=sw, match=match, cookie=0,
                        command=ofproto.OFPFC_ADD, idle_timeout=0, hard_timeout=0,
                        priority=1000,
                        flags=ofproto.OFPFF_SEND_FLOW_REM, actions=[action])
                    sw.send_msg(mod)  
                    match = sw.ofproto_parser.OFPMatch(in_port=switch5_eth1_inport[i], dl_type=0x800,dl_vlan=switch5_eth1_vlan[i])
                    action = sw.ofproto_parser.OFPActionOutput(switch5_eth1_outport[i])
                    mod = sw.ofproto_parser.OFPFlowMod(
                        datapath=sw, match=match, cookie=0,
                        command=ofproto.OFPFC_ADD, idle_timeout=0, hard_timeout=0,
                        priority=1000,
                        flags=ofproto.OFPFF_SEND_FLOW_REM, actions=[action])
                    sw.send_msg(mod)   
            if sw.id == 6:
                for i in range(58):
                    match = sw.ofproto_parser.OFPMatch(in_port=switch6_eth1_inport[i], dl_type=0x806,dl_vlan=switch6_eth1_vlan[i])
                    action = sw.ofproto_parser.OFPActionOutput(switch6_eth1_outport[i])
                    mod = sw.ofproto_parser.OFPFlowMod(
                        datapath=sw, match=match, cookie=0,
                        command=ofproto.OFPFC_ADD, idle_timeout=0, hard_timeout=0,
                        priority=1000,
                        flags=ofproto.OFPFF_SEND_FLOW_REM, actions=[action])
                    sw.send_msg(mod)
                    match = sw.ofproto_parser.OFPMatch(in_port=switch6_eth1_inport[i], dl_type=0x800,dl_vlan=switch6_eth1_vlan[i])
                    action = sw.ofproto_parser.OFPActionOutput(switch6_eth1_outport[i])
                    mod = sw.ofproto_parser.OFPFlowMod(
                        datapath=sw, match=match, cookie=0,
                        command=ofproto.OFPFC_ADD, idle_timeout=0, hard_timeout=0,
                        priority=1000,
                        flags=ofproto.OFPFF_SEND_FLOW_REM, actions=[action])
                    sw.send_msg(mod)                
            if sw.id == 7:
                for i in range(58):
                    match = sw.ofproto_parser.OFPMatch(in_port=switch7_eth1_inport[i], dl_type=0x806,dl_vlan=switch7_eth1_vlan[i])
                    action = sw.ofproto_parser.OFPActionOutput(switch7_eth1_outport[i])
                    mod = sw.ofproto_parser.OFPFlowMod(
                        datapath=sw, match=match, cookie=0,
                        command=ofproto.OFPFC_ADD, idle_timeout=0, hard_timeout=0,
                        priority=1000,
                        flags=ofproto.OFPFF_SEND_FLOW_REM, actions=[action])
                    sw.send_msg(mod)    
                    match = sw.ofproto_parser.OFPMatch(in_port=switch7_eth1_inport[i], dl_type=0x800,dl_vlan=switch7_eth1_vlan[i])
                    action = sw.ofproto_parser.OFPActionOutput(switch7_eth1_outport[i])
                    mod = sw.ofproto_parser.OFPFlowMod(
                        datapath=sw, match=match, cookie=0,
                        command=ofproto.OFPFC_ADD, idle_timeout=0, hard_timeout=0,
                        priority=1000,
                        flags=ofproto.OFPFF_SEND_FLOW_REM, actions=[action])
                    sw.send_msg(mod)                
            if sw.id == 8:
                for i in range(58):
                    match = sw.ofproto_parser.OFPMatch(in_port=switch8_eth1_inport[i], dl_type=0x806,dl_vlan=switch8_eth1_vlan[i])
                    action = sw.ofproto_parser.OFPActionOutput(switch8_eth1_outport[i])
                    mod = sw.ofproto_parser.OFPFlowMod(
                        datapath=sw, match=match, cookie=0,
                        command=ofproto.OFPFC_ADD, idle_timeout=0, hard_timeout=0,
                        priority=1000,
                        flags=ofproto.OFPFF_SEND_FLOW_REM, actions=[action])
                    sw.send_msg(mod)
                    match = sw.ofproto_parser.OFPMatch(in_port=switch8_eth1_inport[i], dl_type=0x800,dl_vlan=switch8_eth1_vlan[i])
                    action = sw.ofproto_parser.OFPActionOutput(switch8_eth1_outport[i])
                    mod = sw.ofproto_parser.OFPFlowMod(
                        datapath=sw, match=match, cookie=0,
                        command=ofproto.OFPFC_ADD, idle_timeout=0, hard_timeout=0,
                        priority=1000,
                        flags=ofproto.OFPFF_SEND_FLOW_REM, actions=[action])
                    sw.send_msg(mod)                
            if sw.id == 9: 
                for i in range(80): 
                    match = sw.ofproto_parser.OFPMatch(in_port=AGswitch0_eth1_inport[i], dl_type=0x806,dl_vlan=AGswitch0_eth1_vlan[i])
                    action = sw.ofproto_parser.OFPActionOutput(AGswitch0_eth1_outport[i])
                    mod = sw.ofproto_parser.OFPFlowMod(
                        datapath=sw, match=match, cookie=0,
                        command=ofproto.OFPFC_ADD, idle_timeout=0, hard_timeout=0,
                        priority=1000,
                        flags=ofproto.OFPFF_SEND_FLOW_REM, actions=[action])
                    sw.send_msg(mod)    
                    match = sw.ofproto_parser.OFPMatch(in_port=AGswitch0_eth1_inport[i], dl_type=0x800,dl_vlan=AGswitch0_eth1_vlan[i])
                    action = sw.ofproto_parser.OFPActionOutput(AGswitch0_eth1_outport[i])
                    mod = sw.ofproto_parser.OFPFlowMod(
                        datapath=sw, match=match, cookie=0,
                        command=ofproto.OFPFC_ADD, idle_timeout=0, hard_timeout=0,
                        priority=1000,
                        flags=ofproto.OFPFF_SEND_FLOW_REM, actions=[action])
                    sw.send_msg(mod) 
            if sw.id == 10: 
                for i in range(24): 
                    match = sw.ofproto_parser.OFPMatch(in_port=AGswitch1_eth1_inport[i], dl_type=0x806,dl_vlan = AGswitch1_eth1_vlan[i])
                    action = sw.ofproto_parser.OFPActionOutput(AGswitch1_eth1_outport[i])
                    mod = sw.ofproto_parser.OFPFlowMod(
                        datapath=sw, match=match, cookie=0,
                        command=ofproto.OFPFC_ADD, idle_timeout=0, hard_timeout=0,
                        priority=1000,
                        flags=ofproto.OFPFF_SEND_FLOW_REM, actions=[action])
                    sw.send_msg(mod)
                    match = sw.ofproto_parser.OFPMatch(in_port=AGswitch1_eth1_inport[i], dl_type=0x800,dl_vlan= AGswitch1_eth1_vlan[i])
                    action = sw.ofproto_parser.OFPActionOutput(AGswitch1_eth1_outport[i])
                    mod = sw.ofproto_parser.OFPFlowMod(
                        datapath=sw, match=match, cookie=0,
                        command=ofproto.OFPFC_ADD, idle_timeout=0, hard_timeout=0,
                        priority=1000,
                        flags=ofproto.OFPFF_SEND_FLOW_REM, actions=[action])
                    sw.send_msg(mod)                     
            if sw.id == 11: 
                for i in range(64): 
                    match = sw.ofproto_parser.OFPMatch(in_port=AGswitch2_eth1_inport[i], dl_type=0x806,dl_vlan=AGswitch2_eth1_vlan[i])
                    action = sw.ofproto_parser.OFPActionOutput(AGswitch2_eth1_outport[i])
                    mod = sw.ofproto_parser.OFPFlowMod(
                        datapath=sw, match=match, cookie=0,
                        command=ofproto.OFPFC_ADD, idle_timeout=0, hard_timeout=0,
                        priority=1000,
                        flags=ofproto.OFPFF_SEND_FLOW_REM, actions=[action])
                    sw.send_msg(mod)    
                    match = sw.ofproto_parser.OFPMatch(in_port=AGswitch2_eth1_inport[i], dl_type=0x800,dl_vlan=AGswitch2_eth1_vlan[i])
                    action = sw.ofproto_parser.OFPActionOutput(AGswitch2_eth1_outport[i])
                    mod = sw.ofproto_parser.OFPFlowMod(
                        datapath=sw, match=match, cookie=0,
                        command=ofproto.OFPFC_ADD, idle_timeout=0, hard_timeout=0,
                        priority=1000,
                        flags=ofproto.OFPFF_SEND_FLOW_REM, actions=[action])
                    sw.send_msg(mod)  
            if sw.id == 12: 
                for i in range(40): 
                    match = sw.ofproto_parser.OFPMatch(in_port=AGswitch3_eth1_inport[i], dl_type=0x806,dl_vlan=AGswitch3_eth1_vlan[i])
                    action = sw.ofproto_parser.OFPActionOutput(AGswitch3_eth1_outport[i])
                    mod = sw.ofproto_parser.OFPFlowMod(
                        datapath=sw, match=match, cookie=0,
                        command=ofproto.OFPFC_ADD, idle_timeout=0, hard_timeout=0,
                        priority=1000,
                        flags=ofproto.OFPFF_SEND_FLOW_REM, actions=[action])
                    sw.send_msg(mod)    
                    match = sw.ofproto_parser.OFPMatch(in_port=AGswitch3_eth1_inport[i], dl_type=0x800,dl_vlan=AGswitch3_eth1_vlan[i])
                    action = sw.ofproto_parser.OFPActionOutput(AGswitch3_eth1_outport[i])
                    mod = sw.ofproto_parser.OFPFlowMod(
                        datapath=sw, match=match, cookie=0,
                        command=ofproto.OFPFC_ADD, idle_timeout=0, hard_timeout=0,
                        priority=1000,
                        flags=ofproto.OFPFF_SEND_FLOW_REM, actions=[action])
                    sw.send_msg(mod)                    
            if sw.id == 13: 
                for i in range(56): 
                    match = sw.ofproto_parser.OFPMatch(in_port=AGswitch4_eth1_inport[i], dl_type=0x806,dl_vlan=AGswitch4_eth1_vlan[i])
                    action = sw.ofproto_parser.OFPActionOutput(AGswitch4_eth1_outport[i])
                    mod = sw.ofproto_parser.OFPFlowMod(
                        datapath=sw, match=match, cookie=0,
                        command=ofproto.OFPFC_ADD, idle_timeout=0, hard_timeout=0,
                        priority=1000,
                        flags=ofproto.OFPFF_SEND_FLOW_REM, actions=[action])
                    sw.send_msg(mod)    
                    match = sw.ofproto_parser.OFPMatch(in_port=AGswitch4_eth1_inport[i], dl_type=0x800,dl_vlan=AGswitch4_eth1_vlan[i])
                    action = sw.ofproto_parser.OFPActionOutput(AGswitch4_eth1_outport[i])
                    mod = sw.ofproto_parser.OFPFlowMod(
                        datapath=sw, match=match, cookie=0,
                        command=ofproto.OFPFC_ADD, idle_timeout=0, hard_timeout=0,
                        priority=1000,
                        flags=ofproto.OFPFF_SEND_FLOW_REM, actions=[action])
                    sw.send_msg(mod)                    
            if sw.id == 14: 
                for i in range(48): 
                    match = sw.ofproto_parser.OFPMatch(in_port=AGswitch5_eth1_inport[i], dl_type=0x806,dl_vlan=AGswitch5_eth1_vlan[i])
                    action = sw.ofproto_parser.OFPActionOutput(AGswitch5_eth1_outport[i])
                    mod = sw.ofproto_parser.OFPFlowMod(
                        datapath=sw, match=match, cookie=0,
                        command=ofproto.OFPFC_ADD, idle_timeout=0, hard_timeout=0,
                        priority=1000,
                        flags=ofproto.OFPFF_SEND_FLOW_REM, actions=[action])
                    sw.send_msg(mod)    
                    match = sw.ofproto_parser.OFPMatch(in_port=AGswitch5_eth1_inport[i], dl_type=0x800,dl_vlan=AGswitch5_eth1_vlan[i])
                    action = sw.ofproto_parser.OFPActionOutput(AGswitch5_eth1_outport[i])
                    mod = sw.ofproto_parser.OFPFlowMod(
                        datapath=sw, match=match, cookie=0,
                        command=ofproto.OFPFC_ADD, idle_timeout=0, hard_timeout=0,
                        priority=1000,
                        flags=ofproto.OFPFF_SEND_FLOW_REM, actions=[action])
                    sw.send_msg(mod)
            if sw.id == 15: 
                for i in range(56): 
                    match = sw.ofproto_parser.OFPMatch(in_port=AGswitch6_eth1_inport[i], dl_type=0x806,dl_vlan=AGswitch6_eth1_vlan[i])
                    action = sw.ofproto_parser.OFPActionOutput(AGswitch6_eth1_outport[i])
                    mod = sw.ofproto_parser.OFPFlowMod(
                        datapath=sw, match=match, cookie=0,
                        command=ofproto.OFPFC_ADD, idle_timeout=0, hard_timeout=0,
                        priority=1000,
                        flags=ofproto.OFPFF_SEND_FLOW_REM, actions=[action])
                    sw.send_msg(mod)    
                    match = sw.ofproto_parser.OFPMatch(in_port=AGswitch6_eth1_inport[i], dl_type=0x800,dl_vlan=AGswitch6_eth1_vlan[i])
                    action = sw.ofproto_parser.OFPActionOutput(AGswitch6_eth1_outport[i])
                    mod = sw.ofproto_parser.OFPFlowMod(
                        datapath=sw, match=match, cookie=0,
                        command=ofproto.OFPFC_ADD, idle_timeout=0, hard_timeout=0,
                        priority=1000,
                        flags=ofproto.OFPFF_SEND_FLOW_REM, actions=[action])
                    sw.send_msg(mod)                    
            if sw.id == 16: 
                for i in range(48): 
                    match = sw.ofproto_parser.OFPMatch(in_port=AGswitch7_eth1_inport[i], dl_type=0x806,dl_vlan=AGswitch7_eth1_vlan[i])
                    action = sw.ofproto_parser.OFPActionOutput(AGswitch7_eth1_outport[i])
                    mod = sw.ofproto_parser.OFPFlowMod(
                        datapath=sw, match=match, cookie=0,
                        command=ofproto.OFPFC_ADD, idle_timeout=0, hard_timeout=0,
                        priority=1000,
                        flags=ofproto.OFPFF_SEND_FLOW_REM, actions=[action])
                    sw.send_msg(mod)    
                    match = sw.ofproto_parser.OFPMatch(in_port=AGswitch7_eth1_inport[i], dl_type=0x800,dl_vlan=AGswitch7_eth1_vlan[i])
                    action = sw.ofproto_parser.OFPActionOutput(AGswitch7_eth1_outport[i])
                    mod = sw.ofproto_parser.OFPFlowMod(
                        datapath=sw, match=match, cookie=0,
                        command=ofproto.OFPFC_ADD, idle_timeout=0, hard_timeout=0,
                        priority=1000,
                        flags=ofproto.OFPFF_SEND_FLOW_REM, actions=[action])
                    sw.send_msg(mod)                     
            if sw.id == 17: 
                for i in range(96): 
                    match = sw.ofproto_parser.OFPMatch(in_port=COswitch0_eth1_inport[i], dl_type=0x806,dl_vlan = COswitch0_eth1_vlan[i])
                    action = sw.ofproto_parser.OFPActionOutput(COswitch0_eth1_outport[i])
                    mod = sw.ofproto_parser.OFPFlowMod(
                        datapath=sw, match=match, cookie=0,
                        command=ofproto.OFPFC_ADD, idle_timeout=0, hard_timeout=0,
                        priority=1000,
                        flags=ofproto.OFPFF_SEND_FLOW_REM, actions=[action])
                    sw.send_msg(mod)
                    match = sw.ofproto_parser.OFPMatch(in_port=COswitch0_eth1_inport[i], dl_type=0x800,dl_vlan= COswitch0_eth1_vlan[i])
                    action = sw.ofproto_parser.OFPActionOutput(COswitch0_eth1_outport[i])
                    mod = sw.ofproto_parser.OFPFlowMod(
                        datapath=sw, match=match, cookie=0,
                        command=ofproto.OFPFC_ADD, idle_timeout=0, hard_timeout=0,
                        priority=1000,
                        flags=ofproto.OFPFF_SEND_FLOW_REM, actions=[action])
                    sw.send_msg(mod)  
            if sw.id == 18: 
                for i in range(24): 
                    match = sw.ofproto_parser.OFPMatch(in_port=COswitch1_eth1_inport[i], dl_type=0x806,dl_vlan = COswitch1_eth1_vlan[i])
                    action = sw.ofproto_parser.OFPActionOutput(COswitch1_eth1_outport[i])
                    mod = sw.ofproto_parser.OFPFlowMod(
                        datapath=sw, match=match, cookie=0,
                        command=ofproto.OFPFC_ADD, idle_timeout=0, hard_timeout=0,
                        priority=1000,
                        flags=ofproto.OFPFF_SEND_FLOW_REM, actions=[action])
                    sw.send_msg(mod)
                    match = sw.ofproto_parser.OFPMatch(in_port=COswitch1_eth1_inport[i], dl_type=0x800,dl_vlan= COswitch1_eth1_vlan[i])
                    action = sw.ofproto_parser.OFPActionOutput(COswitch1_eth1_outport[i])
                    mod = sw.ofproto_parser.OFPFlowMod(
                        datapath=sw, match=match, cookie=0,
                        command=ofproto.OFPFC_ADD, idle_timeout=0, hard_timeout=0,
                        priority=1000,
                        flags=ofproto.OFPFF_SEND_FLOW_REM, actions=[action])
                    sw.send_msg(mod)  
            if sw.id == 19: 
                for i in range(40): 
                    match = sw.ofproto_parser.OFPMatch(in_port=COswitch2_eth1_inport[i], dl_type=0x806,dl_vlan = COswitch2_eth1_vlan[i])
                    action = sw.ofproto_parser.OFPActionOutput(COswitch2_eth1_outport[i])
                    mod = sw.ofproto_parser.OFPFlowMod(
                        datapath=sw, match=match, cookie=0,
                        command=ofproto.OFPFC_ADD, idle_timeout=0, hard_timeout=0,
                        priority=1000,
                        flags=ofproto.OFPFF_SEND_FLOW_REM, actions=[action])
                    sw.send_msg(mod)
                    match = sw.ofproto_parser.OFPMatch(in_port=COswitch2_eth1_inport[i], dl_type=0x800,dl_vlan= COswitch2_eth1_vlan[i])
                    action = sw.ofproto_parser.OFPActionOutput(COswitch2_eth1_outport[i])
                    mod = sw.ofproto_parser.OFPFlowMod(
                        datapath=sw, match=match, cookie=0,
                        command=ofproto.OFPFC_ADD, idle_timeout=0, hard_timeout=0,
                        priority=1000,
                        flags=ofproto.OFPFF_SEND_FLOW_REM, actions=[action])
                    sw.send_msg(mod)   
            if sw.id == 20: 
                for i in range(32): 
                    match = sw.ofproto_parser.OFPMatch(in_port=COswitch3_eth1_inport[i], dl_type=0x806,dl_vlan = COswitch3_eth1_vlan[i])
                    action = sw.ofproto_parser.OFPActionOutput(COswitch3_eth1_outport[i])
                    mod = sw.ofproto_parser.OFPFlowMod(
                        datapath=sw, match=match, cookie=0,
                        command=ofproto.OFPFC_ADD, idle_timeout=0, hard_timeout=0,
                        priority=1000,
                        flags=ofproto.OFPFF_SEND_FLOW_REM, actions=[action])
                    sw.send_msg(mod)
                    match = sw.ofproto_parser.OFPMatch(in_port=COswitch3_eth1_inport[i], dl_type=0x800,dl_vlan= COswitch3_eth1_vlan[i])
                    action = sw.ofproto_parser.OFPActionOutput(COswitch3_eth1_outport[i])
                    mod = sw.ofproto_parser.OFPFlowMod(
                        datapath=sw, match=match, cookie=0,
                        command=ofproto.OFPFC_ADD, idle_timeout=0, hard_timeout=0,
                        priority=1000,
                        flags=ofproto.OFPFF_SEND_FLOW_REM, actions=[action])
                    sw.send_msg(mod)                     
            
            
            
    # the rest of the code
    @set_ev_cls(dpset.EventDP)
    def switchStatus(self, ev):
        print("Switch %s: %s!" %
                (ev.dp.id, "connected" if ev.enter else "disconnected"))

        self.prepareSwitch(ev.dp)
