from distutils.core import setup
from distutils.extension import Extension
from Cython.Distutils import build_ext
ext_modules = [
    Extension("task_2_subprocess_c",  ["task_2_subprocess.py"]),

#   ... all your modules that need be compiled ...
]
setup(
    name = 'My Program Name',
    cmdclass = {'build_ext': build_ext},
    ext_modules = ext_modules
)