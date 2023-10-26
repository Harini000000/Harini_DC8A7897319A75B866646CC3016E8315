def linear_search_product(products, target_product):
  indices = []
  for index, product in enumerate(products):
      if product == target_product:
          indices.append(index)
  return indices

# Example usage:
products = ["Apple", "Banana", "Orange", "Apple", "Grape"]
target_product = "Apple"
result = linear_search_product(products, target_product)
print(result)  # Output will be [0, 3]
