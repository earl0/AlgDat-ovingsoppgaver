from sys import stdin

# This program traverses a linked list and finds the highest value.

class Record:
    value = None
    next = None

    def __init__(self, value):
        self.value = value
        self.next = None


def search(record):
    if (record.next == None): # If this is the last record, return it's value
        return record.value
    # Otherwise, return the highest of either this record's value, or the
    # highest value of the following records in the linked list
    return max(record.value, search(record.next))
                            


def main():
    # reading from stdin and creating a linked list
    first = None
    last = None
    for line in stdin:
        penultimate = last
        last = Record(int(line))
        if first is None:
            first = last
        else:
            penultimate.next = last

    # searching and printing out the result
    print(search(first))


if __name__ == "__main__":
    main()