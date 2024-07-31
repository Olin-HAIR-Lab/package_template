from setuptools import setup

package_name = "my_package"
submodules = "my_package/submodules"

setup(
    name=package_name,
    version="0.0.0",
    packages=[package_name, submodules],
    data_files=[
        ("share/ament_index/resource_index/packages", ["resource/" + package_name]),
        ("share/" + package_name, ["package.xml"]),
        ('share/' + package_name, ['launch/launch_my_package.py']),
    ],
    install_requires=["setuptools"],
    zip_safe=True,
    maintainer="YOUR_NAME",
    maintainer_email="EMAIL",
    description="Package description here",
    license="MIT License",
    tests_require=["pytest"],
    entry_points={
        "console_scripts": [
            "run_my_node = my_package.my_node:main"
        ],
    },
)
