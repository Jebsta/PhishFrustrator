# a script that sends a post request to a login page and sends a username and password to the page
# and then prints the response from the page

import json
import random
import time
import requests

url = "https://neu-winsim.com/routes/process_login.php"

# load firstnames from first-names.txt
firstnames = []
with open("first-names.txt") as f:
    firstnames = f.readlines()
firstnames = [x.strip() for x in firstnames]

# load lastnames from names.txt
lastnames = []
with open("names.txt") as f:
    lastnames = f.readlines()
lastnames = [x.strip() for x in lastnames]

# load passwords from passwords.txt
passwords = []
with open("passwords.txt") as f:
    passwords = f.readlines()
passwords = [x.strip() for x in passwords]

num_requests = 1000000
successful_requests = 0
start_time = time.time()
# create a log file
log_file = open("log.txt", "w")
log_file_verbose = open("log_verbose.txt", "w")

for i in range(1, num_requests + 1):
    # choose random first name, last name, and password
    random_first_name = random.choice(firstnames)
    random_last_name = random.choice(lastnames)
    random_password = random.choice(passwords)

    # create username
    username = (random_first_name[0] + "." + random_last_name + str(random.randint(1, 1000))).lower()
    password = random_password

    data = {
        "username": username,
        "password": password
    }

    response = requests.post(url, data=data)
    # response.text = {"status":"success","uid":1718029114} (str)
    # i want to get the status part
    if response:
        rsp = json.loads(response.text)

        # check if 'status' is 'success'
        if rsp['status'] == 'success':
            print(f'[{i}] Username: {username}, Password: {password}, Response: {response.text}')
            log_file_verbose.write(f'[{i}] Username: {username}, Password: {password}, Response: {response.text}\n')
            successful_requests += 1
        else: 
            print(f'[{i}] Username: {username}, Password: {password}, Response: {response.text}')
            log_file_verbose.write(f'[{i}] Username: {username}, Password: {password}, Response: {response.text}\n')
            break
    else:
        print(f'[{i}] Username: {username}, Password: {password}, Response: no response')
        log_file_verbose.write(f'[{i}] Username: {username}, Password: {password}, Response: no response\n')

    if i % 100 == 0:
        print(f"[{i}] Attempted {i} requests, {successful_requests} successful requests\n[{i}] {time.time() - start_time} seconds elapsed, {successful_requests / (time.time() - start_time)} requests per second")
        log_file.write(f"[{i}] Attempted {i} requests, {successful_requests} successful requests\n[{i}] {time.time() - start_time} seconds elapsed, {successful_requests / (time.time() - start_time)} requests per second\n")
        log_file_verbose.write(f"[{i}] Attempted {i} requests, {successful_requests} successful requests\n[{i}] {time.time() - start_time} seconds elapsed, {successful_requests / (time.time() - start_time)} requests per second\n")
        
    log_file_verbose.flush()
    log_file.flush()
