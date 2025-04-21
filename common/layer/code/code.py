from enum import Enum


class Code(Enum):
	OK = "00"
	DO_NOTHING = "FF"
	ARGUMENT_ERROR = "01"
	UNEXPECTED_BEHAVIOR = "02"
