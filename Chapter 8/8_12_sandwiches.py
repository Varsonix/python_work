def sandwich_order(*items):
    print("\nMaking a sandwich with the following ingredients:")
    if not items:
        print("- No ingredients. Just bread...\n")
    for item in items:
        print(f"- {item}")

sandwich_order('tomato', 'onions', 'lettuce', 'ham', 'turkey')
sandwich_order('turkey', 'ham', 'mustard')
sandwich_order()