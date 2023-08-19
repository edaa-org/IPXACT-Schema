from pathlib import Path
from unittest     import TestCase

from xmlschema import XMLSchema

if __name__ == "__main__":
	print("ERROR: you called a testcase declaration file as an executable module.")
	print("Use: 'python -m unitest <testcase module>'")
	exit(1)


class SPIRIT(TestCase):
	_root: Path = Path("..")

	def test_Schema10(self):
		print()
		print(f"CWD:              {Path.cwd()}")

		directory = self._root / "ipxact-1.0"
		print(f"Schema directory: {directory}")

		schemaFiles = (
			"design.xsd",
			"pmd.xsd",
			"component.xsd",
			"busDefinition.xsd",
			"generator.xsd",
			"configurator.xsd",
			"looseGeneratorInvocation.xsd",
		)
		print(f"Reading schemas ...")
		for file in schemaFiles:
			schemaFile = directory / file
			print(f"  {schemaFile}")
			_ = XMLSchema(schemaFile)

	def test_Schema11(self):
		print()
		print(f"CWD:              {Path.cwd()}")

		directory = self._root / "ipxact-1.1"
		print(f"Schema directory: {directory}")

		schemaFiles = (
			"design.xsd",
			"pmd.xsd",
			"component.xsd",
			"busDefinition.xsd",
			"generator.xsd",
			"configurator.xsd",
			"looseGeneratorInvocation.xsd",
		)
		print(f"Reading schemas ...")
		for file in schemaFiles:
			schemaFile = directory / file
			print(f"  {schemaFile}")
			_ = XMLSchema(schemaFile)

	def test_Schema12(self):
		print()
		print(f"CWD:              {Path.cwd()}")

		directory = self._root / "ipxact-1.2"
		print(f"Schema directory: {directory}")

		schemaFiles = (
			"design.xsd",
			"pmd.xsd",
			"component.xsd",
			"busDefinition.xsd",
			"generator.xsd",
			"configurator.xsd",
			"looseGeneratorInvocation.xsd",
		)
		print(f"Reading schemas ...")
		for file in schemaFiles:
			schemaFile = directory / file
			print(f"  {schemaFile}")
			_ = XMLSchema(schemaFile)

	def test_Schema14(self):
		print()
		print(f"CWD:              {Path.cwd()}")

		directory = self._root / "ipxact-1.4"
		print(f"Schema directory: {directory}")

		schemaFiles = (
			"design.xsd",
			"component.xsd",
			"busDefinition.xsd",
			"generator.xsd",
		)
		print(f"Reading schemas ...")
		for file in schemaFiles:
			schemaFile = directory / file
			print(f"  {schemaFile}")
			_ = XMLSchema(schemaFile)

	def test_Schema15(self):
		print()
		print(f"CWD:              {Path.cwd()}")

		directory = self._root / "ipxact-1.5"
		print(f"Schema directory: {directory}")

		schemaFiles = (
			"design.xsd",
			"component.xsd",
			"busDefinition.xsd",
			"generator.xsd",
		)
		print(f"Reading schemas ...")
		for file in schemaFiles:
			schemaFile = directory / file
			print(f"  {schemaFile}")
			_ = XMLSchema(schemaFile)
