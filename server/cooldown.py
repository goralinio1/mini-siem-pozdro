from datetime import datetime

def should_emit(cache, host, alert_type, cooldown_seconds, now=None):
    now = now or datetime.now()
    key=(host,alert_type)
    previous=cache.get(key)
    if previous is not None and (now-previous).total_seconds() < cooldown_seconds:
        return False
    cache[key]=now
    return True
