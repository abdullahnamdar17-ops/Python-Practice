name = input("Enter your name? ")

match name: #switch statement
    
#     case "Alice":
#         print("Hello Alice!")
#     case "Bob":
#         print("Hello Bob!")
#     case _:
#         print("Who!")

    case "Alice" | "Bob":
        print("Hello Alice!")
    case _:
        print("Who are you?")