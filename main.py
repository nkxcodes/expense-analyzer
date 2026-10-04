
def main():
    import pandas as pd

    df = pd.read_csv('expense_analyzer/expense.csv')

    total_expense = df['amount'].sum()
    highest_expense = df['amount'].max()
    lowest_expense = df['amount'].min()
    average_expense = df['amount'].mean()

    print(df)

    print()
    print('========== Analysis ==========')

    print()
    print(f'Total Expenditure: ₹{total_expense}')
    print(f'Highest Expense: ₹{highest_expense}')
    print(f'Lowest Expense: ₹{lowest_expense}')
    print(f'Average Expense: ₹{average_expense:.2f}')

if __name__ == "__main__":
    main()