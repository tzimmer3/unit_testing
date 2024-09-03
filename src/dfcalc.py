import pandas as pd

def addDF(data):
    """Add Function"""
    return data['x values'] + data['y values']


def subtractDF(data):
    """Subtract Function"""
    return data['x values'] - data['y values']


def multiplyDF(data):
    """Multiply Function"""
    return data['x values'] * data['y values']


def divideDF(data):
    """Divide Function"""
    for value in data['y values'].values.tolist():
        if value == 0:
            raise ValueError("Can not divide by zero!")
    return data['x values'] / data['y values']


if __name__ == '__main__':


    df = pd.read_csv("C:\\Users\\hlmq\code\\unit_testing\\test\\df_calc_test_data.csv")
    # Addition
    df['add result'] = addDF(df)
    print(df['add result'])
    print(df['add expectation'])
    # Subtraction
    df['subtract result'] = subtractDF(df)
    print(df['subtract result'])
    print(df['subtract expectation'])
    # Multiplication
    df['multiply result'] = multiplyDF(df)
    print(df['multiply result'])
    print(df['multiply expectation'])
    # Division
    df['divide result'] = divideDF(df)
    print(df['divide result'])
    print(df['divide expectation'])