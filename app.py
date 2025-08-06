from flask import Flask, render_template
import pandas as pd

app = Flask(__name__)

@app.route('/')
def index():
        
    # get table 1 from the csv provided
    df = pd.read_csv('Table_Input.csv')
    df.set_index("Index #", inplace=True)
    df["Value"] = pd.to_numeric(df["Value"], errors='coerce')

    table1 = df.reset_index().to_dict(orient='records')

    # use table 2 to calculate the values
    v1 = int(df.loc["A5", "Value"] + df.loc["A20", "Value"])
    v2 = int(df.loc["A15", "Value"] / df.loc["A7", "Value"])
    v3 = int(df.loc["A13", "Value"] * df.loc["A12", "Value"])

    table2 = [
    {"Category": "Alpha", "Value": v1},
    {"Category": "Beta", "Value": v2},
    {"Category": "Charlie", "Value": v3}
    ]

    return render_template("index.html", table1=table1, table2=table2)



if __name__ == '__main__':
    app.run(debug=True)



