$RG="Osgroup"
$VNETName="OsgroupVnet"
$Subnet1="Os1"
$LOCATION="South Central US"


Select-AzureRmProfile -Path “login.json”
New-AzureRmResourceGroup -Name "Osgroup" -Location "South Central US"

$VNET=New-AzureRmVirtualNetwork -Name $VNETName -ResourceGroupName $RG -Location $LOCATION `
-AddressPrefix  192.168.0.0/16



Add-AzureRmVirtualNetworkSubnetConfig -Name $Subnet1 -VirtualNetwork $VNET `
-AddressPrefix 192.168.1.0/24

Get-AzureRmVirtualNetwork -ResourceGroupName $RG -Name $VNETName



$FirstRul1=New-AzureRmNetworkSecurityRuleConfig -Name rule1 -Access Allow -Description "Allow all" `
-DestinationAddressPrefix * -DestinationPortRange * -Direction Inbound -Priority 100 `
-Protocol Tcp -SourceAddressPrefix Internet -SourcePortRange *

$NSG=New-AzureRmNetworkSecurityGroup -Location $LOCATION -Name OsgroupNSG `
-ResourceGroupName $RG -SecurityRules $FirstRule

$NSG