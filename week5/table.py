with open(r"C:\Users\rasti\Desktop\pp2_2025\week5\row.txt", "r", encoding="utf-8") as file:
    lines = file.readlines()

items = []

for i in range(len(lines)):
    line_num = lines[i].strip().rstrip('.')
    
    if line_num.isdigit():  # Check if the line is a number (position number)
        try:
            name = lines[i + 1].strip() # Get the product name
            cleaned_line = lines[i + 2].strip().replace("  ", " ")  # Remove extra spaces
            
            # Check if the line contains " x " and split it into two parts
            if " x " in cleaned_line:
                parts = cleaned_line.split(" x ")

                # Remove spaces inside numbers 
                parts = [p.replace(" ", "") for p in parts]

                # Ensure both parts are numbers
                if len(parts) == 2 and all(p.replace(",", "").replace(".", "").isdigit() for p in parts):
                    quantity, unit_price = parts
                    total_price = lines[i + 3].strip().replace(" ", "")  # Remove spaces inside numbers
                    
                    # Convert to float, replacing commas with dots
                    quantity = float(quantity.replace(",", "."))
                    unit_price = float(unit_price.replace(",", "."))
                    total_price = float(total_price.replace(",", "."))

                    items.append((name, quantity, unit_price, total_price))
                else:
                    print(f"Skipping line {i + 2}: format not matched ({cleaned_line!r})")
            else:
                print(f"Skipping line {i + 2}: format not matched ({cleaned_line!r})")
        except (IndexError, ValueError) as e:
            print(f"Error processing lines {i}-{i + 3}: {e}")

# Print table header
print(f"{'№':<3} {'Product':<50} {'Qty':<7} {'Price':<10} {'Total':<10}")
print("-" * 80)

for idx, (name, quantity, unit_price, total_price) in enumerate(items, 1):
    name_lines = [name[i:i+50] for i in range(0, len(name), 50)]  # Split product name into multiple lines

    print(f"{idx:<3} {name_lines[0]:<50} {quantity:<7} {unit_price:<10} {total_price:<10}")  # First line with number and price

    for line in name_lines[1:]:  # Additional lines without number and price
        print(f"{'':<3} {line:<50}")  

print("-" * 80)