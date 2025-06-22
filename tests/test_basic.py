from courseclicker.main import load_position

def test_position_format():
    pos = load_position()
    assert hasattr(pos, "x") and hasattr(pos, "y")