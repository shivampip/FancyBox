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

![Output Screenshot](/imgs/fancybox_messages.png)

* Box with title and description

![Table Screenshot](/imgs/fancybox_table.png)

