import keyboard

def action_get() -> list:
    buttons = [False, False, False, False]
    
    if keyboard.is_pressed('up'):
        buttons[0] = True
        
    if keyboard.is_pressed('left'):
        buttons[1] = True
    
    if keyboard.is_pressed('down'):
        buttons[2] = True
        
    if keyboard.is_pressed('right'):
        buttons[3] = True