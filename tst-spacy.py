import spacy

nlp = spacy.load("en_core_web_sm")
text = """
    Edmond P. Legaspi
Education
2012-2017
I
Bachelor of Science in Applied Mathematics
Data Engineer
University of the Philippines Los Baños
Work History
Data Engineer
Experienced Data Engineer well-versed
2019-Current I Imfre, Inc.
in defining requirements, planning
Developed and designed systems to collect real time streaming data from
solutions and implementing structures.
multiple portals using Kinesis Streams, perform data transformations and
With also experience in
enrichments, and direct it to various sources such as Elasticsearch and Data
architecting/automating and optimizing
Lake.
mission critical data pipeline
Designed and built real time data warehouse / dashboard to power
deployments infrastructure.
numerous data processing, data discovery, and internal business intelligence
and real-time analytics using Elasticsearch and Kibana
Contact
Implemented a continuous integration/continuous deployment (CI/CD)
pipeline for processing data by implementing CI/CD methods (particularly
+63 9167-794-3412
using Terraform and CodePipeline)
legaspi.edmond@gmail.com
Built APIs and developer tooling that allow both internal and external
https://www.linkedin.com/i
engineers to quickly build streaming applications in a self service manner.
/edmond-legaspi-201360120/
Jr. Data Analyst
2018-2019
I
Aarki, Inc.
Skills
Perform data analysis that provides a platform for decision making on a
Programming: Python, Java, Shell
variety of business issues
Script
Apply expertise in quantitative analysis, data mining, and the presentation of
Business Analytics/Databases:
data to see beyond the numbers and guide applicable next steps
Tableau, SQL, PostgreSQL, Kibana,
Understand clients' needs and priorities to create detailed models
MongoDB, Elasticsearch
Run A/B testing and statistical analyses to extract actionable insights that
Infrastructure Management:
influence, support, and assist in product decisions and launches
Terraform, AWS CloudFormation
Ad Hoc analysis to support sales techniques, marketing strategies, and
Version Control: Github/Bitbucket
campaign optimization
CI/CD: Docker, Docker Compose
Present proposals and results in a clear manner backed by data and coupled
with actionable conclusions
AWS
Update and maintain detailed campaign reports
Computing/FaaS: EC2, ECS, Fargate,
Lambda
Junior Market Analyst
Streaming Services: Data Kinesis
2016-2016
|
Ashok Trading Academy
Stream
Gather & Study vital financial information
CI/CD: CodePipeline, CodeBuild,
Recommends trade actions by fundamentals and technical analysis
CodeDeploy
Identifies financial status by analyzing actual results with forecasts and variances
Monitoring: Cloudwatch,
Certifications
CloudwatchLogs, Cloudtrail, Config
AWS Certified Solutions Architect - Associate
DB/Storage: RDS (MySQL
Professional Growth
&PostgreSQL), DynamoDB, S3, EBS,
AWS Certified Big Data Specialty 2020 - In Depth & Hands On!
Storage Gateway, Redshift
Networking/Scalability: VPC, VPC
SQL and Relational Databases 101 -- IBM Cognitive Class
Peering, ELBs, Route53, Flow Logs,
Python 101 for Data Science -- IBM Cognitive Class
ASG
SQL Advanced - Bespoke - NobleProg
CDN: Cloudfront
Kafka Essential Training - Linkedln
Decoupling Applications: SQS, SNS,
Apache Spark Essential Training - Linkedln
Kinesis
Taming Big Data with Apache Spark and Python - Hands On! - Udemy
Version Control: Codecommit
Apache Kafka Series - Learn Apache Kafka for Beginners v2 -- Udemy
Ultimate AWS Certified Developer Associate 2019 - Udemy
"""
doc = nlp(text)

for ent in doc.ents:
    print(ent.text, ent.start_char, ent.end_char, ent.label_)