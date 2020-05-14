@call "C:\Program Files (x86)\Microsoft Visual Studio\2017\Enterprise\VC\Auxiliary\Build\vcvars64.bat"
mkdir build\win32\objs

cl /c /EHsc fastBPE\compat\mman.c /Fobuild\win32\objs\mman.obj 
cl /c /EHsc fastBPE\main.cc /IfastBPE /Fobuild\win32\objs\main.obj
cl /c /EHsc fastBPE\fast.cc /IfastBPE /Fobuild\win32\objs\fast.obj

::cl /c /EHsc fastBPE\fastBPE.hpp /IfastBPE /Fobuild\win32\objs\fastbpe.obj

link build\win32\objs\mman.obj build\win32\objs\main.obj /OUT:build\win32\fast.exe
link /DLL build\win32\objs\mman.obj build\win32\objs\fast.obj /OUT:build\win32\fast.dll

::cd fastBPE && cl /Fofast.exe /EHsc main.cc compat\mman.c && cd .
