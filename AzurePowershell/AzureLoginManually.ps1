

function AzureLogin{
    Login-AzureRmAccount
    Get-AzureRmResourceGroup | select ResourceGroupName
    Save-AzureRmProfile -Path "login.json"


}


function SilentLogin{
Select-AzureRmProfile -Path “login.json”
}

function CreateRG ($Name, $Location){
    # First Check if the RG exists with this name
    [String]$Name1=$Name

    Get-AzureRmResourceGroup -Name $Name1 -ev notpresent -ea 0
    
    if ($notpresent){

        Write-Host "RG for this Name doesnot Exist Creating new RG !!!!"
        New-AzureRmResourceGroup -Name $Name -Location $Location
        Write-Host "RG $Name Created !!!!"
       
    }
    else{
    
        Write-Host "RESOURCE GROUP $Name Exists !!! Please Specify Another Name"
        
    }

}




function RGCheck ($Name, $Location){
    # First Check if the RG exists with this name
    Get-AzureRmResourceGroup -Name $Name -ev notpresent -ea 0
    
    if ($notpresent){
        
        return True
       
    }
    else{
    
      return False
        
    }

}
function VnetSubet($Name,$location,$RG){
   

  if(RGCheck($RG)) {
        Write-Host "RG exists"
  }
   else{
        Write-Host "RG does not exist First Create RG"
   }
    
}

