import fancybox as fb

#https://unicode-table.com/en/#miscellaneous-symbols-and-pictographs

#fb.success("Test Successful")
#fb.error("IOError occured")
#fb.info("Setup Completed")
#fb.warning("name is NULL")


from fancybox import Box
box= Box()
box.bgcolor= 2
box.fgcolor= 15
box.border= 11
box.makebox("NAMES")
box.addbox("Python")
box.addbox("Linux")
box.addbox("Windows")