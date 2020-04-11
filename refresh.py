import psutil

for process in psutil.process_iter():
    print(process)
    try:
        #WINDOWS
        if process.name() == "LeagueClientUxRender.exe":
            process.kill()
        #MAC OS
        elif process.name() == "LeagueClientUx Helper":
            process.kill()
    except:
        pass
