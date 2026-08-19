def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True


def largest_number(*args):
    if not args:
        return None
    return max(args)


def student_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")


def calculate_stats(numbers):
    return {
        "maximum": max(numbers),
        "minimum": min(numbers),
        "average": sum(numbers) / len(numbers),
        "sum": sum(numbers)
    }


num = int(input("Enter a number: "))

if is_prime(num):
    print(f"{num} is a prime number")
else:
    print(f"{num} is not a prime number")


numbers = list(map(int, input("Enter numbers separated by spaces: ").split()))
print("Largest number:", largest_number(*numbers))


student_info(
    name="Harsh",
    age=18,
    course="Python",
    college="UIET"
)


stats = calculate_stats(numbers)

print("Maximum:", stats["maximum"])
print("Minimum:", stats["minimum"])
print("Average:", stats["average"])
print("Sum:", stats["sum"])