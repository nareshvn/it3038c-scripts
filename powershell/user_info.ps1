$Machines = 'localhost'
$myinfo='' 
$Logfile='C:\logs\user_info.txt'

$pt=Get-LocalUser

    $sample = 1 

    foreach ($p in $pt) { 
          $date = Get-Date -Format g 

        $myinfo= "UserName: {0} " -f $p
        Add-Content $Logfile "Info: ${myinfo}"

        $sample++ 
      
    } 
   $myinfo = Get-ComputerInfo -Property "CSUserName"
   Add-Content $Logfile "UserName Info: ${myinfo}"
    $myinfo = Get-ComputerInfo -Property "LogonServer"
   Add-Content $Logfile "Logon Server Info: ${myinfo}"
    $myinfo = Get-ClipBoard
    Add-Content $Logfile "User lately copied info in clipboard: ${myinfo}"


    
  