# Avi_RealTime_Datapipeline - End-to-End Medallion Architecture

## 📌 Project Overview
Built a real-time data pipeline using **Databricks Medallion Architecture** with Jobs orchestration. This project demonstrates an end-to-end ELT pipeline from raw ingestion to analytics-ready gold tables.

## 🏗️ Architecture

**Bronze Layer (Raw Ingestion):**
- Ingested raw CSV data into Delta Lake
- Schema evolution enabled
- Used Batch Ingest

**Silver Layer (Cleaning & Transform):**
- Data cleaning, deduplication, null handling
- PySpark transformations
- Delta format optimization

**Gold Layer (Business Aggregations):**
- Aggregated tables for BI & Reporting
- Optimized for analytics queries

**Orchestration:**
- Databricks Jobs with task dependencies
- Bronze -> Silver -> Gold sequential run
- Auto retry & monitoring enabled

## 🛠️ Tech Stack
- Databricks Workspace, PySpark, Delta Lake, Databricks Jobs, GitHub

## 🚀 Workflow Execution
Job: `Avi_Medallion_Job` - Status: Succeeded. Runs daily.

## 👨‍💻 Author
**Bobbala Harin** | Aspiring Data Engineer
GitHub: @Harinbobbala16
