Set WshShell = CreateObject("WScript.Shell")
WshShell.Run chr(34) & "E:\system\startServer\nopaperserver.bat" & Chr(34), 0
Set WshShell = Nothing