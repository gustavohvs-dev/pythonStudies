#More modules: https://docs.python.org/3/py-modindex.html

from platform import platform, machine, processor, system, version, python_implementation, python_version_tuple
import os

print(platform())
print(platform(1))
print(platform(0, 1))
print(machine())
print(processor())
print(system())
print(version())
print(python_implementation())
print(python_version_tuple())

print(dir(os))