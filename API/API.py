import flask
from flask import url_for,Flask,render_template


import pandas as pd
files_df=pd.read_csv("result_model_2.csv")




app = flask.Flask(__name__,template_folder='template')

@app.route('/',methods=['GET','POST'])
def index():
    message= ''
    if flask.request.method == 'POST':
        input1 = flask.request.form['Shop_id']
        input2 = flask.request.form['Item_id']
        
        query_task=files_df[(files_df.shop_id==int(input1)) & (files_df.item_id==int(input2))]
        return_text_pred=query_task.result.values
        return_text_actual=query_task.date_block_33.values

        
        
        message = "predict"+str(return_text_pred) , "Actual"+str(return_text_actual)
        
        
        
    return flask.render_template("index.html",message=message)

if __name__=='__main__':
     app.run(host="localhost",port=8000, debug=True)

