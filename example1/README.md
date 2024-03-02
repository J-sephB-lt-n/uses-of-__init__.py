```bash
.
├── README.md
├── main.py
├── modules
│   ├── bird_creators
│   │   ├── __init__.py
│   │   ├── create_hadeda.py
│   │   └── create_starling.py
│   └── reptile_creators
│       ├── __init__.py
│       ├── long_reptiles
│       │   ├── __init__.py
│       │   └── create_snake.py
│       └── strange_reptiles
│           ├── __init__.py
│           └── create_chameleon.py
├── requirements.txt
└── tests
    ├── bird_creators
    │   ├── test_create_hadeda.py
    │   └── test_create_starling.py
    └── reptile_creators
        ├── test_create_chameleon.py
        └── test_create_snake.py
```

```python
# main.py

from modules import bird_creators, reptile_creators

if __name__ == "__main__":
    bird_creators.create_hadeda()
    bird_creators.create_starling()
    reptile_creators.create_chameleon()
    reptile_creators.create_snake()
```

Run entry script:
```bash
python main.py
```

Run tests:
```bash
python -m pytest
```
