/* WETA_QUIET_HEADER_WARNINGS_IMPLEMENTATION=1.1 */
#if !defined(WETA_QHW_ALLOW_HEADER_WARNINGS_FOR_KIT_openimageio) && !defined(WETA_QHW_ALLOW_HEADER_WARNINGS)
#if defined(__clang__) && defined(__clang_major__)
#if (__clang_major__ >= 3)
#pragma clang system_header
#endif
#else
#if defined(__INTEL_COMPILER)
#if !defined(WETA_QHW_ALLOW_HEADER_WARNINGS_INTEL_FOR_KIT_openimageio) && !defined(WETA_QHW_ALLOW_HEADER_WARNINGS_INTEL)
#pragma system_header /* Note the following about "internal error": */
/* If the Intel Compiler fails with a message like this:
 *   internal error: assertion failed at: "shared/cfe/edgcpfe/preproc.c", line 4637
 * try setting one of these compiler options:
 *   -DWETA_QHW_ALLOW_HEADER_WARNINGS_INTEL_FOR_KIT_openimageio=1
 *   -DWETA_QHW_ALLOW_HEADER_WARNINGS_INTEL=1
 * to avoid this #pragma when using the Intel Compiler. */
#endif
#else
#if defined(__GNUC__) && defined(__GNUC_MINOR__)
#if (__GNUC__ == 4 && __GNUC_MINOR__ >= 1) || (__GNUC__ > 4)
#pragma GCC system_header
#endif
#endif
#endif
#endif
#endif

