 $VnetName=$Name+'Vnet'
    $VnetName="sylesh-vnet"
    $RG="Osgroup"
    $Subnet1=New-AzureRmVirtualNetworkSubnetConfig -Name $Name -AddressPrefix 192.168.0.0/24
    Get-AzureRmVirtualNetwork 
    $Vnet=New-AzureRmVirtualNetwork -Name $VnetName -Location $location -ResourceGroupName $RG `

    if (Get-AzureRmVirtualNetwork -Name $VnetName -ResourceGroupName $RG){
        Write-host "THE VIRTUAL NETWORK ALREADY EXIST !!!! JUST NEED TO ADD NEW SUBNET /"
    }
    else{
        Write-host "VIRTUAL NETWORK DOESNOT EXIST WITH SAME NAME"
    }