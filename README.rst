Django Flags
============


django-flags offers an easy interface for integrating and controlling flags for rapid experimentation and development.

Basic Operation
---------------
To use a flag you must first define it in a flag config file. This is a JSON file with the following structure
```
[
  {
    "name": "flag1",
    "flag_type": "int",
    "default_value": 0
  }
]
```

Once defined flags can be accesesed from python code by:

```
from flags.utils import get_flag_value
get_flag_value('flag1', **kwargs) # returns 0
```

Can take arbitrary keyword arguments that can override the value of the flag.

To change a flag to use something other than the default value use a FlagOverrider. By default flags comes with a single overrider SiteFlagOverrider. This will look in the django database for any SiteFlagOverrides and apply those values instead of the default value.


API
---
