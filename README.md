# ```               Automation Project               ```
# LinkedIn Job Application Automation Bot

LinkedIn Job Application Automation Project in Python Script we uses Selenium to automate the job application process on LinkedIn. It logs in to your LinkedIn account, searches for Python developer jobs, and applies to each job listing.

## Prerequisites

Before running the script, make sure you have the following installed:

- Python 3
- ChromeDriver (compatible with your Chrome browser version)
- Install project dependencies by running: `pip install -r requirements.txt`

## Usage

1. Clone the repository:

   ```bash
   git clone https://github.com/NoorMahammad-S/linkedin-job-automation.git
   cd linkedin-job-automation
   ```

2. Set up a virtual environment (optional but recommended):

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows, use: .\venv\Scripts\activate
   ```

3. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

4. Update `config.ini` with your LinkedIn credentials.

5. Run the script:

   ```bash
   python linkedin_job_automation.py
   ```

   The script will log in to your LinkedIn account, search for Python developer jobs in London, and automatically apply to each job listing.

## Configuration

Update `config.ini` with your LinkedIn credentials:

```ini
[LinkedIn]
email = Your_Email@example.com
password = Your_Password
```

## Notes

- Make sure to use the correct ChromeDriver version compatible with your Chrome browser.
- Adjust the search criteria in the script for different job searches.

## Contributing

Contributions are welcome! If you find any issues or want to add new features, feel free to open an issue or submit a pull request.
