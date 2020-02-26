# RAE Daily Word
This project scrapes RAE webpage and sends by email today's featured word with its meaning.

![]readme/walkthrough.png

### :wrench: **Configuration**
## Step 1
Install all mandatory modules -> `Pip install requirements.txt`

## Step 2
Set email sender (skip this step if you are not sending the word by email)
There are two options here. Using dotenv or hardcoding your email address and paswword to the main.py script
Dotenv method:
Create a new file named ".env" and type in the following:
```
EMAIL=your_email_address@gmail.com
PASSWORD=your_password
```

Hard coding method:
Open the main.py script with any text editor and type in your email address and password (user and password variables)
![]readme/email_s3.png
*Note:* Notice that either way, the email address must be a gmail.com account


### :file_folder: **Folder structure**
```
└── project
    ├── .gitignore
    ├── .env
    ├── requeriments.txt
    ├── README.md
    ├── main.py
    ├── notebooks
    ├── packages
    │   ├── Acquisition
    │   │   ├── argparser.py
    │   │   └── scraper.py
    │   ├── Analyzing
    │   │   └── analysis.py
    │   └── Reporting
    │   │   └── newsletter.py
    └── data
        ├── recipients.csv
        └── words.csv
```


