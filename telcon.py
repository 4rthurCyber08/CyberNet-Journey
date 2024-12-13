import netmiko
from netmiko import ConnectHandler

class ConnectCisco:
    def __init__(self, device_info):
        self.device_info = device_info
    
    def login(self):
        self.access_cli = netmiko.ConnectHandler(**self.device_info)
        
        return self.access_cli

def getPCList():
    # prompt user for pcs to be erased
    
    list_of_pcs = input('List of PCs: ')
    monitors = list_of_pcs.split(',')
    
    return monitors

active_pcs = getPCList()

# configure each pcs in the list
for m in active_pcs:
    core_taas_ip = '10.' + m + '.1.2'
    core_baba_ip = '10.' + m + '.1.4'
    call_manager_ip = '10.' + m + '.100.8'
    edge_router_ip = '200.0.0.' + m
    
    device_list = ['coreTaas', 'callManager', 'coreBaba', 'edgeRouter']
    
    for device in device_list:
        if device == 'coreTaas':
            device_ip = core_taas_ip
        elif device == 'coreBaba':
            device_ip = core_baba_ip
        elif device == 'callManager':
            device_ip = call_manager_ip
        elif device == 'edgeRouter':
            device_ip = edge_router_ip
        
        device_info= {
            'device_type': 'cisco_ios_telnet',
            'host': device_ip,
            'username': 'admin',
            'password': 'pass',
            'secret': 'pass'
        }

        must_rel = False
        clearStartConfig = False
        
        # access device cli
        access_cli = ConnectCisco(device_info).login()
        access_cli.enable()
        
        # prevent netmiko from returning an error when the cli takes a lot of time to respond
        access_cli.fast_cli = False
        
        # don't delete vlan.dat on edgeRouter
        if device != 'edgeRouter':
            output1 = access_cli.send_command('delete vlan.dat', expect_string='vlan.dat')
            output2 = access_cli.send_command('', expect_string='confirm')
            output3 = access_cli.send_command('')
        
        # remove startup-config on all devices
        output4 = access_cli.send_command('wr er', expect_string='confirm')
        output5 = access_cli.send_command('')
        
        # reload device
        if must_rel:
            output6 = access_cli.send_command('reload', expect_string='confirm')
            output7 = access_cli.send_command('')
        
        
        access_cli.fast_cli = True
        
        
        # inform user
        print('---------Connecting to ' + device + ' [' + device_ip + ']')
        print('Deleting vlan.dat on ' + device + '...')
        #print(output1)
        #print(output2)
        #print(output3)
        print('Success!!!')
        
        print('Deleting startup-config on ' + device)
        #print(output4)
        #print(output5)
        print('Success!!!')
    
    







#enterPrompt = accessCLI.send_command('')

#accessCLI.fast_cli = False
#showIPCUCM = accessCLI.send_command('wr er', expect_string='confirm')
#showIPCUCM += accessCLI.send_command(enterPrompt)
#accessCLI.fast_cli = True

#print(showIPCUCM)