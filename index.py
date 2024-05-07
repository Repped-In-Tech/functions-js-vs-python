import sys

def say_my_name():
    return f"My name is {sys.argv[1]}"

def check_age(age):
    if age > 20:
        return 'You can drink!'
    else:
        return 'No drank fa ya!'

# Pythonic Standard Practice when running files directly
if __name__ == "__main__":
    print(check_age(age = int(sys.argv[1])))
    
    # print(say_my_name())
    # print("Come here!")
