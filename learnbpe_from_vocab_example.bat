SET bin=build\win32\fast.exe

echo "Create Codes Directly from Vocabulary Files."
SET ncodes=%1
SET vocabf=%2
SET codesf=%3
%bin% learnbpe_vocab %ncodes% %vocabf% > %codesf%
echo "Done."