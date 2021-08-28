def fizzbuzz(n,additional_rules=None):
    """
    Convert the number to it's name in the game fizzbuzz
    >>> fizzbuzz(3)
    'Fizz'
    >>> fizzbuzz(15)
    'FizzBuzz'
    >>>fizzbuzz(7,{7:"Whizz"})
    'Whizz'
    >>>fizzbuzz(35,{7:"Whizz"})
    'BuzzWhizz'
    >>>fizzbuzz(2)
     '2'
    """
    rules = {3:"Fizz",5:"Buzz"}
    ans = ""
    if additional_rules:
        rules.update(additional_rules)
    for divisor in sorted(rules.keys()):
        if n%divisor == 0:
            ans += rules[divisor]
    if not ans:
        ans = str(n)
    return ans
