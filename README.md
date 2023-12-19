<p align = "center">
  <img src = "https://github.com/toggysmith/airflow-thread-pool/assets/61121030/f83504e9-359e-4844-b55c-7d5425a9cd0b" width = "400px" height = "400px" />
</p>

# Airflow

Airflow is a C++ library for creating and managing thread-pools.

## API reference

Airflow's API is documented in the source code using Doxygen documentation comments. A HTML and Latex version of this API reference can be generated using the Python script located at `tools/generate-docs.py`. Doxygen must be installed and on the PATH as 'doxygen' for this script to work. This script generates the API reference in `docs/html` and `docs/latex`. The script also accepts an `--internal` flag which means that documentation for internal non-user-facing code will also be generated. Most users will not need this.

## Building examples

Airflow has several code examples located under `examples/`. These can be built manually by running `cmake -B build -DBUILD_EXAMPLES=ON` followed by `cmake --build build` in the root directory. An easier alternative is to use the `tools/build_examples.py` script. CMake must be installed and on the PATH for this script to work. The built examples will be under `build/examples/`.
