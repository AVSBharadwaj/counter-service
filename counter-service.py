from flask import Flask, request, jsonify
import os

app = Flask(__name__)

# define path to file to store the counter 
COUNTER_FILE = "./data/counter.txt"

def read_counter():
    """
    reads the counter file for the counter value. If the file doesnot
    exist it returns 0.
    
    Returns:
        int: The current value of the counter
    """

    if os.path.exists(COUNTER_FILE):
        with open(COUNTER_FILE, "r") as f:
            return int(f.read().strip())
    else:
        return 0
    
def update_counter(counter):
    """
    updates the counter file with the passed counter argument
    
    Args: 
        counter (int): The new counter value to be stored in the file
    
    """
    with open(COUNTER_FILE,"w") as f:
        f.write(str(counter))

@app.route('/', methods=['GET','POST'])
def handle_request():

    counter = read_counter()

    if request.method == 'POST':
        counter+=1
        update_counter(counter)
        return f"updated the counter value. new value is ${counter}"
    else:
        return f"current posts request count is ${counter}"
    
@app.route('/health', methods=['GET'])
def health_check():

    try:
        read_counter()
        return jsonify({"status": "healthy"}), 200
    except Exception as e:
        return jsonify({"status": "unhealthy", "reson": str(e)}), 500
    
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=False)
    
    

    
