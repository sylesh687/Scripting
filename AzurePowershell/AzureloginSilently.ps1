. C:\Users\thakshai\Desktop\Scripting\AzurePowershell\AzureLoginManually.ps1


#-----------------------------------------------------------------------------------
#       Variable Declaration and Definition Area


[String]$RG="Osgroup"
$Location="South Central US"

$RuleName1="osgrouprule"
$RuleName2="Osgrouprule2"
$NSGNAME="OsgroupNSG"
$LOCATION="South Central US"
$VNetName="OsgroupVNET"
$SubNetName="OsgroupSubnet1"


SilentLogin

CreateRG(${RG},$Location)

write-output $RG

[datetime]$d="12/25/2019"

$Rule1=New-AzureRmNetworkSecurityRuleConfig -Name "web-rule" -Description "allow all" `
-Access Allow -Protocol Tcp -Direction Inbound -Priority 100 -SourceAddressPrefix Internet `
-SourcePortRange "*" -DestinationAddressPrefix * -DestinationPortRange *


$NSG=New-AzureRmNetworkSecurityGroup -Name $NSGNAME -ResourceGroupName $RG -Location $LOCATION `
-SecurityRules $Rule1

Get-AzureRmVirtualNetwork -Name 

Get-AzureRmResourceGroupDeployment
Get-AzureRmResourceGroupDeploymentOperation

$PublciIPName="PIPOSGRP"
$DnsName="osgroup-techies"

$PIP=New-AzureRmPublicIpAddress -Name $PublciIPName -ResourceGroupName $RG -DomainNameLabel $DnsName `
-Location $LOCATION -AllocationMethod Static

$PIP
$NICName="osgroupNIC"
$vnet = Get-AzureRmVirtualNetwork -ResourceGroupName $RG -Name $VNetName
$vnet

$NIC=New-AzureRmNetworkInterface -Name $NICName -ResourceGroupName $RG -Location $LOCATION `
-SubnetId $vnet.Subnets[0].id -PublicIpAddressId $PIP.Id -NetworkSecurityGroupId $NSG.Id

$NIC

$RG="Osgroup"
$VNETName="OsgroupVnet"
$Subnet1="Os1"
$LOCATION="South Central US"

Select-AzureRmProfile -Path “login.json”

$VNET=New-AzureRmVirtualNetwork -Name $VNETName -ResourceGroupName $RG -Location $LOCATION `
-AddressPrefix  192.168.0.0/16



Add-AzureRmVirtualNetworkSubnetConfig -Name $Subnet1 -VirtualNetwork $VNET `
-AddressPrefix 192.168.1.0/24

Set-AzureRmVirtualNetworkSubnetConfig -VirtualNetwork $VNET -Name $Subnet1 `
-AddressPrefix 192.168.1.0/24 -NetworkSecurityGroup $NSG


Set-AzureRmVirtualNetwork -VirtualNetwork $VNET

Get-AzureRmVirtualNetwork -ResourceGroupName $RG -Name $VNETName
