print("Hello Contosville!")
# This is a comment that won't be interpreted as a command.

# Associate variable town with the value "Contosoville"
town = "Contosoville"

# Print a message about the secret location
print( "The town I am looking for is " + town )

# Define a power (function) to chant a phrase
def chant( phrase ):
    # Glue three copies together and print it as a message
    print( phrase + phrase + phrase )

    # Invoke the power to chant on the phrase "Contosoville!"
chant( "Contosoville!" )

def lassoLetter( letter, shiftAmount ):
    letterCode = ord(letter.lower())
    decodedLetterCode = letterCode + shiftAmount
    decodedLetter = chr(decodedLetterCode)
    return decodedLetter

print(lassoLetter('a', 2))

print(lassoLetter('N', 2))