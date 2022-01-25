function getuser {
    $env:USERNAME
}
$user = " User is ", (getuser)
function getip {
    (Get-NetIPAddress).IPv4Address | Select-String "192*" 
}
function getpname{
    (Get-PSHostProcessInfo -Id "1984").ProcessName
}
$myip = (getip)
$mypname= " process name is ", (getpname)
$myver = " Version ",$host.version.Major, " Today's date is "
$myDate = get-date -Format "dddd, MM, dd, yyyy" 
$myHname = " Hostname is ", $env:COMPUTERNAME
Write-Host " This machine's IP address is ", $myip,  $user, $myHname , $mypname,  $myver,  $myDate
Add-Content -Path "C:\it3038c-scripts\powershell\test1.txt" -Nonewline -Value " This machine's IP address is ",$myip, $user,$myHname,$mypname,$myver,$myDate
