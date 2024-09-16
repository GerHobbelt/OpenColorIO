# SPDX-License-Identifier: BSD-3-Clause
# Copyright Contributors to the OpenColorIO Project.

set(SOURCES
    main.cpp
)

add_executable(ocioperf ${SOURCES})

set_target_properties(ocioperf PROPERTIES
    COMPILE_FLAGS "${PLATFORM_COMPILE_FLAGS}")

# Weta FX Customization: Suppress some annoying warnings:
target_compile_options(ocioperf PRIVATE
  -Wno-abi
  )

target_link_libraries(ocioperf
    PRIVATE
        apputils
        OpenColorIO
        utils::strings
)

install(TARGETS ocioperf
    RUNTIME DESTINATION ${CMAKE_INSTALL_BINDIR}
)
