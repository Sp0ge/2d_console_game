import keyboard

def action_get() -> list:  
    buttons = [False, False, False, False]
    
    if keyboard.is_pressed('w'):
        buttons[0] = True
        
    if keyboard.is_pressed('a'):
        buttons[1] = True
    
    if keyboard.is_pressed('s'):
        buttons[2] = True
        
    if keyboard.is_pressed('d'):
        buttons[3] = True
        
    return buttons
