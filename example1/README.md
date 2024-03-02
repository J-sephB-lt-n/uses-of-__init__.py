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
│       ├── create_chameleon.py
│       └── create_snake.py
├── requirements.txt
└── tests
    ├── bird_creators
    │   ├── test_create_hadeda.py
    │   └── test_create_starling.py
    └── reptile_creators
        ├── test_create_chameleon.py
        └── test_create_snake.py
```

Run entry script:
```bash
python main.py
```

Run tests:
```bash
python -m pytest
```

