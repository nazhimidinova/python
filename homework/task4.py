
partition = str(input("Please enter partition name: "))
service = str(input("Please enter service name: "))
region = str(input("Please enter region name: "))
accountid = int(input("Please enter accountid: "))
resourceid = int(input("Please enter resourceid: "))
arn = f"arn:{partition}:{service}:{region}:{accountid}:{resourceid}"
print(arn)