#------------------------------------------------------------------
# Author: Shailesh Thakur
# Description: Silent Login to Azure 
# Version: 1.0
#------------------------------------------------------------------


#------------------------------------------------------------------
# Function Name: AzureLogin
# Parameters Passed: 0
# Description : Logs to Azure manually, gets the Randon resource 
#               group and saves the Json file
#------------------------------------------------------------------

function AzureLogin{

    Login-AzureRmAccount
    Get-AzureRmResourceGroup | select ResourceGroupName
    Save-AzureRmProfile -Path "login.json"


}

# Just Call it once 

AzureLogin

# This can be used  later as many times we need to login to Azure 

Select-AzureRmProfile -Path “login.json”



