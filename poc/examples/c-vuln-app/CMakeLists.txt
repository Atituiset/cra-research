cmake_minimum_required(VERSION 3.16)
project(c_vuln_app C)

# The PoC pipeline consumes this compilation database (Joern c2cpg / CodeQL).
set(CMAKE_EXPORT_COMPILE_COMMANDS ON)

# Vendored zlib 1.2.12 — CVE-2022-37434 (last affected release).
add_subdirectory(third_party/zlib)

add_executable(c-vuln-app main.c)
target_include_directories(c-vuln-app PRIVATE third_party/zlib ${CMAKE_CURRENT_BINARY_DIR}/third_party/zlib)
target_link_libraries(c-vuln-app PRIVATE zlibstatic)
