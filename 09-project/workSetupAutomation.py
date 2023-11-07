import webbrowser as wb
import os

codepath = "C:/Users/ghani/AppData/Local/Programs/Microsoft VS Code/Code.exe"
os.startfile(codepath)


def workAuto():
    chrome_path = 'C:/Program Files/Google/Chrome/Application/chrome.exe %s'
    URLS = (
            "google.com",
            "github.com/AbdighaniMD",
            "stackoverflow.com",
            "youtube.com"
        )
    
    for url in URLS:
        wb.get(chrome_path).open(url)

workAuto()