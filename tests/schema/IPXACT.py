from pathlib import Path
from unittest     import TestCase

from xmlschema import XMLSchema

if __name__ == "__main__":
	print("ERROR: you called a testcase declaration file as an executable module.")
	print("Use: 'python -m unitest <testcase module>'")
	exit(1)


class SPIRIT(TestCase):
	def test_Schema10(self):
		schema = XMLSchema(Path("../../ipxact-1.0/design.xsd"))

	def test_Schema11(self):
		schema = XMLSchema(Path("../../ipxact-1.1/design.xsd"))

	def test_Schema12(self):
		schema = XMLSchema(Path("../../ipxact-1.2/design.xsd"))

	def test_Schema14(self):
		schema = XMLSchema(Path("../../ipxact-1.4/design.xsd"))

	def test_Schema15(self):
		schema = XMLSchema(Path("../../ipxact-1.5/design.xsd"))


class IEEE_1685(TestCase):
	def test_Schema2009(self):
		schema = XMLSchema(Path("../../ieee-1685-2009/design.xsd"))

	def test_Schema2014(self):
		schema = XMLSchema(Path("../../ieee-1685-2014/design.xsd"))

	def test_Schema2022(self):
		schema = XMLSchema(Path("../../ieee-1685-2022/design.xsd"))
