# PY_MLBrainSurgeon
# Colin Buenvenida


# Importing necessary global packages
import pandas as pd


def brainOp():
    """
    Of the 4 possible ML_Brainstem data frames, loads a user-specified one and pre-processes it for further analysis

    :return: Pre-processed data frame, from initial DEN/INT coronal and sagittal data frames
    """

    # User greeting:
    print("Hi Colin! This is brainOp(). \nWhat data frame are we working on today?", "\n")
    print("1: DEN_Coronal")
    print("2: INT_Coronal")
    print("3: DEN_Sagittal")
    print("4: INT_Sagittal", "\n")

    # Data frame selection:
    try:
        user_select = int(input("What dataframe?: "))
    except ValueError:
        print("Invalid input. Please enter a number, 1 through 4.")

    # Assigning data frame and file path:
    if user_select == 1:
        filePath = "NewDenC.csv"
        outputPath = "nu_brain_NewDenC.csv"
    elif user_select == 2:
        filePath = "NewIntC.csv"
        outputPath = "nu_brain_NewIntC.csv"
    elif user_select == 3:
        filePath = "NewDenS.csv"
        outputPath = "nu_brain_NewDenS.csv"
    elif user_select == 4:
        filePath = "NewIntS.csv"
        outputPath = "nu_brain_NewIntS.csv"
    else:
        print("Invalid option. Please select a number between 1 and 4.")

    # Reading CSV file
    df = pd.read_csv(filePath, header=0)

    # Displaying a head table to ensure successful and proper loading of data
    print("Original DataFrame:")
    print(df.head())

    # Removing columns 1 through 6
    df = df.iloc[:, 6:]

    # Displaying the head table after pre-processing
    print("\nDataFrame after removing columns 1 through 6:")
    print(df.head())

    # Calculating and displaying the maximum and minimum values
    max_value = df.values.max()
    min_value = df.values.min()
    print(f"\nMinimum Value: {min_value}")
    print(f"Maximum Value: {max_value}")

    # Saving the edited DataFrame to a new CSV file
    user_ok = input("\nWould you like to go ahead and create a new .csv file based on the data frame? y/n?: ")

    if user_ok == "y":
        df.to_csv(outputPath, index=False)
        print(f"\nEdited DataFrame saved to {outputPath}")
    else:
        print("C'est la vie. Next time then.")
        pass

    return df


if __name__ == "__main__":
    brainOp()
