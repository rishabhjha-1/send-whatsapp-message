import time
import csv
from data import data
import pywhatkit
# Array of phone numbers to send messages to  
def read_phone_numbers_from_csv(csv_file):
    with open(csv_file, 'r') as file:
        reader = csv.reader(file)
        phone_numbers = [row[0] for row in reader]
    return phone_numbers

# Path to the CSV file containing phone numbers
csv_file_path = './unique_numbers.csv'  # Update the path as needed

# Read phone numbers from CSV file
phone_numbers = read_phone_numbers_from_csv(csv_file_path)
 
message_body = " Join Us for LetzKhelo Season 4 Armwrestling Competition on May 5! Dear Armwrestling Enthusiasts,We hope this message finds you in good spirits and ready for an adrenaline-pumping challenge! The LetzKhelo team is thrilled to announce the Season 4 Armwrestling Competition, scheduled to take place on May 5.Are you ready to flex your muscles and test your strength against the best? Whether you're a seasoned pro or a newcomer to the sport, we invite you to join us for a day filled with excitement, camaraderie, and fierce competition.Here's what you can expect from the event:Thrilling Matches: Prepare to go head-to-head with some of the most formidable armwrestlers in the region. With various weight categories and skill levels, there's a challenge waiting for everyone.Expert Guidance: Our experienced referees and judges will ensure fair play and uphold the spirit of sportsmanship throughout the competition. Whether you're a contender or a spectator, you're guaranteed an unforgettable experience.Networking Opportunities: Connect with fellow armwrestling enthusiasts, share tips and techniques, and forge lasting friendships within the community. Who knows? You might even discover your next training partner or mentor.Registration for the event is now open on our website www.letzkhelo.com. Don't miss this chance to showcase your skills and claim your spot among the armwrestling elite!If you have any questions or require assistance with the registration process, please don't hesitate to reach out to our dedicated team. We're here to help make your participation in LetzKhelo Season 4 an unforgettable experience.Get ready to grip it and rip it! We look forward to seeing you at the competition.Best regards,"

  
# Loop through the phone numbers and send the message  
for number in phone_numbers:  
    # pywhatkit requires hour and minute for scheduling  
    current_time = time.localtime()  
    hour = current_time.tm_hour  
    minute = current_time.tm_min + 1  # schedule for 1 minute later  
  
    # Send the message  
    pywhatkit.sendwhatmsg(number, message_body, hour, minute)  
    time.sleep(60)  # wait a minute to prevent overlapping messages