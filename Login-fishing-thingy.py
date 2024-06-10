# a script that sends a post request to a login page and sends a username and password to the page
# and then prints the response from the page

import json
import random
import time
import requests

url = "https://neu-winsim.com/routes/process_login.php"
timeout = 0.5
unsuccesful_requests_in_a_row = 0
max_unsuccesful_requests_in_a_row = 100
wait = False
timeout_unsuccesful_requests = 0.25
timeout_successful_requests = -0.125

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
# add timestamp to logfile name
timestamp = time.strftime("%Y%m%d-%H%M%S")
log_file = open(f'{timestamp}-log.log', "w")
log_file_verbose = open(f'{timestamp}-log_verbose.log', "w")

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
    try:
        response = requests.post(url, data=data)
    except Exception:
        unsuccesful_requests_in_a_row += 1
        print(f"[{i}] Unsuccesful requests because of an error. Error will be ignored!")
        log_file.write(f"[{i}] Unsuccesful requests because of an error. Error will be ignored!\n")
        log_file_verbose.write(f"[{i}] Unsuccesful requests because of an error. Error will be ignored!\n")
        continue

    # response.text = {"status":"success","uid":1718029114} (str)
    # i want to get the status part
    if response:
        rsp = json.loads(response.text)

        # check if 'status' is 'success'
        if rsp['status'] == 'success':
            print(f'[{i}] Username: {username}, Password: {password}, Response: {response.text}')
            log_file_verbose.write(f'[{i}] Username: {username}, Password: {password}, Response: {response.text}\n')
            successful_requests += 1
            timeout += timeout_successful_requests
            unsuccesful_requests_in_a_row = 0
        else: 
            print(f'[{i}] Username: {username}, Password: {password}, Response: {response.text}')
            log_file_verbose.write(f'[{i}] Username: {username}, Password: {password}, Response: {response.text}\n')
            break
    else:
        print(f'[{i}] Username: {username}, Password: {password}, Response: no response')
        timeout += timeout_unsuccesful_requests
        unsuccesful_requests_in_a_row += 1
        log_file_verbose.write(f'[{i}] Username: {username}, Password: {password}, Response: no response, New Timeout = {timeout}\n')

    if i % 100 == 0:
        print(f"[{i}] Attempted {i} requests, {successful_requests} successful requests\n[{i}] {time.time() - start_time} seconds elapsed, {successful_requests / (time.time() - start_time)} requests per second")
        log_file.write(f"[{i}] Attempted {i} requests, {successful_requests} successful requests\n[{i}] {time.time() - start_time} seconds elapsed, {successful_requests / (time.time() - start_time)} requests per second\n")
        log_file_verbose.write(f"[{i}] Attempted {i} requests, {successful_requests} successful requests\n[{i}] {time.time() - start_time} seconds elapsed, {successful_requests / (time.time() - start_time)} requests per second\n")
        
    log_file_verbose.flush()
    log_file.flush()
    if unsuccesful_requests_in_a_row >= max_unsuccesful_requests_in_a_row:
        print(f"Unsuccesful requests in a row reached {max_unsuccesful_requests_in_a_row}, stopping...")
        log_file.write(f"Unsuccesful requests in a row reached {max_unsuccesful_requests_in_a_row}, stopping...\n")
        log_file_verbose.write(f"Unsuccesful requests in a row reached {max_unsuccesful_requests_in_a_row}, stopping...\n")
        break
    if wait:
        time.sleep(timeout)

