import setuptools

setuptools.setup(
    name="streamlit-toggle",
    version="1.0.0",
    author="Sam Dobson",
    author_email="1309834+samdobson@users.noreply.github.com",
    description="Toggle widget for Streamlit",
    long_description="",
    long_description_content_type="text/plain",
    url="https://github.com/samdobson/streamlit-toggle",
    packages=setuptools.find_packages(),
    include_package_data=True,
    classifiers=[],
    python_requires=">=3.6",
    install_requires=[
        "streamlit >= 0.63",
    ],
)
