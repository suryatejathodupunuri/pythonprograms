import sys;
def compare_columns(input_file, equal_file, unequal_file):
    # Open the input file in read mode and the output files in write mode
    with open(input_file, 'r') as infile, \
         open(equal_file, 'w') as equal_outfile, \
         open(unequal_file, 'w') as unequal_outfile:

        # Iterate over each line in the input file
        for line in infile:
            # Split the line by tab
            columns = line.strip().split('\t')
            
            # Ensure the line has at least 4 columns
            if len(columns) >= 4:
                col1 = columns[0]  #First column
                col2 = columns[1]  # Second column
                col3 = columns[2]  # Third column
                col4 = columns[3]  # Fourth column
                
                
                if col2 == col3 or col2 == col4 or col3 == col4:
                    equal_outfile.write(f"{col1}\t{col2}\t{col3}\t{col4}\n")
                else:
                    unequal_outfile.write(f"{col1}\t{col2}\t{col3}\t{col4}\n")


    print("successful")
# Define the file paths
input_file = sys.argv[1] # The input file path
equal_file = sys.argv[2] # Output file for equal data
unequal_file = sys.argv[3] # Output file for unequal data

# Call the function to process the file and generate outputs
compare_columns(input_file, equal_file, unequal_file)
