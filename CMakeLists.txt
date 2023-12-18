cmake_minimum_required(VERSION 3.20)

project(airflow LANGUAGES CXX)

option(BUILD_EXAMPLES "Build examples." OFF)

set(CMAKE_CXX_STANDARD 11)
set(CMAKE_CXX_STANDARD_REQUIRED ON)
set(CMAKE_EXPORT_COMPILE_COMMANDS ON)

file(GLOB_RECURSE AIRFLOW_SOURCES "src/*.cpp")

add_library(airflow ${AIRFLOW_SOURCES})

target_include_directories(airflow PRIVATE "include")

if(BUILD_EXAMPLES)
    add_subdirectory("examples")
endif()
