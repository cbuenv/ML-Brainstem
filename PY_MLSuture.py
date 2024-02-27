# PY_MLSuture
# Colin Buenvenida


# Importing global packages
import pandas as pd


def suture(filepath, column_threshold, row_threshold):
    """
    Loads a CSV file based on provided filepath by user, and removes rows and columns with NaN values based on given or
    automatically determined screening thresholds, in the form of a float. Rows and columns will be removed accordingly
    if they are made up of NaN values at that set point or higher.

    :param filepath: CSV file
    :param column_threshold: Column threshold (float), percentage of non-NaN values that make up the data frame
    :param row_threshold: Row threshold (float), percentage of non-NaN values that make up the data frame

    :return: Revised dataframe that is screened according to the given parameters
    """

    # Validating and converting thresholds to percentages
    try:
        column_threshold = float(column_threshold)
        row_threshold = float(row_threshold)
        if not (0 <= column_threshold <= 100 and 0 <= row_threshold <= 100):
            raise ValueError("Thresholds must be between 0 and 100.")
    except ValueError:
        print("Invalid threshold input. Thresholds must be numeric values between 0 and 100.")
        return

    # Loading CSV file with pandas
    df = pd.read_csv(filepath, header=0, float_precision='high')

    # Showcasing head table of loaded dataset
    print("\nHEAD TABLE OF LOADED DATASET:")
    print(df.head())

    # Determining the column threshold count
    column_threshold_count = int((column_threshold / 100) * len(df))
    # Removing columns if overall makeup is less than the provided NaN threshold
    df = df.dropna(axis=1, thresh=column_threshold_count)

    # Determining the row threshold count
    row_threshold_count = int((row_threshold / 100) * len(df.index))
    # Removing rows if overall makeup is less than the provided NaN threshold
    df = df.dropna(axis=0, thresh=row_threshold_count)

    # Showcasing head table of screening dataset
    print("\nHEAD TABLE OF SCREENED DATASET:")
    print(df.head())

    # Showcasing the overall size of the revised dataset
    print("\nDimensions of screened dataset (row x column): ", df.shape)

    # Making sure the new data frame is to the user's liking
    proceed = input("\nWould you like to finalize the new dataframe and save it as a file? (y/n): ")
    if proceed.lower() == 'y':
        fileOutput_name = input("\nEnter a name for the new file: ")
        fileOutput = f"{fileOutput_name}.csv"
        print("\nSaving new file under the name " + fileOutput)
        df.to_csv(fileOutput, index=False)

    else:
        print("\nTerminating session. Will not save the newly-screened dataframe.")


if __name__ == "__main__":
    # User greeting
    print("\nHey Colin! This is suture(). Booting up analysis protocol now...")

    # Asking for filepath, column_threshold, and row_threshold
    filepath = input("\nEnter file to be analyzed: ")
    column_threshold = float(input("Enter column threshold: "))
    row_threshold = float(input("Enter row threshold: "))

    # Executing suture()
    suture(filepath, column_threshold, row_threshold)

    # Contingency Protocol #############################
    ''' NOTE: The below code checks if a given data frame contains NaN values'''

    contingency_init = input("\nDo you want to initiate contingency analysis? (y/n): ")
    if contingency_init.lower() == 'y':
        print("\n\nsuture() Contingency Protocol now booting...")  # Greeting user and initiating protocol
        double_check = input("What is the name of the CSV file you would like to check?: ")

        df = pd.read_csv(double_check)  # Reading CSV file
        has_nan_values = df.isna().any().any()  # Checking for NaN values
        print(f"Does the CSV file have NaN values? {has_nan_values}")  # Printing the result

    else:
        print("\nWill not initiate contingency protocol. Bye!")
    #####################################################

