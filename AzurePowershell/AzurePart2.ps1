
Select-AzureRmProfile -Path "mycredential.json"

New-AzureRmResourceGroup -Name "Osgroup" -Location "South Central US"

Get-AzureRmResourceGroup -Name "Osgroup"