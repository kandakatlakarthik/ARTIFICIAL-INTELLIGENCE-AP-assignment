def compute_charges(pu, cu, cust_type):
    # Energy charges
    ec = pu * cu

    # Rules for Fixed Charges (FC) and Customer Charges (CC)
    ct = cust_type.lower()
    if ct in ("d", "domestic", "residential"):
        # Domestic / Residential
        if cu <= 100:
            fc = 50.0
        elif cu <= 300:
            fc = 75.0
        else:
            fc = 100.0
        cc = 30.0
        ed_rate = 0.05  # 5% electricity duty on energy charges
    elif ct in ("c", "commercial", "industrial"):
        # Commercial / Industrial
        if cu <= 100:
            fc = 100.0
        elif cu <= 300:
            fc = 150.0
        else:
            fc = 200.0
        cc = 50.0
        ed_rate = 0.10  # 10% electricity duty on energy charges
    else:
        raise ValueError("Unknown customer type. Use Domestic/Commercial (D/C).")

    ed = ed_rate * ec
    total = ec + fc + cc + ed
    return ec, fc, cc, ed, total

def read_float(prompt):
    while True:
        try:
            return float(input(prompt).strip())
        except ValueError:
            print("Invalid number. Please try again.")

def read_cu(prompt):
    while True:
        try:
            v = input(prompt).strip()
            # allow integer or float units
            return float(v)
        except ValueError:
            print("Invalid units. Please enter numeric value.")

def main():
    print("Electricity Bill Calculator")
    pu = read_float("Enter Price per Unit (PU): ")
    cu = read_cu("Enter Units Consumed (CU): ")
    cust_type = input("Enter Customer Type (Domestic/Commercial) [D/C]: ").strip()

    try:
        ec, fc, cc, ed, total = compute_charges(pu, cu, cust_type)
    except ValueError as e:
        print(e)
        return

    # Print results (2 decimal places)
    print(f"EC(Energy Charges): {ec:.2f}")
    print(f"FC(Fixed Charges): {fc:.2f}")
    print(f"CC(Customer Charges): {cc:.2f}")
    print(f"ED(Electricity Duty Charges): {ed:.2f}")
    print(f"Bill Amount: {total:.2f}")

if __name__ == "__main__":
    main()