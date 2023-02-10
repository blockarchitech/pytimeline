# pytimline

Interface with Rebble's Timeline API via Python.


## Usage

Right now, it's only possible to push pins via pushPin:

```python
from pypebbletimeline.timeline import pushPin

    # valid times are:
    # 1 - Instant
    # 2 - In 30 min. (Timeline Subscription)
    # 3 - In 60 min. 
    # 4. - In 3 hours (Free)

print(pushPin('title','body','subtitle','1','token'))
```

## Install

```bash
$ pip install pypebbletimeline
Successfully installed pypebbletimeline-0.1.1
```

