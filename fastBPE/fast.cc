#include "fastBPE.hpp"
using namespace fastBPE;

extern "C" __declspec(dllexport) BPEApplyer* CreateBPE(const char* codes, const char* vocab) {
    return new BPEApplyer(codes, vocab);
}

extern "C" __declspec(dllexport) void DeleteBPE(BPEApplyer* bpe) {
    if (bpe != NULL) {
        delete bpe;
        bpe = NULL;
    }
}

extern "C" __declspec(dllexport) int ApplyBPE(BPEApplyer* bpe, const char* ins, char* buf, int bufsize) {
    std::string out = bpe->apply_str(ins);
    strcpy_s(buf, bufsize, out.c_str());
    return out.size()>bufsize? bufsize: out.size();
}