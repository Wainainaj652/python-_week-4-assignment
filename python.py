def file_processing_app():
    print("File Processing Application")
    print("--------------------------")
    
    # Get input filename with error handling
    while True:
        input_filename = input("Enter the name of the file to read: ")
        try:
            # Try to open the file for reading
            with open(input_filename, 'r') as input_file:
                content = input_file.read()
            break  # Exit loop if file was successfully read
        except FileNotFoundError:
            print(f"Error: The file '{input_filename}' does not exist.")
        except PermissionError:
            print(f"Error: You don't have permission to read '{input_filename}'.")
        except IsADirectoryError:
            print(f"Error: '{input_filename}' is a directory, not a file.")
        except UnicodeDecodeError:
            print(f"Error: Could not decode the file '{input_filename}'. It may not be a text file.")
        except Exception as e:
            print(f"An unexpected error occurred: {str(e)}")
    
    # Modify the content (example: convert to uppercase)
    modified_content = content.upper()
    
    # Get output filename with validation
    while True:
        output_filename = input("Enter the name of the output file: ")
        if output_filename.strip() == "":
            print("Error: Output filename cannot be empty.")
            continue
        
        if output_filename == input_filename:
            print("Error: Output filename cannot be the same as input filename.")
            continue
        
        try:
            # Try to open the file for writing to check permissions
            with open(output_filename, 'w') as test_file:
                pass
            break
        except PermissionError:
            print(f"Error: You don't have permission to write to '{output_filename}'.")
        except Exception as e:
            print(f"An unexpected error occurred: {str(e)}")
    
    # Write the modified content to the new file
    try:
        with open(output_filename, 'w') as output_file:
            output_file.write(modified_content)
        print(f"Success! Modified content written to '{output_filename}'.")
    except Exception as e:
        print(f"Failed to write to output file: {str(e)}")

# Run the application
if __name__ == "__main__":
    file_processing_app()