# Debug Log

**Explain how you used the the techniques covered (Trace Forward, Trace Backward, Divide & Conquer) to uncover the bugs in each exercise. Be specific!**

In your explanations, you may want to answer:

- What is the expected vs. actual output?
- If there is a stack trace, what useful information does it contain?
- Which technique did you use, on which line numbers?
- What assumptions did you have about each line of code, and which ones were proven to be wrong?

### Example:
 I noticed that the program should show pizza orders once a new order is made, and that it wasn't showing any. 
 So, I used the `trace forward technique` starting on `line 13`. I discovered the bug on `line 27` was caused by a typo of `'pzza'` instead of `'pizza'`._

_Then I noticed another bug ..._

## Exercise 1 - Flask Pizza Shop
expected output is supposed to be redirect to the homepage after the order has been submitted and saved in the database.
The error says toppings is not in pizza toppings. It says that the info we are passing is matching up with the model we have set
I used trace backward to solve this problem. Since the issue was a form post error, it was just looking through the post operations to see what where it was going wrong

## Exercise 2 - Weather API

### Bug 1: Data is not correctly passed back leaving parameters empty.
### Solution: By using step forward on line 39 and 40 finding out why the parameters are empty, solution is renaming them to match the parameters.
### Bug 2: Api call returns an error.
### Solution: By looking at the api docs, the api takes q as the city name
### Bug 3: Data is not correct when setting context variables.
### Solution: By using trace forward on line 50 and checking the stack call you can set each variable to the correct location in the json file to match up.

## Exercise 3 - Sort/Search Algorithms

### Merge Sort
### Bug 1: On line 37 the index was out of range. 
### Solution: By using trace backward we can look the fact that the while loop uses variable j that is equal to zero. The contents should also be using variable j as well.

### Binary Search
### Bug 1: Float error thrown out on line 48.
### Solution: By using trace forward on line 48 we can see that the error occurs becasue a float instead of an int is being passed. To fix it we use // instead of /.
