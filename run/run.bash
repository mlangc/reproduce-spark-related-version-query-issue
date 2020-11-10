#!/usr/bin/env bash

spark-submit --master local \
  --py-files ../dist/reproduce_version_query_spark_issue-*.whl \
  --archives venv.tar.gz#PY_ENV \
  --conf spark.pyspark.python="./PY_ENV/venv/bin/python3" \
  --conf spark.pyspark.driver.python="../venv/bin/python3" \
  run.py