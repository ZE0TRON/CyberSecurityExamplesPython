import platform
def platformOS():
    if platform.system() == "Linux":
        print("Linux System")
    elif platform.system() == "Windows":
        print("Windows System")
        
