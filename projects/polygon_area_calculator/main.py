from shape_calculator import Rectangle, Square

def main():
    print("Rectangle Examples:")
    print("-----------------")
    
    # Create a rectangle
    rect = Rectangle(10, 5)
    print(f"Rectangle Area: {rect.get_area()}")
    print(f"Rectangle Perimeter: {rect.get_perimeter()}")
    print(f"Rectangle Diagonal: {rect.get_diagonal():.2f}")
    print(f"String Representation: {rect}")
    
    # Change rectangle dimensions
    rect.set_height(3)
    print(f"\nAfter changing height to 3:")
    print(f"New Rectangle: {rect}")
    print(f"New Area: {rect.get_area()}")
    print(f"New Perimeter: {rect.get_perimeter()}")
    
    # Print rectangle picture
    print("\nRectangle Picture:")
    print(rect.get_picture())
    
    print("\nSquare Examples:")
    print("---------------")
    
    # Create a square
    sq = Square(9)
    print(f"Square Area: {sq.get_area()}")
    print(f"Square Perimeter: {sq.get_perimeter()}")
    print(f"Square Diagonal: {sq.get_diagonal():.2f}")
    print(f"String Representation: {sq}")
    
    # Change square side
    sq.set_side(4)
    print(f"\nAfter changing side to 4:")
    print(f"New Square: {sq}")
    print(f"New Area: {sq.get_area()}")
    print(f"New Perimeter: {sq.get_perimeter()}")
    
    # Change square using width method (should affect both width and height)
    sq.set_width(5)
    print(f"\nAfter changing width to 5:")
    print(f"New Square: {sq}")
    print(f"Width: {sq.width}, Height: {sq.height}")
    
    # Print square picture
    print("\nSquare Picture:")
    print(sq.get_picture())
    
    # Test get_amount_inside
    rect.set_width(16)
    rect.set_height(8)
    print(f"\nHow many {sq} can fit in {rect}?")
    print(f"Answer: {rect.get_amount_inside(sq)}")
    
    # Test a case where no shapes fit
    small_rect = Rectangle(2, 3)
    big_rect = Rectangle(3, 6)
    print(f"\nHow many {big_rect} can fit in {small_rect}?")
    print(f"Answer: {small_rect.get_amount_inside(big_rect)}")
    
    # Test a case with "Too big for picture"
    big_rect = Rectangle(60, 10)
    print(f"\nTrying to print a picture of {big_rect}:")
    print(big_rect.get_picture())

if __name__ == "__main__":
    main()