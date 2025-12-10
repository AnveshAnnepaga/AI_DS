s = set()

def set_(st):
    for i in range(6):
        st.add(int(input(f"Enter integer {i+1}: ")))
    print("Final set:", st)

set_(s)