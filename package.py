##################################################
##################################################
# Building OCIO and OIIO:
#
# Order of building:
# 1) OCIO (core): no apps (CLI utilities)
# 2) OIIO: against OCIO (core)
# 3) OCIO (full): with apps
#
# The reason is that OIIO requires OCIO and OCIO CLI tools require OIIO.
#
# Both 'core' and 'full' OCIO builds will come from the same repo, but from different
# branches:
#     branch: rez-vX.X.X (core)
#     branch: rez-vX.X.X-tools (full)
#
# Once released, 2 different REZ packages will be available: "ocio" and "ocio_tools"
##################################################
##################################################

# name = "ocio"
name = "ocio_tools"

version = "2.1.3.hh.1.0.0"

authors = [
    "AcademySoftwareFoundation",
]

description = """Color management libraries and tools"""

with scope("config") as c:
    import os

    c.release_packages_path = os.environ["HH_REZ_REPO_RELEASE_EXT"]


@early()
def requires():
    if this.name == "ocio":
        return [
            "glew",
            "libexpat",
            "pybind11",
            "imath",
        ]
    elif this.name == "ocio_tools":
        return [
            "glew",
            "libexpat",
            "pybind11",
            "imath",
            "lcms",
            "oiio",
        ]
    else:
        raise ValueError("Wrong package name")


private_build_requires = []

variants = [
    ["python-3.7"],
    ["python-3.9"],
    ["python-3.10"],
    ["python-3.11"],
    ["python-3.12"],
]


def commands():
    env.REZ_OCIO_ROOT = "{root}"
    env.OCIO_ROOT = "{root}"
    env.OCIO_LOCATION = "{root}"
    env.OCIO_INCLUDE_DIR = "{root}/include"
    env.OCIO_LIBRARY_DIR = "{root}/lib64"

    env.PATH.append("{root}/bin")
    env.LD_LIBRARY_PATH.append("{root}/lib64")

    if building:
        env.CMAKE_MODULE_PATH.append("{root}/lib64/cmake/OpenColorIO")

    if "python" in resolve:
        python_ver = resolve["python"].version
        if python_ver.major == 3:
            if python_ver.minor == 7:
                env.PYTHONPATH.append("{root}/lib64/python3.7/site-packages")
            elif python_ver.minor == 9:
                env.PYTHONPATH.append("{root}/lib64/python3.9/site-packages")
            elif python_ver.minor == 10:
                env.PYTHONPATH.append("{root}/lib64/python3.10/site-packages")
            elif python_ver.minor == 11:
                env.PYTHONPATH.append("{root}/lib64/python3.11/site-packages")
            elif python_ver.minor == 12:
                env.PYTHONPATH.append("{root}/lib64/python3.12/site-packages")


uuid = "repository.OpenColorIO"
