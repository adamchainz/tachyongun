import os
import time

# Isolate tests from the host machine’s timezone
os.environ["TZ"] = "UTC"
time.tzset()
