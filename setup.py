from setuptools import setup

def readme():
    with open('README.md') as f:
        README = f.read()
    return README


setup(
    name="quick_perf_tracer",
    version="1.0.0",
    description="Decodes the perfetto traces super fast",
    long_description=readme(),
    long_description_content_type="text/markdown",
    url="https://github.com/VivekKannaV/quick_perf_tracer",
    author="Vivek Kanna V",
    author_email="behappy.vivek@gmail.com",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
    ],
    packages=["quick_perf_tracer"],
    include_package_data=True,
    python_requires='>=3',
)
