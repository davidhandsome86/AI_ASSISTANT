import time

def get_current_date(): 
    return time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
        
def get_week():
    return time.strftime('%A', time.localtime())

def get_zone():
    return time.strftime('%z', time.localtime())