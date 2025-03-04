def print_exception_hierarchy(exception_class, indent=0):
    print(' ' * indent + exception_class.__name__)
    for subclass in exception_class.__subclasses__():
        print_exception_hierarchy(subclass, indent + 4)

# Imprimir la jerarquía comenzando desde la clase base Exception
print_exception_hierarchy(Exception)
# Exception
#     TypeError
#     StopAsyncIteration
#     StopIteration
#     ImportError
#         ModuleNotFoundError
#         ZipImportError
#     OSError
#         ConnectionError
#             BrokenPipeError
#             ConnectionAbortedError
#             ConnectionRefusedError
#             ConnectionResetError
#         BlockingIOError
#         ChildProcessError
#         FileExistsError
#         FileNotFoundError
#         IsADirectoryError
#         NotADirectoryError
#         InterruptedError
#         PermissionError
#         ProcessLookupError
#         TimeoutError
#         UnsupportedOperation
#     EOFError
#     RuntimeError
#         RecursionError
#         NotImplementedError
#         _DeadlockError
#     NameError
#         UnboundLocalError
#     AttributeError
#     SyntaxError
#         IndentationError
#             TabError
#     LookupError
#         IndexError
#         KeyError
#         CodecRegistryError
#     ValueError
#         UnicodeError
#             UnicodeEncodeError
#             UnicodeDecodeError
#             UnicodeTranslateError
#         UnsupportedOperation
#     AssertionError
#     ArithmeticError
#         FloatingPointError
#         OverflowError
#         ZeroDivisionError
#     SystemError
#         CodecRegistryError
#     ReferenceError
#     MemoryError
#     BufferError
#     Warning
#         UserWarning
#         EncodingWarning
#         DeprecationWarning
#         PendingDeprecationWarning
#         SyntaxWarning
#         RuntimeWarning
#         FutureWarning
#         ImportWarning
#         UnicodeWarning
#         BytesWarning
#         ResourceWarning