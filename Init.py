import subprocess
import time

# Check internet connection
def check_internet():
    try:
        # Check if internet is accessible by making a request to a reliable website
        response = subprocess.check_output(['ping', '-c', '1', 'google.com'])
        return True
    except subprocess.CalledProcessError:
        return False

# Wait until internet connection is available
connected_to_internet = False
while not connected_to_internet:
    if check_internet():
        connected_to_internet = True
    else:
        # Wait for a certain period before checking again
        time.sleep(5)

# VPN connection command
command = 'echo "Panitan03" | sudo openconnect --protocol=gp ipsec.bu.ac.th --user=panitan.kwan --passwd-on-stdin'
log_file = '/home/panitank/BUOS/init.log'

# Run the VPN connection command and redirect the output to a log file
subprocess.call(['bash', '-c', '{} > {} 2>&1'.format(command, log_file)])
