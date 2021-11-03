from flask import Flask,request
from get_text import text

app = Flask(__name__)

@app.route('/')
def test():
	return {"text":"Hello docsumo"}
	
	
@app.route('/search/text/',methods=['POST'])
def search_text():
    request_data = request.get_json()
    filename=request_data["file_name"]
    position=request_data["position"]
    return {"text":"{0}".format(text(filename,position))}
#except:
#return {"error":"Something went wrong"}
	
if __name__ == '__main__':
    app.run()