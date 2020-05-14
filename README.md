
# fastBPE-win

Ugly add win-x64 support for fastBPE. It could also be compiled under linux.

## Thanks
Fix compat by [klauspost's mman project](https://github.com/klauspost/mman-win32) and [AShelly's unistd.h](https://stackoverflow.com/a/826027/5557571).

## Release (windows)
```
# clone the repository
git clont https://github.com/lomizandtyd/fastBPE

# run CLI: dist\fast.exe

# install python package
python.exe -m easy_install dist\fastBPE-0.1.1-py3.7-win-amd32.egg
```

## Build for yourself (windows)
Need Visual Studio installed.

1. Clone the project and cd the top directory
2. Change the path of `vcvars64.bat` in `build_win32.bat` to your VS install path.
3. Open cmd and run `build_win32.bat`, you'll get the executable `fast.exe` at `build\win32\fast.exe`.

## Updates
1. Add support for learn bpe directly from vocabulary count.
2. Change the separator of infile/outfile to TAB `\t`.
3. Add support for large file in win64, re-compile codes with `//change readTextSlow -> readText; readText -> other dummy name`
4. Add DLL export for C#.

------------------------------
# copy from original repository
-------------------------------

# fastBPE

C++ implementation of [Neural Machine Translation of Rare Words with Subword Units](https://arxiv.org/abs/1508.07909), with Python API.

## Installation

Compile with:
```
g++ -std=c++11 -pthread -O3 fastBPE/main.cc -IfastBPE -o fast
```

## Usage:

### List commands
```
./fast
usage: fastbpe <command> <args>

The commands supported by fastBPE are:

getvocab input1 [input2]             extract the vocabulary from one or two text files
learnbpe nCodes input1 [input2]      learn BPE codes from one or two text files
learnbpe_vocab nCodes vocab          learn BPE codes directly from vocabulary files
applybpe output input codes [vocab]  apply BPE codes to a text file
applybpe_stream codes [vocab]        apply BPE codes to stdin and outputs to stdout
```

fastBPE also supports stdin inputs. For instance, these two commands are equivalent:
```
./fast getvocab text > vocab
cat text | ./fast getvocab - > vocab
```
But the first one will memory map the input file to read it efficiently, which can be more than twice faster than stdin on very large files. Similarly, these two commands are equivalent:
```
./fast applybpe output input codes vocab
cat input | ./fast applybpe_stream codes vocab > output
```
Although the first one will be significantly faster on large datasets, as it uses multi-threading to pre-compute the BPE splits of all words in the input file.

### Learn codes
```
./fast learnbpe 40000 train.de train.en > codes
```

### Apply codes to train
```
./fast applybpe train.de.40000 train.de codes
./fast applybpe train.en.40000 train.en codes
```

### Get train vocabulary
```
./fast getvocab train.de.40000 > vocab.de.40000
./fast getvocab train.en.40000 > vocab.en.40000
```

### Apply codes to valid and test
```
./fast applybpe valid.de.40000 valid.de codes vocab.de.40000
./fast applybpe valid.en.40000 valid.en codes vocab.en.40000
./fast applybpe test.de.40000  test.de  codes vocab.de.40000
./fast applybpe test.en.40000  test.en  codes vocab.en.40000
```

## Python API

To install the Python API, simply run:
```bash
python setup.py install
```

**Note:** For Mac OSX Users, add `export MACOSX_DEPLOYMENT_TARGET=10.x` (x=9 or 10, depending on your version) or `-stdlib=libc++` to the `extra_compile_args` of `setup.py` before/during the above install command, as appropriate.

Call the API using:

```python
import fastBPE

bpe = fastBPE.fastBPE(codes_path, vocab_path)
bpe.apply(["Roasted barramundi fish", "Centrally managed over a client-server architecture"])

>> ['Ro@@ asted barr@@ am@@ un@@ di fish', 'Centr@@ ally managed over a cli@@ ent-@@ server architecture']
```
