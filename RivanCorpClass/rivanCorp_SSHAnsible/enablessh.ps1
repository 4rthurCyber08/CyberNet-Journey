# Get Windows Capability
Get-WindowsCapability -Online | Where-Object { $_.Name -like 'OpenSSH*' }

# Add OpenSSH Server Capability
Add-WindowsCapability -Online -Name OpenSSH.Server~~~~0.0.1.0 

# Start the SSH Server service
Start-Service -Name "sshd" 

# Set the SSH Server service to start automatically
Set-Service -Name "sshd" -StartupType Automatic 

# Display SSH Server service details
Get-Service -Name "sshd" | Select-Object *

# Create a firewall rule to allow SSH traffic
New-NetFirewallRule -Name "SSH" `
    -DisplayName "SSH" `
    -Description "Allow SSH" `
    -Profile Any `
    -Direction Inbound `
    -Action Allow `
    -Protocol TCP `
    -Program Any `
    -LocalAddress Any `
    -RemoteAddress Any `
    -LocalPort 22 `
    -RemotePort Any