'''
Lab 02 Step 4 - Hashing Program
Daniel Mendoza, 801414965
ITIS 3200 - Info Security and Privacy
Professor Jian Xiang
'''
import json

def hash_file():
    pass

def traverse_directory():
    pass

def generate_table(filepath) -> dict:
    pass

def validate_hash(file, hash) -> bool:
    pass

def main():
    while True:
        choice = int(input("(1) Generate Hashes for a Directory\n(2) Validate Hashes\n(3) Exit\nChoice: "))
        if choice == 1:
            filepath = input("Provide a filepath: ")
            hash_table = generate_table(filepath)
            with open('hash_table.json', 'w') as file:
                file.write(json.dump(hash_table))
        elif choice == 2:
            valid = True
            with open('hash_table.json') as file:
                hash_table = json.load(file)
                for path, hash in hash_table.items():
                    if not validate_hash(path, hash):
                        print("Valid hash found at file: ", path)
                        valid = False
                if not valid:
                    print("All keys validated in", file)
        elif choice == 3:
            print("Exiting...")
            break
        else:
            print("Invalid option.")

if __name__ == "__main__":
    main()