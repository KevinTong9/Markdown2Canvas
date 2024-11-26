import sys
import uuid

def main():
    print(uuid.uuid4().hex[0:10])
    print(sys.argv[1])

if __name__ == "__main__":
    sys.exit(main())
