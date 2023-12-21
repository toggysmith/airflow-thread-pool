file(GLOB_RECURSE TEST_SOURCES "*.cpp")

add_executable(test_runner ${TEST_SOURCES})

target_include_directories(test_runner PRIVATE "../include" "external")
