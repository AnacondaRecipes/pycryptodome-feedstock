from Crypto.Random import random


def test_pycryptodome_pkg():
    """
    Tests to validate the pycrptodome pkg.
    """
    print("Validating pycryptodome package")
    #  Returns  an integer <=a and <=b
    x = random.randint(0, 5000)
    y = random.randint(0,5000)
    assert 0 <= x <= 5000, "Failed to assert the random number from given range"
    assert x != y, "Failed to generate Random numbers"

    # Returns a random value from the list
    list1 = [1, 2, 3, 4, 5, 6]
    output_3 = random.choice(list1)
    assert output_3 in list1, "Failed to assert the random number from list Returned value is not in the list "


test_pycryptodome_pkg()