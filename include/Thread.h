#include <cstdio>

class Thread
{
public:
    Thread();
    void start();
    void wait();
    void detach();
    bool is_joinable();
    ~Thread();
};