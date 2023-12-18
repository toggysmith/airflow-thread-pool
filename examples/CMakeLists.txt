message(STATUS "Examples included.")

set(AIRFLOW_EXAMPLE_SOURCE_FILES
    "example-1.cpp"
    "example-2.cpp"
)

string(REPLACE ".cpp" "" AIRFLOW_EXAMPLE_EXECUTABLE_NAMES "${AIRFLOW_EXAMPLE_SOURCE_FILES}")

foreach(name ${AIRFLOW_EXAMPLE_EXECUTABLE_NAMES})
    add_executable(${name} ${name}.cpp)
endforeach()

foreach(name ${AIRFLOW_EXAMPLE_EXECUTABLE_NAMES})
    target_link_libraries(${name} PRIVATE airflow)
    target_include_directories(${name} PRIVATE "../../include")
endforeach()
