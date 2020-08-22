import os
print()
print()

print ("             **************************************************************************************************************   "    )
print ("                                                      Hello Welcome to my Bot - Chingari v1.0                                 "    )
print ("Note: Use Chingari to access/open/run the Windows Environtments                                                               "    )                               
print ("             **************************************************************************************************************   "    )
print ()

while True: 

    print ("                   Happy to serve your request, Please try here:  " , end='')
    i = input ()

    if ("open" in i  and "notepad" in i or "editor" in i):
        os.system("notepad")

    elif ("open" in i  and "chrome" in i or "browser" in i):
        os.system("chrome")
    
    elif ("open" in i  and "explorer" in i ):
        os.system ("explorer")
        
    elif ("open" in i  and "mmc" in i ):
        os.system ("mmc")
    
    elif ("open" in i  and "word" in i or "doc" in i or "office" in i):
        os.system ("wps")
        
    elif ("open" in i  and "excel" in i or "xl" in i or "sheet" in i):
        os.system ("et")
        
    elif ("open" in i  and "ppt" in i or "present" in i or "power" in i or "point" in i):
        os.system ("wpp")
  
    elif ("show" in i or "current" in i  and "time" in i):
        os.system ("time")
        
    elif ("show" in i or "today's" in i  and "date" in i):
        os.system ("date")
   
    elif ("open" in i  and "calc" in i or "calculator" in i):
        os.system ("calc")
  
    elif ("open" in i  and "cmd" in i or "command prompt" in i or "cli" in i):
         os.system ("cmd")
            
    elif ("run" in i or "open" in i and "git" in i  or  "gui" in i):
           os.system ("git-gui")
   
    elif ("close" in i or "exit" in i or "quit" in i ):
            break
  
    else:
        print("Dont Support")
  

 

 
