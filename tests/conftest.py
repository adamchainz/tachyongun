from __future__ import annotations

import os
import sys
import time

# Isolate tests from the host machine’s timezone
os.environ["TZ"] = "UTC"
if hasattr(time, 'tzset'):  # Not available on Windows
    time.tzset()
