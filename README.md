Put both .py files in a same folder
First run the code of search_text.py
Using postman or other api testing tools try post method http://127.0.0.1:5000(localhost)/search/text/
In body pass {"file_name": "testing .csv file name", "position": [50,50,1000,150]}
After heating this call you will get output as {"text": "State bank of  india"}.

Congrants!! you have done the testing of this api.
