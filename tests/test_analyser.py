from analyser import count_levels

def test_count_levels_basic():
    entries = ["ERROR", "ERROR", "WARNING", "INFO"]

    result = count_levels(entries)

    assert result["ERROR"] == 2
    assert result["WARNING"] == 1
    assert result["INFO"] == 1
