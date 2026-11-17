cmake_minimum_required(VERSION 3.16)
project(AA_Laborator_Tema LANGUAGES CXX)

set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED ON)
set(CMAKE_CXX_EXTENSIONS OFF)

add_executable(AA_Laborator_Tema
    main.cpp
    src/Individ.cpp
    src/Populatie.cpp
    src/Helper.cpp
)

target_include_directories(AA_Laborator_Tema PRIVATE include)

# Optional convenience: make default sample input available in build folder.
file(COPY "${CMAKE_SOURCE_DIR}/data" DESTINATION "${CMAKE_BINARY_DIR}")
