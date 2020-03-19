cmake_minimum_required(VERSION 3.16)
project(thread_conan_test LANGUAGES C CXX)
add_library(Thread
    src/Thread.cpp)
target_include_directories(Thread PUBLIC "./include")