grocery_items = "milk cheese bread apples oranges chicken"
dairy1 = "milk"
dairy2 = "cheese"
bakery1 = "bread"

#Extract dairy and bakery items by slicing
dairy1 = grocery_items[0:4] # 'milk'
dairy2 = grocery_items [5:11] # 'cheese'
bakery1 = grocery_items [12:17] # 'bread'

# Build and print the sentence
sentence = (
    "We have dairy and bakery items: "
    + dairy1 + ", "
    + dairy2 + " , and "
    + bakery1
    + " in aisle " + str(5)
)
print(sentence)