# from namespace_package.package1 import add_stuff
# from namespace_package.package1.module_a import add_stuff
from namespace_package.package1.subpackage1 import add_stuff


def doit() -> int:
    return add_stuff(2, 2)
