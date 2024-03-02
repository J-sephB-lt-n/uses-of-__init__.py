from modules.reptile_creators import create_chameleon


def test_create_chameleon():
    assert create_chameleon() == "chameleon"
