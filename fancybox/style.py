
PRE= "\x1b["
#PRE= "\033["

# Styles
BOLD= PRE+"1m"
ITALIC= PRE+"3m"
UNDERLINE= PRE+"4m"
BLINK= PRE+"5m"
REVERSE= PRE+"7m"
    
# Colors 8 bit
FG_8BIT = PRE+"38;5;{}m"
BG_8BIT = PRE+"48;5;{}m"

# Colors RGB
FG_RGB = PRE+"38;2;{};{};{}m"
BG_RGB = PRE+"48;2;{};{};{}m"

# END
END= PRE+"0m"


