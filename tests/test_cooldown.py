import sys
from datetime import datetime, timedelta
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parents[1] / "server"))
from cooldown import should_emit

def test_cooldown_blocks_duplicate():
    cache={}
    now=datetime(2026,9,17,12,0,0)
    assert should_emit(cache,"client","HIGH_CPU",60,now)
    assert not should_emit(cache,"client","HIGH_CPU",60,now+timedelta(seconds=30))
    assert should_emit(cache,"client","HIGH_CPU",60,now+timedelta(seconds=61))
