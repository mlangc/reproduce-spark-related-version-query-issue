import version_query
from setuptools import setup

setup(
    name="reproduce_version_query_spark_issue",
    version=version_query.predict_version_str(),
    description="Reproduces a version-query bug",
    py_modules=["some_module"],
    python_requires=">=3.6",
    install_requires=["version-query"],
    setup_requires=["version-query"],
)
