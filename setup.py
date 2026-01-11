# ReEzSynth/setup.py
import os

from setuptools import setup
from torch.utils.cpp_extension import BuildExtension, CUDAExtension

# Compiler flags (platform-specific)
is_msvc = os.name == "nt"
if is_msvc:
    # MSVC-compatible flags
    CXX_FLAGS = [
        "/O2",
        "/std:c++17",
        "/openmp",
        "/EHsc",
        "/DNOMINMAX",
        "/D_ENABLE_EXTENDED_ALIGNED_STORAGE",
        "/MP",
        "/permissive-",
        "/Zc:__cplusplus",
        "/D_WIN32",
        "/DUSE_CUDA",
    ]
    NVCC_FLAGS = [
        "-O3",
        "-std=c++17",
        "-U__CUDA_NO_HALF_OPERATORS__",
        "-U__CUDA_NO_HALF_CONVERSIONS__",
        "--use_fast_math",
        "--threads=8",
        "-Xptxas=-v",
        "-diag-suppress=174",
        # Host compiler flags for MSVC
        "-Xcompiler",
        "/DWIN32",
        "-Xcompiler",
        "/DUSE_CUDA",
    ]
else:
    # GCC/Clang flags (Linux/macOS)
    CXX_FLAGS = ["-g", "-O3", "-fopenmp", "-lgomp", "-std=c++17", "-DENABLE_BF16"]
    NVCC_FLAGS = [
        "-O3",
        "-std=c++17",
        "-U__CUDA_NO_HALF_OPERATORS__",
        "-U__CUDA_NO_HALF_CONVERSIONS__",
        "--use_fast_math",
        "--threads=8",
        "-Xptxas=-v",
        "-diag-suppress=174",
    ]

setup(
    name="ebsynth_torch",
    ext_modules=[
        CUDAExtension(
            name="ebsynth_torch",
            sources=[
                "ebsynth_extension/ext.cpp",
                "ebsynth_extension/dispatch.cu",
                "ebsynth_extension/kernels.cu",
                "ebsynth_extension/integral_image.cu",
            ],
            extra_compile_args={"cxx": CXX_FLAGS, "nvcc": NVCC_FLAGS},
            extra_link_args=([] if is_msvc else ["-lcuda"]),
        ),
    ],
    cmdclass={"build_ext": BuildExtension},
)
