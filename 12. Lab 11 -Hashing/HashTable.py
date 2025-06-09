# Author: Mikaela Yvonne
# Date: 05/29/2025
# Description : The code implements two hash table classes: HashTableChaining - for collision resolution using
# linked list chaining; HashTable Probing for collision resolution using linear probing with rehashing.
# Both classes methods for hashing, inserting and finding values.

from LinkedList import LinkedList

class HashTableChaining:
    """
    Create a hash table using linked list chaining for collision resolution
    """
    def __init__(self, size = 17):
        """
        Constructor
        :param size: int the size of the table
        """
        self.__buckets =[]
        for i in range(size):
            self.__buckets.append(LinkedList())

    def __hash(self,value):
        """
        Hash function
        :param value: any
        :return: int the bucket number for the value
        """
        return value % len(self.__buckets)

    def insert(self, value):
        """
        inserts a value into the hash table
        :param value: any
        :return: None
        """
        bucket_num = self.__hash(value)
        self.__buckets[bucket_num].append(value)


    def find(self, value):
        """
        Find the value in the table
        :param value: any
        :return: Return the value in the table that matches the parameter
        """
        bucket_num = self.__hash(value)
        result = self.__buckets[bucket_num].find(value)
        return result

    def __str__(self):
        """
        Create a string representation of the hash table
        :return: str representation of the hash table
        """
        result = ""
        for i in range(len(self.__buckets)):

            result += "bucket" + str(i) + ": " + str(len(self.__buckets[i])) + ": "

        return result


class HashTableProbing:
    """
    Create a hash table using linear probing for collision resolution
    """
    def __init__(self, size = 17):
        """
        Constructor

        :param size: int - the size of the table. needs to be a prime number.
        """
        self.__buckets = [None] * size
        self.__skip = 3


    def __hash(self, value):
        """
        Hash function

        :param value: any
        :return: int the bucket number for the value
        """
        return value % len(self.__buckets)


    def __rehash(self, bucket_num):
        """
        Re-hash function

        :param bucket_num: bucketNum (int) The last bucket number attempted
        :return: (int) the next bucket number to try
        """
        return (bucket_num + self.__skip) % len(self.__buckets)


    def insert(self, value):
        """
        Inserts a value into the hash table

        :param value: any
        :return: None
        """
        bucket_num = self.__hash(value)

        original_bucket_num = bucket_num

        if self.__buckets[bucket_num] is not None:
            bucket_num = self.__rehash(bucket_num)

        while self.__buckets[bucket_num] is not None and bucket_num != original_bucket_num:
            bucket_num = self.__rehash[bucket_num]

        if self.__buckets[bucket_num] is None:
            self.__buckets[bucket_num] = value

        else:
            raise Exception("Table Full")



    def find(self, value):
        """
        Find a value in the table
        :param value: any
        :return: Return the value in the table that matches the parameter or None if
        it's not in the table
        """
        bucket_num = self.__hash(value)

        original_bucket_num = bucket_num

        if self.__buckets[bucket_num] is not None and self.__buckets[bucket_num] == value:
            return self.__buckets[bucket_num]

        else:
            bucket_num = self.__rehash(bucket_num)

        while self.__buckets[bucket_num] is not None and self.__buckets[bucket_num] != value \
                and bucket_num != original_bucket_num:
            bucket_num = self.__rehash(bucket_num)

        if self.__buckets[bucket_num] is not None and self.__buckets[bucket_num] == value:
            return self.__buckets[bucket_num]

        else:
            return None

    def __str__(self):
        """
        Create a string representation of the hash table

        :return: A string representation of the hash table
        """
        result = ""
        for i in range(len(self.__buckets)):

            result += "buckets" + str(i) + ": " + str(self.__buckets[i]) + "\n"
        return result

def main():
    print("Testing HashTableChaining")
    ht_chaining = HashTableChaining()
    chaining_values = [10, 20, 30, 53, 76, 86, 7, 90]
    for value in chaining_values:
        ht_chaining.insert(value)
    print(ht_chaining)

    print("Find 53:", ht_chaining.find(53))
    print("Find 99:", ht_chaining.find(99))
    print("Find 99:", ht_chaining.find(90))
    print("Find 99:", ht_chaining.find(86))

    print("\nTesting HashTableProbing")
    ht_probing = HashTableProbing()
    probing_values = [10, 20, 30, 53, 76, 86, 7, 90]
    for value in probing_values:
        ht_probing.insert(value)
    print(ht_probing)

    print("Find 53:", ht_probing.find(53))
    print("Find 99:", ht_probing.find(99))
    print("Find 99:", ht_chaining.find(90))
    print("Find 99:", ht_chaining.find(86))


if __name__ == "__main__":
    main()
