project(thread_conan_test LANGUAGE C CXX VERSION 1.0)
add_library(Thread PUBLIC
    src/Thread.cpp)
target_include_directories(Thread PUBLIC "./include")