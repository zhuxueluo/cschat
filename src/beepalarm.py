def fourbeep():
    import ctypes
    import time
    player=ctypes.windll.kernel32
    for i in range(4):
        player.Beep(2000,200)
        time.sleep(0.001)
def twobeep():
    import ctypes
    import time
    player=ctypes.windll.kernel32
    for i in range(2):
        player.Beep(2000,200)
        time.sleep(0.001)
        
def alarm_fourbeep(times):
    if times>0:
        for i in range(times):
            fourbeep()
            import time
            time.sleep(0.5)
    else:
        print 'input positive number'
def alarm_twobeep(times):
    if times>0:
        for i in range(times):
            twobeep()
            import time
            time.sleep(0.5)
    else:
        print 'input positive number'