import common.common as cmn
import ctypes


def init():
    ENABLE_PROCESSED_OUTPUT = 0x0001
    ENABLE_WRAP_AT_EOL_OUTPUT = 0x0002
    ENABLE_VIRTUAL_TERMINAL_PROCESSING = 0x0004
    MODE = ENABLE_PROCESSED_OUTPUT + ENABLE_WRAP_AT_EOL_OUTPUT + ENABLE_VIRTUAL_TERMINAL_PROCESSING
    kernel32 = ctypes.windll.kernel32
    handle = kernel32.GetStdHandle(-11)
    kernel32.SetConsoleMode(handle, MODE)


def LOG(text: str):
    if cmn.DEBUG_FLAG:
        print("[DEBUG] "+text)


def ERROR_LOG(text: str):
    if cmn.DEBUG_FLAG:
        print("\033[31m[ERROR]\033[0m" + text)
