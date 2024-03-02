from modules.bird_creators import create_starling


def test_create_starling():
    assert create_starling() == "starling" 
