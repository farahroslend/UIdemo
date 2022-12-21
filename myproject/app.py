from flask import Flask, render_template, request, make_response
from openpyxl import load_workbook
import pandas as pd


app = Flask("Excel_Web-App")


@app.route("/", methods=["GET", "POST"])
def form():
	    if request.method == "POST" or "z" in request.form:
			# x = request.form.get('z')
	        # x = int(x)
	        # dataset = pd.read_excel("data/dummy_data.xlsx")
	        # Stream = dataset["Stream"]
	        # dataset['Input'] = dataset['Input'] * (x/100)
	        # filename="Updated_file.xlsx"
	        # dataset.to_excel(filename)
			# return render_template("view_input_data.html", sheet=sheet)
	        return "PROMPT: File to be absorbed into BE"
	        
	        #return "Data has been Updated Successfully in Updated_file.xlsx!! Check it out!!"			
		

	    return render_template("form.html") 