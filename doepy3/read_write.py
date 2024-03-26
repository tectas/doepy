import csv
import json


# ==========================================================
# Function for reading a CSV file into a dictionary format
# ==========================================================


def read_variables_csv(csvfile):
    """
    Builds a Python dictionary object from an input CSV file.
    Helper function to read a CSV file on the disk, where user stores the limits/ranges of the process variables.
    Output of this function can be used directly with any DOE builder function
    The CSV file should be in the same directory
    """
    dict_key = {}
    try:
        with open(csvfile) as f:
            reader = csv.DictReader(f)
            fields = reader.fieldnames
            for row in reader:
                for field in fields:
                    if field not in dict_key:
                        dict_key[field] = []
                    dict_key[field].append(float(row[field]))
        return dict_key
    except:
        print(
            "Error in reading the specified file from the disk. Please make sure it is in current directory."
        )
        return -1


# ===============================================================
# Function for writing the design matrix into an output CSV file
# ===============================================================


def write_csv(df, filename, rounding=2):
    """
    Writes a CSV file on to the disk from the computed design matrix
    filename: To be specified by the user. Just a name is fine. .CSV extension will be added automatically.
    rounding: Number up to which decimal the output will be rounded off. Often needed for practical DOE plans.
    """
    df_copy = round(df, rounding)
    try:
        if ".csv" not in filename:
            filename = filename + ".csv"
        f = df_copy.to_csv(filename, index=False)
        return f
    except:
        return -1


# ===============================================================
# Function for writing the design matrix into an output JSON file
# ===============================================================


def write_json(df, filename, rounding=2):
    """
    Writes a JSON file on to the disk from the computed design matrix
    filename: To be specified by the user. Just a name is fine. .JSON extension will be added automatically.
    rounding: Number up to which decimal the output will be rounded off. Often needed for practical DOE plans.
    """
    df_copy = round(df, rounding)
    try:
        if ".json" not in filename:
            filename = filename + ".json"
        with open(filename, 'w') as f:
            result_json = json.dumps(df.to_dict(orient='list'))
            f.write(result_json)
        return f
    except:
        return -1


# ===============================================================
# Function for reading a JSON file into a dictionary format
# ===============================================================


def read_json(filename):
    """
    Builds a Python dictionary object from an input JSON file.
    Helper function to read a JSON file on the disk, where user stores the limits/ranges of the process variables.
    Output of this function can be used directly with any DOE builder function
    The JSON file should be in the same directory
    """
    try:
        with open(filename) as f:
            data = json.load(f)
        return data
    except:
        print(
            "Error in reading the specified file from the disk. Please make sure it is in current directory."
        )
        return -1
