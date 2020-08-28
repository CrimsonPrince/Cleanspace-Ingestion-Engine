import boto3
from datetime import datetime, timedelta
import sys
import s3agent




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
        s3agent.download_s3_folder('openaq-fetches', path)
        print("Downloaded " + currentDate.date().__str__())
    sys.exit()

if __name__ == "__main__":
   main(sys.argv[1:])