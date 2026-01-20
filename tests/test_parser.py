import tempfile
from parser import parse_log_file

def test_parse_log_file_basic():
    log_content = """2026-01-12 14:33:01 ERROR Something failed
INVALID LINE
2026-01-12 14:33:02 INFO All good
"""

    with tempfile.NamedTemporaryFile(mode="w+", delete=False) as temp_log:
        temp_log.write(log_content)
        temp_log_path = temp_log.name

    valid_levels = ["ERROR", "WARNING", "INFO"]

    entries, malformed_count = parse_log_file(
        temp_log_path,
        valid_levels
    )

    assert entries == ["ERROR", "INFO"]
    assert malformed_count == 1
