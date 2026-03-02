# 📊 Billing Data Warehouse

This project consists of the **creation of a Data Warehouse focused on the billing domain**, with the main objective of consolidating a **single, reliable source of truth (Single Source of Truth)** for the organization.

The Data Warehouse has been designed to:

- Centralize information from transactional billing systems.
- Apply **company-specific business rules**, ensuring data consistency, quality, and traceability.
- Standardize key metrics and dimensions for financial and operational analysis.
- Enable data consumption for BI, reporting, and advanced analytics.

## 🏗️ Approach and Methodology

This repository was developed following the process detailed in the following base project:

🔗 **Reference process repository:**  
`https://github.com/DataWithBaraa/sql-data-warehouse-project.git`

The design and implementation were supported by multiple technical and functional documents from that same repository, including:

- Architecture definition.
- Modeling guidelines.
- Naming standards.
- Layer specifications (Bronze, Silver, Gold).
- Functional documentation of the billing domain.

## 🎯 Strategic Objective

The purpose of this solution is to provide a robust and scalable data platform that:

- Improves data-driven decision-making.
- Reduces inconsistencies across reports.
- Ensures governance and control over critical billing information.
- Adapts to evolving analytical needs of the company.

## 🏗️ Data Architecture

The data architecture for this project follows Medallion Architecture **Bronze**, **Silver**, and **Gold** layers:
![Data Architecture](docs/data_architecture.png)

1. **Bronze Layer**: Stores raw data as-is from the source systems. Data is ingested from MariaDB Database into PostgreSQL.
2. **Silver Layer**: This layer includes data cleansing, standardization, and normalization processes to prepare data for analysis.
3. **Gold Layer**: Houses business-ready data modeled into a star schema required for reporting and analytics.

---
## 📖 Project Overview

This project involves:

1. **Data Architecture**: Designing a Modern Data Warehouse Using Medallion Architecture **Bronze**, **Silver**, and **Gold** layers.
2. **ETL Pipelines**: Extracting, transforming, and loading data from source systems into the warehouse.
3. **Data Modeling**: Developing fact and dimension tables optimized for analytical queries.
4. **Analytics & Reporting**: Creating SQL-based reports and dashboards for actionable insights.




## 🚀 Project Requirements

### Building the Data Warehouse (Data Engineering)

#### Objective
Develop a modern data warehouse using Open Source Database to consolidate sales data, enabling analytical reporting and informed decision-making.

#### Specifications
- **Data Sources**: Import data from ERP system work in MariaDB.
- **Data Quality**: Cleanse and resolve data quality issues prior to analysis.
- **Integration**: Combine both sources into a single, user-friendly data model designed for analytical queries.
- **Scope**: Focus on the latest dataset only; historization of data is not required.
- **Documentation**: Provide clear documentation of the data model to support both business stakeholders and analytics teams.

---

### BI: Analytics & Reporting (Data Analysis)

#### Objective
Develop SQL-based analytics to deliver detailed insights into:
- **Customer Behavior**
- **Product Performance**
- **Sales Trends**

These insights empower stakeholders with key business metrics, enabling strategic decision-making.  

For more details, refer to [docs/requirements.md](docs/requirements.md).

