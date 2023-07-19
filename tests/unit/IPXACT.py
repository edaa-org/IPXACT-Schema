from pathlib import Path
from unittest     import TestCase

from xmlschema import XMLSchema

if __name__ == "__main__":
	print("ERROR: you called a testcase declaration file as an executable module.")
	print("Use: 'python -m unitest <testcase module>'")
	exit(1)


class SPIRIT(TestCase):
	_root: Path = Path("../..")

	def test_Schema10(self):
		directory = self._root / "ipxact-1.0"

		schemaFiles = (
			"design.xsd",
			"pmd.xsd",
			"component.xsd",
			"busDefinition.xsd",
			"generator.xsd",
			"configurator.xsd",
			"looseGeneratorInvocation.xsd",
		)
		for schemaFile in schemaFiles:
			_ = XMLSchema(directory / schemaFile)

	def test_Schema11(self):
		directory = self._root / "ipxact-1.1"

		schemaFiles = (
			"design.xsd",
			"pmd.xsd",
			"component.xsd",
			"busDefinition.xsd",
			"generator.xsd",
			"configurator.xsd",
			"looseGeneratorInvocation.xsd",
		)
		for schemaFile in schemaFiles:
			_ = XMLSchema(directory / schemaFile)

	def test_Schema12(self):
		directory = self._root / "ipxact-1.2"

		schemaFiles = (
			"design.xsd",
			"pmd.xsd",
			"component.xsd",
			"busDefinition.xsd",
			"generator.xsd",
			"configurator.xsd",
			"looseGeneratorInvocation.xsd",
		)
		for schemaFile in schemaFiles:
			_ = XMLSchema(directory / schemaFile)

	def test_Schema14(self):
		directory = self._root / "ipxact-1.4"

		schemaFiles = (
			"design.xsd",
			"component.xsd",
			"busDefinition.xsd",
			"generator.xsd",
		)
		for schemaFile in schemaFiles:
			_ = XMLSchema(directory / schemaFile)

	def test_Schema15(self):
		directory = self._root / "ipxact-1.5"

		schemaFiles = (
			"design.xsd",
			"component.xsd",
			"busDefinition.xsd",
			"generator.xsd",
		)
		for schemaFile in schemaFiles:
			_ = XMLSchema(directory / schemaFile)


class IEEE_1685(TestCase):
	_root: Path = Path("../..")
	
	def test_Schema2009(self):
		directory = self._root / "ieee-1685-2009"

		schemaFiles = (
			"design.xsd",
			"component.xsd",
			"busDefinition.xsd",
			"generator.xsd",
		)
		for schemaFile in schemaFiles:
			_ = XMLSchema(directory / schemaFile)

	def test_Schema2014(self):
		directory = self._root / "ieee-1685-2014"

		schemaFiles = (
			"design.xsd",
			"component.xsd",
			"busDefinition.xsd",
			"generator.xsd",
		)
		for schemaFile in schemaFiles:
			_ = XMLSchema(directory / schemaFile)

	def test_Schema2022(self):
		directory = self._root / "ieee-1685-2022"

		schemaFiles = (
			"design.xsd",
			"component.xsd",
			"busDefinition.xsd",
			"generator.xsd",
		)
		for schemaFile in schemaFiles:
			_ = XMLSchema(directory / schemaFile)
