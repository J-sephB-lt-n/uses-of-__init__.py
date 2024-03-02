from modules.reptile_creators.strange_reptiles import create_chameleon


def test_create_chameleon():
    assert create_chameleon() == "chameleon"
