import csv
book = [[]]
def append_dict_to_csv(file_path, my_dict):
    try:
        with open('Demo.csv', 'a', newline='') as file:
            fieldnames = ['name','author','volume','issued']
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            # Append the dictionary
            writer.writerow(my_dict)
            print(f"List appended to {file_path} successfully.")
    except Exception as e:
        print(f"Error: {e}")