from modules.bird_creators import create_hadeda


def test_create_hadeda():
    assert create_hadeda() == "hadeda" 
