# Python Coding Style Guide

## General
* Write clear and readable code.
* Use vertical and horizontal spaces generally.
* Minimise the use of abbreviations and shortened words.
* Be explicit and build your own functions if possible.
* Consider not using functions if not clear how it works internally.

## Examples

### File Names
```
GraphicsHandler.py (contains a class called GraphicsHandler)
IWorkloadFactory.py (interface)
etc.
```

### Class Names
``` Python
ListGenerator
CommandImplementation
AIControllerBase
```

### Variable Names
``` Python
count # not 'cnt'
savedIndex # not 'savedIdx'
maximum or max # widely used and the shortened form is are acceptable
```

### Constant Names
``` Python
MAX_ARRAY_LENGTH
CLICK_LIMIT_PER_SECOND

```

### Function Names
``` Python
readFromFile()
updateIfRequired()
getDefaultSound()
```

### Iterative Variables
``` Python
# 'i' is used for the indices. 'i' is better than 'n' in this case.
for i in range(11): 
    sum += arr[i]
    
# 'n' is used for the data. 'n' is better than 'i' in this case.
for n in arr:
    print(n)
```

### More to come...
maybe not