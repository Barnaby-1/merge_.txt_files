import os

directory = "files_to_be_merged"
files = os.listdir(directory)

merged_elements = []

# removes "\n" from elements
def remove_new_line(element):
    return element.removesuffix("\n")

# checks there are 2 files to merge
if len(files) == 2:
    file1 = os.path.join(directory, files[0])
    file2 = os.path.join(directory, files[1])
    # opens both files and reads all the lines
    with open(file1, "r") as f1, open (file2, "r") as f2:
            f1_contents = [remove_new_line(line) for line in f1.readlines()]
            f2_contents = [remove_new_line(line) for line in f2.readlines()]

            new_f1_contents = []
            for elements in f1_contents:
                new_f1_contents.append(elements)

            # removes "\n" ready to check for unique values
            new_f2_contents = []
            for elements in f2_contents:
                new_f2_contents.append(elements)
            
            # loops through all lines in both files
            for elements1 in f1_contents:
                # checks for unique values in file 1 against file 2
                if elements1 not in new_f2_contents:
                    # adds unique values to merged_elements
                    merged_elements.append(elements1)
                for elements2 in f2_contents:
                    if elements1 == elements2:
                        # adds duplicate elements to merged_elements
                        merged_elements.append(elements1)
            
            # checks for unique values in file 2 against file 1
            for elements2 in f2_contents:
                if elements2 not in new_f1_contents:
                        # adds unique values to merged_elements
                        merged_elements.append(elements2)
    
    # adding a new line after each element
    merged_elements = [f"{element}\n" for element in merged_elements]
    # converts merged_elements into a string
    merged_elements = "".join(merged_elements)
    print(merged_elements)

    # opens and writes merged_elements to the new file
    with open("merged_file.txt", "w") as merged_file:
         merged_file.write(merged_elements)
else:
    print("\nThere must be 2 files to merge\n")
