from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class single_string(_message.Message):
    __slots__ = ("single_string",)
    SINGLE_STRING_FIELD_NUMBER: _ClassVar[int]
    single_string: str
    def __init__(self, single_string: _Optional[str] = ...) -> None: ...

class empty(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class super_path(_message.Message):
    __slots__ = ("alpha_path",)
    ALPHA_PATH_FIELD_NUMBER: _ClassVar[int]
    alpha_path: str
    def __init__(self, alpha_path: _Optional[str] = ...) -> None: ...
