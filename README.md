# CLI Utility for working with the Bitly Services using their API
This small CLI Utility shorts any long urls creating bitlinks with metrics. 

The Bitlinks metrics show how many times your bitlink was clicked.

The CLI Utility uses Bitly Services through their API (https://dev.bitly.com/)

## First steps
1. Clone / download the repository
2. Install the CLI utility following the steps below
3. Read user manual. 

### How to install
1. Generate access `token` to connect with Bitly API  
    To connect with Bitly API you have to use your own token.  
    To get the token, create a Bitly account and generate the access token in API settings of your Bitly profile or follow this link: https://app.bitly.com/settings/api/  

    Once the token is generated, place it in a file named `.env`. The file should be located in root directory of the project.  
    
    The API token in .env file should look like: 
    ```
    API_TOKEN = 4510184a6fe87ba1f222ea522c356d31a842c6a5
    ```

    > :warning: Keep the access token in secret, don't commit it in your git repository.


2. Install Python3 and project dependencies  
    Python3 should be already installed.   
    
    We recommend to use the Python Virtual Environment (https://docs.python.org/3/tutorial/venv.html).

    Then use `pip` (or `pip3`, if there is a conflict with Python2) to install dependencies:
    ```
    pip install -r .venv/requirements.txt
    ```

### Usage
Please refer to built-in user help manual, when executing the CLI Utility in your cmd console:
```
> cli_bitlink.py --help  
```

### Project Goals

The code is written for educational purposes on online-course for web-developers [dvmn.org](https://dvmn.org/).
