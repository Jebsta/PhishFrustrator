Here's a README for your project:

---

# PhishFrustrator

PhishFrustrator is a Python toolset designed to combat and frustrate scammers and phishers by sending a large number of randomized login attempts to their phishing pages. This tool can help in identifying phishing sites and protecting users from scam SMS messages prompting them to log in to malicious websites.

## Features

- Sends randomized login attempts to a specified URL.
- Uses a large list of first names, last names, and passwords to generate unique credentials.
- Logs the responses from the phishing site for further analysis.
- Provides statistics on the number of successful and attempted requests.

## Prerequisites

- Python 3.x
- `requests` library (install using `pip install requests`)

## Installation

1. Clone the repository:

    ```sh
    git clone https://github.com/Jebsta/PhishFrustrator.git
    cd PhishFrustrator
    ```

2. Install the required Python libraries:

    ```sh
    pip install requests
    ```

3. Prepare the required data files:
    - `first-names.txt`: A file containing a list of first names.
    - `names.txt`: A file containing a list of last names.
    - `passwords.txt`: A file containing a list of passwords.

## Usage

1. Edit the `url` variable in the script to point to the phishing site's login page:

    ```python
    url = "https://example-phishing-site.com/login"
    ```

2. Run the script:

    ```sh
    python phishfrustrator.py
    ```

3. The script will start sending randomized login attempts and logging the responses. The logs are saved in two files:
    - `log.txt`: Summary log with statistics.
    - `log_verbose.txt`: Detailed log with individual request details.

## Script Details

The script performs the following steps:

1. Loads first names, last names, and passwords from text files.
2. Generates random usernames and passwords.
3. Sends POST requests to the specified URL with the generated credentials.
4. Logs the responses from the server.
5. Provides periodic updates on the number of attempts and successful requests.

## Example Log Output

```
[100] Attempted 100 requests, 5 successful requests
[100] 12.345 seconds elapsed, 8.1 requests per second
```

## Disclaimer

This tool is intended for educational purposes and to help individuals protect themselves from phishing scams. 
It should not be used for any illegal activities. The author is not responsible for any misuse of this tool.
I just made this script because i joked with my friends about it.
Please use a VPN when using this script!

## Contributing

Contributions are welcome! Please open an issue or submit a pull request with your changes.
