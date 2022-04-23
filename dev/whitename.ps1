(Get-Content .\outputtest.csv) | 
    foreach {
        #"work some magic"
        $_ -replace '"\s+|\s+"','"'
    } | Out-File .\outputtest.csv
