"""Flask app entrypoint."""
import sys
import os
from pydocshost.run_app import run

if __name__ == "__main__":
    run(8000, *sys.argv[1:], **os.environ)
