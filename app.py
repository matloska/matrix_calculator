from flask import Flask, render_template, request, redirect
from matrix_manager import MatrixManager
import numpy as np

app = Flask(__name__)

@app.route("/", methods=['POST','GET'])
def matrices():
    """Renders a page on which we could add matrices"""
    
    # Get the number of rows and columns defined in the URL parameters
    rows_a = int(request.args.get('rows_a','3'))
    cols_a = int(request.args.get('cols_a','3'))
    rows_b = int(request.args.get('rows_b','3'))
    cols_b = int(request.args.get('cols_b','3'))

    if request.method == "POST":
        resp = request.form

        if 'calc_type' in resp:
            result = None

            # calc_type is passed after the calculation type was selected on the page 
            manager = MatrixManager()

            #create zero matrices to which the data will be inserted
            matrix_a = manager.create_zero_matrix(rows_a,cols_a)
            matrix_b = manager.create_zero_matrix(rows_b,cols_b)

            #filter only for data relevant for the matrix
            matrix_a_data = manager.filter_data_for_matrix_cells("A", resp.items())
            matrix_b_data = manager.filter_data_for_matrix_cells("B", resp.items())

            #assign values to the zero matrix
            matrix_a = manager.assign_values(matrix_a, matrix_a_data)
            matrix_b = manager.assign_values(matrix_b, matrix_b_data)

            #check for possible operations
            possible_operations = manager.possible_operations(matrix_a,matrix_b)

            #calculate if the selected operation is in the list of possible operations
            if resp['calc_type'] in possible_operations:
                if resp['calc_type'] == "add":
                    result = matrix_a + matrix_b
                elif resp['calc_type'] == "substract":
                    result = matrix_a - matrix_b
                else:
                    result = np.dot(matrix_a,matrix_b)

                return render_template('matrices.html', 
                            rows_a=rows_a, cols_a=cols_a,
                            rows_b=rows_b, cols_b=cols_b,
                            has_result=True,
                            result=result)
            
        #Redirect after changing the size of the matrices
        return redirect("/?rows_a="+str(resp['rows_a']) \
                        +"&cols_a="+str(resp['cols_a']) \
                        +"&rows_b="+str(resp['rows_b']) \
                        +"&cols_b="+str(resp['cols_b'])
                            )
    return render_template('matrices.html', 
                           rows_a=rows_a, cols_a=cols_a,
                           rows_b=rows_b, cols_b=cols_b)