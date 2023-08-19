from pathlib import Path
from unittest     import TestCase

from xmlschema import XMLSchema

if __name__ == "__main__":
	print("ERROR: you called a testcase declaration file as an executable module.")
	print("Use: 'python -m unitest <testcase module>'")
	exit(1)


class SPIRIT(TestCase):
	_root: Path = Path("..")
