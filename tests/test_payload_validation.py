import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parents[1] / "server"))
from app_sqlite import validate_payload

def test_missing_host():
    ok, message = validate_payload({"cpu":1,"ram":2,"disk":3})
    assert not ok and "host" in message

def test_metric_out_of_range():
    ok, _ = validate_payload({"host":"client","cpu":101,"ram":2,"disk":3})
    assert not ok
