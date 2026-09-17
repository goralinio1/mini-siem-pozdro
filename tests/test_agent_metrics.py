import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parents[1] / "agent"))
from agent import collect_metrics

def test_metrics_shape():
    data=collect_metrics()
    assert set(data)=={"host","cpu","ram","disk"}
    assert data["host"]
    assert all(0 <= data[k] <= 100 for k in ("cpu","ram","disk"))
