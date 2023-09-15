import os
import pandas as pd

#EXTRACT the Data
def load_data(folder_path):
    # Initialize an empty DataFrame to store the loaded data
    all_data = pd.DataFrame()

    # Loop through each file in the folder
    for file_name in os.listdir(folder_path):
        if file_name.endswith('.csv'):  # Modify the file extension if necessary
            file_path = os.path.join(folder_path, file_name)
            try:
                # Load data from the file
                df = pd.read_csv(file_path)
                # Append the loaded data to the main DataFrame
                #all_data = all_data.append(df, ignore_index=True)
                all_data = pd.concat([all_data, df], ignore_index=True)
            except pd.errors.EmptyDataError:
                print(f"Empty file: {file_name}")
            except pd.errors.ParserError:
                print(f"Error parsing file: {file_name}")

    return all_data

# Specify the folder path
folder_path = 'C:/Users/shazi/Downloads/archive'  # Update with your folder path

# Load data from the folder
loaded_data = load_data(folder_path)

# Display the loaded data
print(loaded_data.head())


# TRANSFORM the Data
loaded_data.rename(columns={'V1': 'S1'},inplace= True)
print(loaded_data.head())

#LOAD to another location
output_file = 'C:/Users/shazi/Downloads/output.csv'
loaded_data.to_csv(output_file, index=False)

# Display the transformed data
print("Data saved to:", output_file)
