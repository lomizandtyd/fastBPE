import sys
from setuptools import setup, find_packages, Extension
from distutils.command.sdist import sdist as _sdist

try:
    from Cython.Build import cythonize
except ImportError:
    use_cython = False
else:
    use_cython = True


if use_cython:
    print("build under cython")
    extension = 'pyx'
else:
    extension = 'cpp'


if "linux" in sys.platform:
    extensions = [
        Extension(
            'fastBPE',
            [
                "fastBPE/fastBPE." + extension,
            ],
            language='c++',
            extra_compile_args=[
                "-O3",
                "-pthread",
                "-std=c++11"
            ],
        ),
    ]
else:
    print(sys.platform)
    extensions = [
        Extension(
            'fastBPE',
            [
                "fastBPE/fastBPE." + extension,
                "fastBPE/compat/mman.c"
            ],
            language='c++',
            extra_compile_args=[
                "/O2"
            ],
        ),
    ]

if use_cython:
    extensions = cythonize(extensions)


with open('README.md') as f:
    readme = f.read()


setup(
    name = 'fastBPE',
    version = '0.1.1',
    description = 'C++ implementation of Neural Machine Translation of Rare Words with Subword Units, with Python API.',
    url = 'https://github.com/glample/fastBPE',
    long_description = readme,
    long_description_content_type = 'text/markdown',
    ext_package = '',
    ext_modules = extensions,
    packages=[
        'fastBPE',
    ],
)
