
def main():
    import pandas as pd

    df = pd.read_csv('expense.csv')

    print()
    print('========== EXPENSE ANALYZER ==========')
    print()

    total_expense = df['amount'].sum()
    highest_expense = df['amount'].max()
    lowest_expense = df['amount'].min()
    average_expense = df['amount'].mean()
    category_expense = df.groupby('category')['amount'].sum()
    highest_transaction = df[df['amount'] == df['amount'].max()]

    print(df)

    print()
    print('========== Analysis ==========')

    print()
    print(f'Total Expenditure: ₹{total_expense}')
    print(f'Highest Expense: ₹{highest_expense}')
    print(f'Lowest Expense: ₹{lowest_expense}')
    print(f'Average Expense: ₹{average_expense:.2f}')

    print()
    print(category_expense)

    print()
    print(f'Category Max Expense: ₹{category_expense.max()}')

    print()
    print(f'Highest Transaction: ')
    print(highest_transaction)

if __name__ == "__main__":
    main()