# Big Data Challenges

This repository contains solutions for four Big Data challenges, covering data preprocessing, real-time streaming, incremental processing with CDC, and in-memory data processing.  
Each task includes scripts and a dedicated README with instructions to run.

---

## 📂 Tasks Overview

### 🟢 Task 1: Data Preprocessing (30%)
- **Objective:** Clean and preprocess a raw dataset using Apache Spark.  
- **Includes:** Handling missing values, type inconsistencies, duplicates, normalization, feature engineering.  
- **Directory:** `Task1_DataPreprocessing`

---

### 🔵 Task 2: Real-Time Data Streaming (35%)
- **Objective:** Build a Kafka Producer-Consumer system that streams simulated sensor data in real time.  
- **Includes:** Producer, Consumer, Stream Processor (rolling averages).  
- **Tools:** Apache Kafka, Python (`kafka-python`).  
- **Directory:** `Task2_RealTimeStreaming`

---

### 🟡 Task 3: Incremental Data Processing with CDC (25%)
- **Objective:** Process data incrementally using Change Data Capture (CDC) concepts.  
- **Includes:** Insert, Update, Delete events streamed via Kafka and applied to an in-memory state.  
- **Tools:** Apache Kafka, Python (`kafka-python`).  
- **Directory:** `Task3_IncrementalProcessing`

---

### 🔴 Task 4: In-Memory Data Processing (10%)
- **Objective:** Analyze large datasets efficiently using in-memory processing with PySpark.  
- **Includes:** DataFrames, caching, aggregation queries.  
- **Tools:** Apache Spark (PySpark).  
- **Directory:** `Task4_InMemoryProcessing`

---

## 🛠️ Tools & Technologies
- **Apache Kafka** → Real-time data streaming & CDC  
- **Apache Spark (PySpark)** → Data preprocessing & in-memory analytics  
- **Python** → Data processing logic  
- **Jupyter Notebooks / Python scripts** → For coding and submission  

---

## 🚀 How to Use

```bash
# 1. Clone the repository
git clone git@github.com:Harish-M-R/bigdata-challenges.git
cd bigdata-challenges

# 2. Navigate to a specific task folder (example: Task 2)
cd Task2_RealTimeStreaming

# 3. Follow the steps in that task’s README to run
