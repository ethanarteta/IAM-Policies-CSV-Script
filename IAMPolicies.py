import csv
import boto3
import os.path
# Create an AWS Identity and Access Management (IAM) client using Boto3
client = boto3.client('iam')
# Define the function
def policies_list():
    # Request the policies
    response = client.list_policies()
    # Create a CSV file where the results will be written
    csv_filename = 'IAM_Policies.csv'
    # Empty list to store policy data
    policies_filtered = []

    # Collect policy information
    for policy in response['Policies']:
        policies_filtered.append({
            "Policy_Name": policy['PolicyName'],
            "PolicyId": policy['PolicyId'],
            "Arn": policy['Arn']
        })
    # Write the results to the CSV file
    with open(csv_filename, 'w', newline='') as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=['Policy_Name', 'PolicyId', 'Arn'], extrasaction='ignore')
        writer.writeheader()
        writer.writerows(policies_filtered)
# Run Function
policies_list()
# Creates a variable for the path of the CSV file
path = './IAM_Policies.csv'
# Check if the file has been created
check_file = os.path.exists(path)
# If statement depending on the result
if check_file == True:
       
       print(" IAM_Policies.csv created ")
else:
      
       print("Error try again")
