# Databricks notebook source
# MAGIC %md
# MAGIC # Sample Databricks Notebook
# MAGIC
# MAGIC This notebook demonstrates:
# MAGIC - Using the root-level utils module
# MAGIC - Importing and using the deeply nested Helpers class
# MAGIC - Basic data processing with PySpark

# COMMAND ----------

# MAGIC %md
# MAGIC ## Setup and Imports

# COMMAND ----------

import sys
from pyspark.sql import SparkSession
from pyspark.sql.functions import col, count

# Add the root directory to the path
sys.path.append('/Workspace/Repos/your-repo')

# Import root utils module
from utils import format_string, calculate_sum, validate_config

# Import the deeply nested helpers class
from level1.level2.level3.level4.level5.helpers import Helpers

# COMMAND ----------

# MAGIC %md
# MAGIC ## Initialize Helpers

# COMMAND ----------

# Initialize the Helpers class with debug mode enabled
helpers = Helpers(debug=True)
print(f"Helpers initialized at: {helpers.format_timestamp()}")

# COMMAND ----------

# MAGIC %md
# MAGIC ## Test Root Utils Functions

# COMMAND ----------

# Test format_string
sample_text = "  hello databricks  "
formatted = format_string(sample_text, uppercase=True)
print(f"Formatted text: {formatted}")

# Test calculate_sum
numbers = [10, 20, 30, 40, 50]
total = calculate_sum(numbers)
print(f"Sum of {numbers}: {total}")

# Test validate_config
config = {'name': 'databricks-app', 'version': '1.0.0'}
is_valid = validate_config(config)
print(f"Config valid: {is_valid}")

# COMMAND ----------

# MAGIC %md
# MAGIC ## Test Helpers Class Functions

# COMMAND ----------

# Test transform_data
data = [
    {'id': 1, 'name': 'Alice', 'score': 95},
    {'id': 2, 'name': 'Bob', 'score': 87},
    {'id': 3, 'name': 'Charlie', 'score': 92}
]
names = helpers.transform_data(data, 'name')
print(f"Names extracted: {names}")

# Test filter_by_condition
scores = [85, 90, 75, 92, 88, 78]
filtered_scores = helpers.filter_by_condition(scores, 85)
print(f"Scores >= 85: {filtered_scores}")

# Test calculate_statistics
stats = helpers.calculate_statistics([float(x) for x in scores])
print(f"Statistics: {stats}")

# COMMAND ----------

# MAGIC %md
# MAGIC ## Create Sample DataFrame

# COMMAND ----------

# Create sample data
sample_data = [
    (1, "Alice", 95, "Engineering"),
    (2, "Bob", 87, "Sales"),
    (3, "Charlie", 92, "Engineering"),
    (4, "Diana", 88, "Marketing"),
    (5, "Eve", 91, "Engineering")
]

# Create DataFrame
df = spark.createDataFrame(sample_data, ["id", "name", "score", "department"])
display(df)

# COMMAND ----------

# MAGIC %md
# MAGIC ## Data Analysis

# COMMAND ----------

# Count by department
dept_counts = df.groupBy("department").agg(count("*").alias("count"))
display(dept_counts)

# Filter high scorers
high_scorers = df.filter(col("score") >= 90)
print(f"High scorers count: {high_scorers.count()}")
display(high_scorers)

# COMMAND ----------

# MAGIC %md
# MAGIC ## Combine Utils and Spark

# COMMAND ----------

# Use helpers to process Spark data
scores_list = [row.score for row in df.collect()]
score_stats = helpers.calculate_statistics([float(x) for x in scores_list])

print("Score Statistics:")
for key, value in score_stats.items():
    print(f"  {key}: {value:.2f}")

# COMMAND ----------

# MAGIC %md
# MAGIC ## Summary

# COMMAND ----------

summary = {
    'total_records': df.count(),
    'departments': df.select('department').distinct().count(),
    'avg_score': score_stats['mean'],
    'timestamp': helpers.format_timestamp()
}

print("Notebook Execution Summary:")
for key, value in summary.items():
    print(f"  {key}: {value}")
