import setuptools
from setuptools.command import build_py
import distutils
import os
import subprocess
import distutils.core

from distutils.core import setup
from distutils.command.install_data import install_data


with open("README.md", "r") as fh:
    long_description = fh.read()


class BuildReact(distutils.cmd.Command):
    """A custom command to run Pylint on all Python source files."""

    description = "Build the client react app"
    user_options = []

    def initialize_options(self):
        """Set default values for options."""
        # Each user option must be listed here with their default value.
        pass

    def finalize_options(self):
        """Post-process options."""
        pass

    def run(self):
        """Run command."""
        command = ["./build.sh"]
        command.append(os.getcwd())
        self.announce(
            "Running command: %s" % str(command),
            level=distutils.log.INFO)
        subprocess.check_call(command)


class BuildPyCommand(build_py.build_py):
    """Run prebuild steps."""

    def run(self):
        self.run_command("build_client")
        build_py.build_py.run(self)


setuptools.setup(
    name="pydocshost",
    version="0.1.1",
    author="Sam Bland",
    author_email="sblandcouk@gmail.com",
    description="Python docs api and frontend",
    python_requires=">=3.8",
    cmdclass={
        "build_client": BuildReact,
        "build_py": BuildPyCommand,
    },
    setup_requires=[
        "pytest-cov",
        "pytest-runner",
        "snapshottest"
    ],
    tests_require=["pytest"],
    extras_require={"test": ["pytest", "pytest-mock"]},
    install_requires=["flask"],
    packages=setuptools.find_packages(),
    package_dir={"pydocshost": "pydocshost", "pydocshost.app": "app"},
    include_package_data=True,
    classifiers=[
        "Programming Language :: Python :: 3.8",
        "Operating System :: OS Independent",
    ],
)
