# Minimal Example for Spark Related Version Query Bug
Minimal example that reproduces a [version-query bug](https://github.com/mbdevpl/version-query/issues/7), that
occurs when the library is invoked from within wheel package in a Spark job.

## Prerequisites
* Python-3.6 or newer
* Apache Spark 2.4.x or newer (no cluster needed - a local installation works fine)
* Bash


## How to Reproduce the Issue
1. Open a shell
1. `cd $projectRoot` (go to project root)
1. `python3 -m venv venv` (create virtual environment)
1. `source venv/bin/activate` (activate virtual environment)
1. `pip install -r requirements.txt` (install dependencies)
1. `python setup.py bdist_wheel` (build whl package)
1. `tar czf venv.tar.gz venv` (pack virtual environment into archive)
1. `cd run` (go to the run directory)
1. `./run.bash` (execute run.bash)

Executing these commands results in
```
Traceback (most recent call last):
  File "/project/root/run/run.py", line 4, in <module>
    print(f"Running version {some_module.get_version()}")
  File "/project/root/dist/reproduce_version_query_spark_issue-0.1.0.dev1+bfcaa08b-py3-none-any.whl/some_module.py", line 5, in get_version
  File "/project/root/venv/lib/python3.7/site-packages/version_query/query.py", line 96, in predict_version_str
    return predict_caller(2).to_str()
  File "/project/root/venv/lib/python3.7/site-packages/version_query/query.py", line 81, in predict_caller
    here = _caller_folder(stack_level + 1)
  File "/project/root/venv/lib/python3.7/site-packages/version_query/query.py", line 22, in _caller_folder
    assert here.is_file(), here
AssertionError: /project/root/dist/reproduce_version_query_spark_issue-0.1.0.dev1+bfcaa08b-py3-none-any.whl/some_module.py
```