# SMTP-Alert-Cron
This is a python script for sending email alerts to recipients.
I got tired of creating new kubernetes cron jobs, so I configured this script to take in parameters to meet any message requirements that I want to be alerted about.
- This script is dockerized and able to run as a **cron job** in kubernetes via the `cron-template.yaml`. 
- The goal is to reuse the same script and docker container for all
future cron jobs by only editing the cron-template.yaml file and changing the b64 encoded env vars `MESSAGE` and `RECIPIENTS` (list of ',' delimited emails) :)