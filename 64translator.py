import base64
import os

def encode_base64(data):
    return base64.b64encode(data).decode('utf-8')

def decode_base64(data):
    return base64.b64decode(data).decode('utf-8')

def get_input():
    choice = input("Would you like to provide input directly or select a file? (input/file): ").strip().lower()

    if choice == "file":
        file_path = input("Please provide the path to the file: ").strip()
        if not os.path.exists(file_path):
            print("File does not exist.")
            return None, None
        with open(file_path, 'rb') as file:
            data = file.read()
        return data, "file"
    elif choice == "input":
        data = input("Please enter the text to encode/decode: ").strip().encode('utf-8')
        return data, "input"
    else:
        print("Invalid choice.")
        return None, None

def main():
    data, data_type = get_input()
    if data is None:
        return

    action = input("Would you like to encode or decode the input? (encode/decode): ").strip().lower()

    if action == "encode":
        result = encode_base64(data)
    elif action == "decode":
        if data_type == "file":
            # For files, assume the content is already in Base64 format.
            result = decode_base64(data.decode('utf-8'))
        else:
            result = decode_base64(data.decode('utf-8'))
    else:
        print("Invalid action.")
        return

    if data_type == "file":
        output_file = input("Enter the output file path: ").strip()
        with open(output_file, 'w') as file:
            file.write(result)
        print(f"Result has been saved to {output_file}")
    else:
        print("Result:", result)

if __name__ == "__main__":
    main()
