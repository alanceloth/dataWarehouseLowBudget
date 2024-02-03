from frontend import CSVValidatorUI
from backend import process_csv, csv_to_sql
import logging
import sentry_sdk

import sentry_sdk

sentry_sdk.init(
    dsn="https://998b620bfe94c8f55bd0640e8ea26ee0@o4506680328323072.ingest.sentry.io/4506680337104896",
    # Set traces_sample_rate to 1.0 to capture 100%
    # of transactions for performance monitoring.
    traces_sample_rate=1.0,
    # Set profiles_sample_rate to 1.0 to profile 100%
    # of sampled transactions.
    # We recommend adjusting this value in production.
    profiles_sample_rate=1.0,
)

def main():
    ui = CSVValidatorUI()
    ui.display_header()

    upload_file = ui.upload_file()

    if upload_file:
        df, result, error = process_csv(upload_file)
        ui.display_results(result, error)
        
        if error:
            ui.display_wrong_message()
            logging.error("Error: %s", error)
            sentry_sdk.capture_message("Error: %s", error)
        elif ui.display_save_button():
            csv_to_sql(df)
            ui.display_success_message()
            logging.info("Data saved in the database")
            sentry_sdk.capture_message("Data saved in the database")

if __name__ == "__main__":
    main()
        