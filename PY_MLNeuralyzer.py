# PY_MLNeuralyzer
# Colin Buenvenida


# Importing global package(s)
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


def neuralyzer():
    """
    Of 4 possible ML_Brainstem data frames (created by PY_MLBrainSurgeon's brainOp() function),
    loads a user-specified frame and reads through it, replacing values that are equal to or below a
    user-specified threshold.

    :return: A new CSV file depicting the newly-screened and edited data frame, the output itself varying by a user-case
    basis.
    """

    # User greeting
    print("Hi Colin! This is neuralyzer(). \nWhat data frame are we working on today?", "\n")
    print("1: DEN_Coronal")
    print("2: INT_Coronal")
    print("3: DEN_Sagittal")
    print("4: INT_Sagittal", "\n")

    # Data frame selection
    user_select = int(input("What dataframe?: "))
    if user_select not in [1, 2, 3, 4]:
        print("Invalid input. Will restart the program. \n")
        neuralyzer()

    # Assigning data frame and file path
    if user_select == 1:
        filePath = "nu_brain_NewDenC.csv"
        fileOutput = "wakeup_NewDenC"
    elif user_select == 2:
        filePath = "nu_brain_NewIntC.csv"
        fileOutput = "wakeup_NewIntC"
    elif user_select == 3:
        filePath = "nu_brain_NewDenS.csv"
        fileOutput = "wakeup_NewDenS"
    elif user_select == 4:
        filePath = "nu_brain_NewIntS.csv"
        fileOutput = "wakeup_NewIntS"

    # Asking user to set a threshold
    try:
        threshold = float(input("\nEnter the threshold value: "))
    except ValueError:
        print("Invalid threshold value. Please enter a numeric value.")
        exit(1)

    # Reading CSV file with pandas
    df = pd.read_csv(filePath, header=0, float_precision='high')

    # Showcasing a head table of the loaded data
    print("\nHead of the original data:")
    print(df.head())

    # Replacing values below or equal to the threshold with NaN's
    for col in df.columns:
        if df[col].dtype == 'float64':  # Checking if the column contains numerical data
            df[col][df[col] <= threshold] = np.nan

    # Showcasing a head table of the now-processed data
    print("\nHead of the processed data:")
    print(df.head())

    # Counting non-NaN entries for each row
    non_nan_counts = df.notna().sum(axis=1)

    # Plotting a bar chart
    plt.figure(figsize=(10, 6))
    plt.bar(range(len(non_nan_counts)), non_nan_counts, color='blue')
    plt.xlabel('Row Index')
    plt.ylabel('Number of Non-NaN Entries')
    plt.title('Number of Active Genes (Non-NaN Entries) per Voxel (Row)')
    plt.show()

    # Showcasing the number of NaN-filled rows (voxels) and columns (genes) there are w/in the now-processed data
    NaN_voxels = df[df.isnull().all(axis=1)]    # Voxels
    print("\nRows with all NaN values:")
    print(NaN_voxels)
    NaN_genes = df.columns[df.isnull().all()]   # Genes
    print("\nColumns with all NaN values:")
    print(NaN_genes)

    # Counting the number of rows and columns with all NaN values, printing the results
    num_rows_with_all_nan = NaN_voxels.shape[0]
    num_columns_with_all_nan = len(NaN_genes)
    print("\nNumber of rows with all NaN values:", num_rows_with_all_nan)
    print("Number of columns with all NaN values:", num_columns_with_all_nan)

    # Exporting NaN-filled rows (voxels) and columns (genes) to separate CSV files
    export_nan_rows = input("\nDo you want to export rows with all NaN values to a CSV file? (y/n): ")
    export_nan_columns = input("Do you want to export columns with all NaN values to a CSV file? (y/n): ")

    if export_nan_rows.lower() == 'y':
        # Export indices of rows with all NaN values to a CSV file vertically
        NaN_voxels_index = NaN_voxels.index.to_frame(name='Row Indices')
        NaN_voxels_index.to_csv(f"{fileOutput}_[{threshold}]_NaNRows.csv", index=False)
        print(f"Rows with all NaN values exported to {fileOutput}_[{threshold}]_NaNRows.csv")

    if export_nan_columns.lower() == 'y':
        # Export columns with all NaN values to a CSV file vertically
        NaN_columns = pd.DataFrame({'Column Names': NaN_genes})
        NaN_columns.to_csv(f"{fileOutput}_[{threshold}]_NaNColumns.csv", index=False)
        print(f"Columns with all NaN values exported to {fileOutput}_[{threshold}]_NaNColumns.csv")

    # Making sure the new data frame is to the user's liking
    proceed = input("\nDo you want to go ahead and save the new data frame? (y/n): ")
    if proceed == 'y':
        NaN_shave = input("\nDo you want to remove columns and rows with all NaN values? (y/n): ")
        if NaN_shave == 'y':
            # Removing NaN rows and columns
            df = df.dropna(axis=0, how='all')
            df = df.dropna(axis=1, how='all')

            # Writing modified data to a new CSV file WITHOUT NaN's
            print("\nData frame screening and processing complete.")
            print("The new data frame will be saved under the following name: ",
                  f"{fileOutput}_[{threshold}]_noNaN.csv")
            print("Bye bye!")
            nu_fileOutput = f"{fileOutput}_[{threshold}]_noNaN.csv"
            df.to_csv(nu_fileOutput, index=False)
        else:
            # Writing modified data to a new CSV file WITH NaN's
            print("\nData frame screening and processing complete.")
            print("The new data frame WILL contain the NaN's.")
            print("The new data frame will be saved under the following name: ", f"{fileOutput}_[{threshold}].csv")
            print("Bye bye!")
            nu_fileOutput = f"{fileOutput}_[{threshold}].csv"
            df.to_csv(nu_fileOutput, index=False)

    else:
        print("\nEither 'n' or an invalid input was entered. Terminating function. Sayonara.")


if __name__ == "__main__":
    # Running function, neuralyzer()
    neuralyzer()
