from .box import Box

#https://unicode-table.com/en/#miscellaneous-symbols-and-pictographs
# 🌲


def success(text):
    box= Box()
    box.fgcolor= 16
    box.bgcolor= 82
    box.border= 16
    box.makebox(text)


def error(text):
    box= Box()
    box.fgcolor= 16
    box.bgcolor= 9
    box.border= 16
    box.makebox(text)


def info(text):
    box= Box()
    box.fgcolor= 16
    box.bgcolor= 38
    box.border= 16
    box.makebox(text)


def warning(text):
    box= Box()
    box.fgcolor= 16
    box.bgcolor= 220
    box.border= 16
    box.makebox(text)

