
$RG="Osgroup"
Select-AzureRmProfile -Path "mycredential.json"

$RuleName1="osgrouprule"
$RuleName2="Osgrouprule2"
$NSGNAME="OsgroupNSG"
$LOCATION="South Central US"
$VNetName="OsgroupVNET"
$SubNetName="OsgroupSubnet1"

$Rule1=New-AzureRmNetworkSecurityRuleConfig -Name "web-rule" -Description "allow all" `
-Access Allow -Protocol Tcp -Direction Inbound -Priority 100 -SourceAddressPrefix Internet `
-SourcePortRange "*" -DestinationAddressPrefix * -DestinationPortRange *


$NSG=New-AzureRmNetworkSecurityGroup -Name $NSGNAME -ResourceGroupName $RG -Location $LOCATION `
-SecurityRules $Rule1

$NSG


$VNET=New-AzureRmVirtualNetwork -Name $VNetName -ResourceGroupName $RG -Location $LOCATION `
-AddressPrefix  192.168.0.0/16


$VNET

Add-AzureRmVirtualNetworkSubnetConfig -Name $SubNetName -VirtualNetwork $VNET `
-AddressPrefix 192.168.1.0/24

 
Set-AzureRmVirtualNetworkSubnetConfig -VirtualNetwork $VNET -Name $SubNetName `
-AddressPrefix 192.168.1.0/24 -NetworkSecurityGroup $NSG

Set-AzureRmVirtualNetwork -VirtualNetwork $VNET

#---------------------------------------------------------------------------------------------#
#----------------------------Creating public IP-----------------------------------------------#

$PublciIPName="PIPOSGRP"
$DnsName="DNSOSGRP"

$PIP=New-AzureRmPublicIpAddress -Name $PublciIPName -ResourceGroupName $RG -DomainNameLabel $DnsName `
-Location $LOCATION -AllocationMethod Static


#-----------------Creating a another Subnet-------------------------#
$Subnet=New-AzureRmVirtualNetworkSubnetConfig -Name TESTSubnet -AddressPrefix 10.0.0.0/24

Add-AzureRmVirtualNetworkSubnetConfig -Name $Subnet -VirtualNetwork $VNET -AddressPrefix 10.1.1.0/16

#     Creating a NIC card for the Virtual Machine 

$NICName="osgroupNIC"

$vnet = Get-AzureRmVirtualNetwork -ResourceGroupName $RG -Name $VNetName

$NIC=New-AzureRmNetworkInterface -Name $NICName -ResourceGroupName $RG -Location $LOCATION `
-SubnetId $vnet.Subnets[0].id  -PublicIpAddressId $PIP.Id -NetworkSecurityGroupId $NSG.Id

$cred = Get-Credential

$vmConfig=New-AzureRmVMConfig -VMName sylesh -VMSize Standard_DS2 | `
Set-AzureRmVMOperatingSystem -Windows -ComputerName sylesh -Credential $cred | `
Set-AzureRmVMSourceImage -PublisherName MicrosoftWindowsServer -Offer WindowsServer -Skus 2016-Datacenter -Version latest | `
Add-AzureRmVMNetworkInterface -Id $NIC.Id

New-AzureRmVM -ResourceGroupNam e $RG -Location $LOCATION -VM $vmConfig