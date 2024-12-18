from typing import TypeVar

DataType = TypeVar("DataType")

class _DefaultHandler:
	def __call__(self, dtype: type[DataType]=object) -> DataType | None:
		if issubclass(dtype, int): return 0 # covers false as well
		if dtype == float: return 0.0
		if dtype == complex: return complex()
		if dtype == str: return ""
		if dtype == list: return []
		if dtype == set: return set()
		if dtype == dict: return {}

		return None
	
	def __get__(self): return self()

	def __getitem__(self, dtype: type[DataType]) -> DataType: return self(dtype)

default = _DefaultHandler()