# Task 4: In-Memory Data Processing Challenge

## Objective
Demonstrate in-memory data processing using Apache Spark DataFrames with caching for performance improvement.

---

## Steps to Run (Copy-Paste Ready)

# 1. Install PySpark if not already installed
pip install pyspark

# 2. Place your dataset (CSV) in the project root directory
# Example: large_dataset.csv with columns -> id, name, department, salary

# 3. Run the script
python Task4_InMemoryProcessing/in_memory_processing.py

---

## Example Dataset (large_dataset.csv)
id,name,department,salary  
1,Alice,HR,50000  
2,Bob,IT,60000  
3,Charlie,Finance,70000  
4,David,IT,80000  
5,Eve,HR,55000  

---

## Example Output
+----------+----------+  
|department|avg_salary|  
+----------+----------+  
|HR        |   52500.0|  
|IT        |   70000.0|  
|Finance   |   70000.0|  
+----------+----------+  

---

## Tools Used
- Apache Spark (PySpark)
- Python
- In-memory caching with DataFrames
