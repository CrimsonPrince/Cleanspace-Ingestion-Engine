import boto3
from datetime import datetime, timedelta
import os
import sys

s3 = boto3.resource('s3')


def download_s3_folder(bucket_name, s3_folder, local_dir=None):

    bucket = s3.Bucket(bucket_name)
    for obj in bucket.objects.filter(Prefix = s3_folder):
        target = obj.key if local_dir is None \
            else os.path.join(local_dir, os.path.basename(obj.key))
        if not os.path.exists(os.path.dirname(target)):
            os.makedirs(os.path.dirname(target))
        bucket.download_file(obj.key, target)


def main(argv):

    if(len(argv) != 2):
        print("Please Submit Start Date & End Date as Arguments In Reverse Eg 2020-08-10")
        sys.exit()

    
    startDate = datetime.strptime(argv[0], "%Y-%m-%d")
    endDate = datetime.strptime(argv[1], "%Y-%m-%d")
    currentDate = startDate
    path = ""
    
    delta =  endDate - startDate

    for day in range(delta.days + 1):
        currentDate =  startDate + timedelta(days=day)
        path = "realtime/" + currentDate.date().__str__()
        download_s3_folder('openaq-fetches', path)
        print("Downloaded " + currentDate)
    sys.exit()
    # download_s3_folder('openaq-fetches', 'realtime/2020-08-27')
    # print(datetime.now().date())

if __name__ == "__main__":
   main(sys.argv[1:])