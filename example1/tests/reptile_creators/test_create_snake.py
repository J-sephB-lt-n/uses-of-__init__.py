from modules.reptile_creators.long_reptiles import create_snake


def test_create_snake():
    assert create_snake() == "snake" 
