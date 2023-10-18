import ctypes
lib = ctypes.cdll.LoadLibrary('./libperson.so')

class Person(object):
    def __init__(self, age):
        lib.Person_new.argtypes = [ctypes.c_int]
        lib.Person_new.restype = ctypes.c_void_p
        lib.Person_get.argtypes = [ctypes.c_void_p]
        lib.Person_get.restype = ctypes.c_int
        lib.Person_set.argtypes = [ctypes.c_void_p,ctypes.c_int]
        lib.Person_delete.argtypes = [ctypes.c_void_p]
        lib.Person_fib.argtypes = [ctypes.c_void_p]  #new line
        lib.Person_fib.restype = ctypes.c_int  #new line
        self.obj = lib.Person_new(age)

    def get(self):
        return lib.Person_get(self.obj)

    def set(self, age):
        lib.Person_set(self.obj, age)

    def fib(self):  #new method
        return lib.Person_fib(self.obj)  #call the new C function
    
    def __del__(self):
        return lib.Person_delete(self.obj)