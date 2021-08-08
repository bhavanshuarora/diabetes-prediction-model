from keras.models import load_model
from flask import Flask, render_template, request
app=Flask("mydiaapp")
model= load_model("diabetes-model.h5")
@app.route("/")
def home():
	return "Diabetes prediction App"
@app.route("/myform")
def myform():
	return render_template("myform.html")
@app.route("/predict",methods=["GET"])
def predict():
	Pregnancies=request.args.get("Pregnancies")
	Glucose=request.args.get("Glucose")
	BloodPressure=request.args.get("BloodPressure")
	SkinThickness=request.args.get("SkinThickness")
	Insulin=request.args.get("Insulin")
	BMI=float(request.args.get("BMI"))
	DiabetesPedigree=float(request.args.get("DiabetesPedigree"))
	Age=request.args.get("Age")
	output = model.predict([[int(Pregnancies),int(Glucose),int(BloodPressure),int(SkinThickness),int(Insulin),float(BMI),float(DiabetesPedigree),int(Age)]])
	output = round(output[0][0])
	if(output==0):
		return ("""Congratulations you do not have diabetes.
Stay Safe stay healthy""")
	else:
		return (""" there is an high chance you have diabetes 
consult your doctor immediately""") 

app.run(host="172.17.0.2",port=5001)
