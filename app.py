"""Flask app entrypoint."""
import sys
from pydocshost.run_app import run

if __name__ == "__main__":
    run(8000, *sys.argv[1:])
