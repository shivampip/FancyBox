# FancyBox

Fancy Box is a Python module that allows you to print beautiful message boxes on command line. There are predefined message boxes, you can use or you can create you own custom box.


## Installation
```
pip3 install fancybox
```

## Uses
* Simple messages
```
import fancybox as fb

fb.success("Test Successful")
fb.error("IOError occured")
fb.info("Setup Completed")
fb.warning("name is NULL")
```

![Output Screenshot](https://github.com/shivampip/FirstPyPl/blob/master/imgs/fancybox_messages.png)

* Box with title and description
```
from fancybox import Box
box= Box()
box.makeboxwithheadbold(title, description)
```

![Table Screenshot](https://github.com/shivampip/FirstPyPl/blob/master/imgs/fancybox_table.png)

* Create customize box

```
from fancybox import Box
box= Box()
box.bgcolor= 2
box.fgcolor= 15
box.border= 11
box.makebox("NAMES")
box.addbox("Python")
box.addbox("Linux")
box.addbox("Windows")
```

![Custom box](https://github.com/shivampip/FirstPyPl/blob/master/imgs/custom_box.png)


**Happy Programming**