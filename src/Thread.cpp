#include "Thread.h"

Thread::Thread()
{
    printf("Thread instance was created");
}
void Thread::start()
{
    printf("Thread instance has started");
}
void Thread::wait()
{
    printf("Waiting for thread...");
}
void Thread::detach()
{
    printf("Detaching !");
}
bool Thread::is_joinable()
{
    return true;
}

Thread::~Thread()
{
    printf("Thread instance was destructed");
}