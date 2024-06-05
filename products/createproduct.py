def create_product_page_and_update_shop(product_title, product_description):
    # Read the content of 'product1.html'
    with open('product1.html', 'r') as file:
        product_content = file.read()

    # Replace placeholders with actual content
    product_content = product_content.replace('IAMTHEPRODUCTTITLE', product_title)
    product_content = product_content.replace('IAMTHEPRODUCTDESCRIPTION', product_description)

    # Define the new file name based on the product title
    product_file_name = f'{product_title.replace(" ", "_").lower()}.html'

    # Save the new content to the new file
    with open(product_file_name, 'w') as file:
        file.write(product_content)

    print(f'New product page created: {product_file_name}')

    # Create the new product entry for the shop
    product_entry = f"""
    <div class="product">
        <a href="products/{product_file_name}">
            <img src="cart.png" alt="{product_title}" class="product-thumb">
            <h3 class="product-title">{product_title}</h3>
            <p class="product-price">$25.00</p>
        </a>
    </div>
    """

    # Read the content of 'shop.html'
    with open('../shop.html', 'r') as file:
        shop_content = file.read()

    # Find the position to insert the new product entry
    insertion_index = shop_content.find('<div class="product-list">') + len('<div class="product-list">')

    # Insert the new product entry
    updated_shop_content = (
        shop_content[:insertion_index]
        + product_entry
        + shop_content[insertion_index:]
    )

    # Save the updated shop content back to 'shop.html'
    with open('../shop.html', 'w') as file:
        file.write(updated_shop_content)

    print('shop.html updated with new product entry')

# Example usage
product_title = input("Enter the product title: ")
product_description = input("Enter the product description: ")

create_product_page_and_update_shop(product_title, product_description)
