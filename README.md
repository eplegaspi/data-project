# Data Project

# Sample Text Extract with PDF (pdf.py)
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

# Sample Named Entity Recognition (named_entities.py)
```
Calling DetectEntities
{
    "Entities": [
        {
            "BeginOffset": 5,
            "EndOffset": 14,
            "Score": 0.9712600708007812,
            "Text": "Edmond P.",
            "Type": "PERSON"
        },
        {
            "BeginOffset": 15,
            "EndOffset": 22,
            "Score": 0.6990995407104492,
            "Text": "Legaspi",
            "Type": "ORGANIZATION"
        },
        {
            "BeginOffset": 33,
            "EndOffset": 42,
            "Score": 0.9702270030975342,
            "Text": "2012-2017",
            "Type": "DATE"
        },
        {
            "BeginOffset": 102,
            "EndOffset": 131,
            "Score": 0.9736692905426025,
            "Text": "University of the Philippines",
            "Type": "ORGANIZATION"
        },
        {
            "BeginOffset": 132,
            "EndOffset": 141,
            "Score": 0.9710884690284729,
            "Text": "Los Ba\u00f1os",
            "Type": "LOCATION"
        },
        {
            "BeginOffset": 207,
            "EndOffset": 211,
            "Score": 0.9938310384750366,
            "Text": "2019",
            "Type": "DATE"
        },
        {
            "BeginOffset": 222,
            "EndOffset": 233,
            "Score": 0.8282142877578735,
            "Text": "Imfre, Inc.",
            "Type": "ORGANIZATION"
        },
        {
            "BeginOffset": 403,
            "EndOffset": 410,
            "Score": 0.6679206490516663,
            "Text": "Kinesis",
            "Type": "TITLE"
        },
        {
            "BeginOffset": 411,
            "EndOffset": 418,
            "Score": 0.4272090196609497,
            "Text": "Streams",
            "Type": "COMMERCIAL_ITEM"
        },
        {
            "BeginOffset": 531,
            "EndOffset": 544,
            "Score": 1.0,
            "Text": "Elasticsearch",
            "Type": "COMMERCIAL_ITEM"
        },
        {
            "BeginOffset": 830,
            "EndOffset": 843,
            "Score": 1.0,
            "Text": "Elasticsearch",
            "Type": "COMMERCIAL_ITEM"
        },
        {
            "BeginOffset": 848,
            "EndOffset": 854,
            "Score": 0.8528515696525574,
            "Text": "Kibana",
            "Type": "ORGANIZATION"
        },
        {
            "BeginOffset": 1003,
            "EndOffset": 1020,
            "Score": 0.9900745749473572,
            "Text": "+63 9167-794-3412",
            "Type": "OTHER"
        },
        {
            "BeginOffset": 1027,
            "EndOffset": 1036,
            "Score": 0.530957818031311,
            "Text": "Terraform",
            "Type": "TITLE"
        },
        {
            "BeginOffset": 1041,
            "EndOffset": 1053,
            "Score": 0.6332933902740479,
            "Text": "CodePipeline",
            "Type": "ORGANIZATION"
        },
        {
            "BeginOffset": 1055,
            "EndOffset": 1079,
            "Score": 0.9631871581077576,
            "Text": "legaspi.edmond@gmail.com",
            "Type": "OTHER"
        },
        {
            "BeginOffset": 1124,
            "EndOffset": 1128,
            "Score": 0.9431847929954529,
            "Text": "both",
            "Type": "QUANTITY"
        },
        {
            "BeginOffset": 1151,
            "EndOffset": 1177,
            "Score": 0.9453963041305542,
            "Text": "https://www.linkedin.com/i",
            "Type": "OTHER"
        },
        {
            "BeginOffset": 1255,
            "EndOffset": 1280,
            "Score": 0.7264560461044312,
            "Text": "edmond-legaspi-201360120/",
            "Type": "OTHER"
        },
        {
            "BeginOffset": 1298,
            "EndOffset": 1307,
            "Score": 0.7186384797096252,
            "Text": "2018-2019",
            "Type": "DATE"
        },
        {
            "BeginOffset": 1310,
            "EndOffset": 1321,
            "Score": 0.977746844291687,
            "Text": "Aarki, Inc.",
            "Type": "ORGANIZATION"
        },
        {
            "BeginOffset": 1414,
            "EndOffset": 1420,
            "Score": 0.9866251945495605,
            "Text": "Python",
            "Type": "TITLE"
        },
        {
            "BeginOffset": 1422,
            "EndOffset": 1426,
            "Score": 0.9925520420074463,
            "Text": "Java",
            "Type": "TITLE"
        },
        {
            "BeginOffset": 1428,
            "EndOffset": 1433,
            "Score": 0.9049133062362671,
            "Text": "Shell",
            "Type": "TITLE"
        },
        {
            "BeginOffset": 1640,
            "EndOffset": 1647,
            "Score": 0.989635169506073,
            "Text": "Tableau",
            "Type": "TITLE"
        },
        {
            "BeginOffset": 1649,
            "EndOffset": 1652,
            "Score": 0.9906608462333679,
            "Text": "SQL",
            "Type": "TITLE"
        },
        {
            "BeginOffset": 1654,
            "EndOffset": 1664,
            "Score": 0.9849739074707031,
            "Text": "PostgreSQL",
            "Type": "TITLE"
        },
        {
            "BeginOffset": 1666,
            "EndOffset": 1672,
            "Score": 0.9837407469749451,
            "Text": "Kibana",
            "Type": "TITLE"
        },
        {
            "BeginOffset": 1741,
            "EndOffset": 1748,
            "Score": 0.9821252822875977,
            "Text": "MongoDB",
            "Type": "TITLE"
        },
        {
            "BeginOffset": 1750,
            "EndOffset": 1763,
            "Score": 1.0,
            "Text": "Elasticsearch",
            "Type": "COMMERCIAL_ITEM"
        },
        {
            "BeginOffset": 1933,
            "EndOffset": 1942,
            "Score": 0.643983781337738,
            "Text": "Terraform",
            "Type": "ORGANIZATION"
        },
        {
            "BeginOffset": 1944,
            "EndOffset": 1947,
            "Score": 0.9851865172386169,
            "Text": "AWS",
            "Type": "ORGANIZATION"
        },
        {
            "BeginOffset": 1948,
            "EndOffset": 1962,
            "Score": 0.5128036141395569,
            "Text": "CloudFormation",
            "Type": "TITLE"
        },
        {
            "BeginOffset": 2051,
            "EndOffset": 2057,
            "Score": 0.859306812286377,
            "Text": "Github",
            "Type": "TITLE"
        },
        {
            "BeginOffset": 2058,
            "EndOffset": 2067,
            "Score": 0.8796945214271545,
            "Text": "Bitbucket",
            "Type": "TITLE"
        },
        {
            "BeginOffset": 2097,
            "EndOffset": 2103,
            "Score": 0.3363986909389496,
            "Text": "Docker",
            "Type": "ORGANIZATION"
        },
        {
            "BeginOffset": 2105,
            "EndOffset": 2111,
            "Score": 0.36099016666412354,
            "Text": "Docker",
            "Type": "ORGANIZATION"
        },
        {
            "BeginOffset": 2223,
            "EndOffset": 2226,
            "Score": 0.9958927631378174,
            "Text": "AWS",
            "Type": "ORGANIZATION"
        },
        {
            "BeginOffset": 2289,
            "EndOffset": 2292,
            "Score": 0.39624664187431335,
            "Text": "EC2",
            "Type": "OTHER"
        },
        {
            "BeginOffset": 2299,
            "EndOffset": 2306,
            "Score": 0.7923741936683655,
            "Text": "Fargate",
            "Type": "ORGANIZATION"
        },
        {
            "BeginOffset": 2308,
            "EndOffset": 2314,
            "Score": 0.5455145835876465,
            "Text": "Lambda",
            "Type": "ORGANIZATION"
        },
        {
            "BeginOffset": 2357,
            "EndOffset": 2369,
            "Score": 0.8333207368850708,
            "Text": "Data Kinesis",
            "Type": "ORGANIZATION"
        },
        {
            "BeginOffset": 2370,
            "EndOffset": 2379,
            "Score": 0.9651731252670288,
            "Text": "2016-2016",
            "Type": "DATE"
        },
        {
            "BeginOffset": 2382,
            "EndOffset": 2403,
            "Score": 0.9854800701141357,
            "Text": "Ashok Trading Academy",
            "Type": "ORGANIZATION"
        },
        {
            "BeginOffset": 2461,
            "EndOffset": 2473,
            "Score": 0.4223259389400482,
            "Text": "CodePipeline",
            "Type": "ORGANIZATION"
        },
        {
            "BeginOffset": 2475,
            "EndOffset": 2484,
            "Score": 0.5854305028915405,
            "Text": "CodeBuild",
            "Type": "ORGANIZATION"
        },
        {
            "BeginOffset": 2550,
            "EndOffset": 2560,
            "Score": 0.5449939966201782,
            "Text": "CodeDeploy",
            "Type": "TITLE"
        },
        {
            "BeginOffset": 2658,
            "EndOffset": 2668,
            "Score": 0.8423929810523987,
            "Text": "Cloudwatch",
            "Type": "TITLE"
        },
        {
            "BeginOffset": 2685,
            "EndOffset": 2699,
            "Score": 0.543770432472229,
            "Text": "CloudwatchLogs",
            "Type": "TITLE"
        },
        {
            "BeginOffset": 2701,
            "EndOffset": 2711,
            "Score": 0.8209521174430847,
            "Text": "Cloudtrail",
            "Type": "TITLE"
        },
        {
            "BeginOffset": 2720,
            "EndOffset": 2723,
            "Score": 0.9830495715141296,
            "Text": "AWS",
            "Type": "ORGANIZATION"
        },
        {
            "BeginOffset": 2778,
            "EndOffset": 2781,
            "Score": 0.5116491317749023,
            "Text": "RDS",
            "Type": "OTHER"
        },
        {
            "BeginOffset": 2783,
            "EndOffset": 2801,
            "Score": 0.6657083630561829,
            "Text": "MySQL\nProfessional",
            "Type": "TITLE"
        },
        {
            "BeginOffset": 2810,
            "EndOffset": 2820,
            "Score": 0.43930649757385254,
            "Text": "PostgreSQL",
            "Type": "TITLE"
        },
        {
            "BeginOffset": 2823,
            "EndOffset": 2831,
            "Score": 0.7775035500526428,
            "Text": "DynamoDB",
            "Type": "TITLE"
        },
        {
            "BeginOffset": 2833,
            "EndOffset": 2835,
            "Score": 0.8231731057167053,
            "Text": "S3",
            "Type": "TITLE"
        },
        {
            "BeginOffset": 2837,
            "EndOffset": 2840,
            "Score": 0.8156144618988037,
            "Text": "EBS",
            "Type": "TITLE"
        },
        {
            "BeginOffset": 2842,
            "EndOffset": 2845,
            "Score": 0.7449948787689209,
            "Text": "AWS",
            "Type": "ORGANIZATION"
        },
        {
            "BeginOffset": 2875,
            "EndOffset": 2879,
            "Score": 0.8875938653945923,
            "Text": "2020",
            "Type": "DATE"
        },
        {
            "BeginOffset": 2962,
            "EndOffset": 2965,
            "Score": 0.8280623555183411,
            "Text": "SQL",
            "Type": "TITLE"
        },
        {
            "BeginOffset": 2998,
            "EndOffset": 3001,
            "Score": 0.9560208916664124,
            "Text": "IBM",
            "Type": "ORGANIZATION"
        },
        {
            "BeginOffset": 3002,
            "EndOffset": 3011,
            "Score": 0.3593454360961914,
            "Text": "Cognitive",
            "Type": "TITLE"
        },
        {
            "BeginOffset": 3012,
            "EndOffset": 3017,
            "Score": 0.3325992822647095,
            "Text": "Class",
            "Type": "OTHER"
        },
        {
            "BeginOffset": 3033,
            "EndOffset": 3040,
            "Score": 0.47260400652885437,
            "Text": "Route53",
            "Type": "TITLE"
        },
        {
            "BeginOffset": 3042,
            "EndOffset": 3051,
            "Score": 0.5956608057022095,
            "Text": "Flow Logs",
            "Type": "TITLE"
        },
        {
            "BeginOffset": 3053,
            "EndOffset": 3063,
            "Score": 0.971939206123352,
            "Text": "Python 101",
            "Type": "TITLE"
        },
        {
            "BeginOffset": 3084,
            "EndOffset": 3087,
            "Score": 0.9611243605613708,
            "Text": "IBM",
            "Type": "ORGANIZATION"
        },
        {
            "BeginOffset": 3108,
            "EndOffset": 3111,
            "Score": 0.755571186542511,
            "Text": "SQL",
            "Type": "TITLE"
        },
        {
            "BeginOffset": 3133,
            "EndOffset": 3142,
            "Score": 0.4441637098789215,
            "Text": "NobleProg",
            "Type": "ORGANIZATION"
        },
        {
            "BeginOffset": 3148,
            "EndOffset": 3158,
            "Score": 0.721122682094574,
            "Text": "Cloudfront",
            "Type": "TITLE"
        },
        {
            "BeginOffset": 3159,
            "EndOffset": 3164,
            "Score": 0.5812486410140991,
            "Text": "Kafka",
            "Type": "TITLE"
        },
        {
            "BeginOffset": 3220,
            "EndOffset": 3223,
            "Score": 0.9762864112854004,
            "Text": "SQS",
            "Type": "TITLE"
        },
        {
            "BeginOffset": 3225,
            "EndOffset": 3228,
            "Score": 0.848581075668335,
            "Text": "SNS",
            "Type": "TITLE"
        },
        {
            "BeginOffset": 3230,
            "EndOffset": 3242,
            "Score": 0.7062606811523438,
            "Text": "Apache Spark",
            "Type": "TITLE"
        },
        {
            "BeginOffset": 3302,
            "EndOffset": 3308,
            "Score": 0.6955340504646301,
            "Text": "Apache",
            "Type": "ORGANIZATION"
        },
        {
            "BeginOffset": 3309,
            "EndOffset": 3314,
            "Score": 0.659520149230957,
            "Text": "Spark",
            "Type": "TITLE"
        },
        {
            "BeginOffset": 3319,
            "EndOffset": 3325,
            "Score": 0.98150634765625,
            "Text": "Python",
            "Type": "TITLE"
        },
        {
            "BeginOffset": 3340,
            "EndOffset": 3345,
            "Score": 0.34422236680984497,
            "Text": "Udemy",
            "Type": "PERSON"
        },
        {
            "BeginOffset": 3374,
            "EndOffset": 3380,
            "Score": 0.6522382497787476,
            "Text": "Apache",
            "Type": "TITLE"
        },
        {
            "BeginOffset": 3381,
            "EndOffset": 3393,
            "Score": 0.6483775973320007,
            "Text": "Kafka Series",
            "Type": "TITLE"
        },
        {
            "BeginOffset": 3402,
            "EndOffset": 3408,
            "Score": 0.5519299507141113,
            "Text": "Apache",
            "Type": "TITLE"
        },
        {
            "BeginOffset": 3409,
            "EndOffset": 3414,
            "Score": 0.525940477848053,
            "Text": "Kafka",
            "Type": "TITLE"
        },
        {
            "BeginOffset": 3429,
            "EndOffset": 3431,
            "Score": 0.41073670983314514,
            "Text": "v2",
            "Type": "TITLE"
        },
        {
            "BeginOffset": 3435,
            "EndOffset": 3440,
            "Score": 0.38587701320648193,
            "Text": "Udemy",
            "Type": "ORGANIZATION"
        },
        {
            "BeginOffset": 3450,
            "EndOffset": 3453,
            "Score": 0.8335628509521484,
            "Text": "AWS",
            "Type": "ORGANIZATION"
        },
        {
            "BeginOffset": 3484,
            "EndOffset": 3488,
            "Score": 0.949600100517273,
            "Text": "2019",
            "Type": "DATE"
        },
        {
            "BeginOffset": 3491,
            "EndOffset": 3496,
            "Score": 0.9427134394645691,
            "Text": "Udemy",
            "Type": "PERSON"
        }
    ],
    "ResponseMetadata": {
        "HTTPHeaders": {
            "content-length": "8699",
            "content-type": "application/x-amz-json-1.1",
            "date": "Thu, 20 Jan 2022 14:53:07 GMT",
            "x-amzn-requestid": "024fbe85-af47-4bb3-8cb4-b1babe399c17"
        },
        "HTTPStatusCode": 200,
        "RequestId": "024fbe85-af47-4bb3-8cb4-b1babe399c17",
        "RetryAttempts": 0
    }
}
End of DetectEntities
```
