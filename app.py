import os
from flask import Flask, render_template, request 
import json
from web3 import Web3, HTTPProvider
import ipfsApi
from datetime import datetime
import pickle

app = Flask(__name__)

global details, username, school_name, company_name
details=''
global contract

api = ipfsApi.Client(host='http://127.0.0.1', port=5001)

def readDetails(contract_type):
    global details
    details = ""
    blockchain_address = 'http://127.0.0.1:8545' #Blokchain connection IP
    web3 = Web3(HTTPProvider(blockchain_address))
    web3.eth.defaultAccount = web3.eth.accounts[0]
    compiled_contract_path = 'Evidence.json' 
    deployed_contract_address = '0xc92728dCaa98c3E788bb967bae0199fBe7444212' #hash address to access counter feit contract
    with open(compiled_contract_path) as file:
        contract_json = json.load(file)  # load contract info as JSON
        contract_abi = contract_json['abi']  # fetch contract's abi - necessary to call its functions
    file.close()
    contract = web3.eth.contract(address=deployed_contract_address, abi=contract_abi) #now calling contract to access data
    if contract_type == 'lab':
        details = contract.functions.getlab().call()
    if contract_type == 'hospital':
        details = contract.functions.gethospital().call()
    if contract_type == 'police':
        details = contract.functions.getpolice().call()
    if contract_type == 'court':
        details = contract.functions.getcourt().call()
    if contract_type == 'adduser':
        details = contract.functions.getuser().call()
    if len(details) > 0:
        if 'empty' in details:
            details = details[5:len(details)]    
      

def saveDataBlockChain(currentData, contract_type):
    global details
    global contract
    details = ""
    blockchain_address = 'http://127.0.0.1:8545'
    web3 = Web3(HTTPProvider(blockchain_address))
    web3.eth.defaultAccount = web3.eth.accounts[0]
    compiled_contract_path = 'Evidence.json' 
    deployed_contract_address = '0xc92728dCaa98c3E788bb967bae0199fBe7444212' #contract address
    with open(compiled_contract_path) as file:
        contract_json = json.load(file)  # load contract info as JSON
        contract_abi = contract_json['abi']  # fetch contract's abi - necessary to call its functions
    file.close()
    contract = web3.eth.contract(address=deployed_contract_address, abi=contract_abi)
    readDetails(contract_type)
    if contract_type == 'lab':
        details+=currentData
        msg = contract.functions.setlab(details).transact()
        tx_receipt = web3.eth.waitForTransactionReceipt(msg)
    if contract_type == 'hospital':
        details+=currentData
        msg = contract.functions.sethospital(details).transact()
        tx_receipt = web3.eth.waitForTransactionReceipt(msg)
    if contract_type == 'police':
        details+=currentData
        msg = contract.functions.setpolice(details).transact()
        tx_receipt = web3.eth.waitForTransactionReceipt(msg)
    if contract_type == 'court':
        details+=currentData
        msg = contract.functions.setcourt(details).transact()
        tx_receipt = web3.eth.waitForTransactionReceipt(msg)
    if contract_type == 'adduser':
        details+=currentData
        msg = contract.functions.setuser(details).transact()
        tx_receipt = web3.eth.waitForTransactionReceipt(msg)
    



@app.route('/AddLabAction', methods=['POST'])
def AddLabAction():
    if request.method == 'POST':
        global details
        username = request.form['t1']
        password = request.form['t2']
        contact = request.form['t3']
        email = request.form['t4']
        address = request.form['t5']
        readDetails('adduser')
        arr = details.split("\n")
        status = "none"
        for i in range(len(arr)-1):
            array = arr[i].split("#")
            if array[0] == 'Lab' and array[1] == username:
                status = username+" Username already exists"
                break
        if status == "none":
            data = "Lab#"+username+"#"+password+"#"+contact+"#"+email+"#"+address+"\n"
            saveDataBlockChain(data,"adduser")
            context = "Lab Incharge signup task completed"
            return render_template('LabRegister.html', data=context)
        else:
            context = status
            return render_template('LabRegister.html', data=context)


@app.route('/AddHospitalAction', methods=['POST'])
def AddHospitalAction():
    if request.method == 'POST':
        global details
        username = request.form['t1']
        password = request.form['t2']
        contact = request.form['t3']
        email = request.form['t4']
        address = request.form['t5']
        readDetails('adduser')
        arr = details.split("\n")
        status = "none"
        for i in range(len(arr)-1):
            array = arr[i].split("#")
            if array[0] == 'Hospital' and array[1] == username:
                status = username+" Username already exists"
                break
        if status == "none":
            data = "Hospital#"+username+"#"+password+"#"+contact+"#"+email+"#"+address+"\n"
            saveDataBlockChain(data,"adduser")
            context = "Hospital signup task completed"
            return render_template('HospitalRegister.html', data=context)
        else:
            context = status
            return render_template('HospitalRegister.html', data=context)

@app.route('/AddPoliceAction', methods=['POST'])
def AddPoliceAction():
    if request.method == 'POST':
        global details
        username = request.form['t1']
        password = request.form['t2']
        contact = request.form['t3']
        email = request.form['t4']
        address = request.form['t5']
        readDetails('adduser')
        arr = details.split("\n")
        status = "none"
        for i in range(len(arr)-1):
            array = arr[i].split("#")
            if array[0] == 'Police' and array[1] == username:
                status = username+" Username already exists"
                break
        if status == "none":
            data = "Police#"+username+"#"+password+"#"+contact+"#"+email+"#"+address+"\n"
            saveDataBlockChain(data,"adduser")
            context = "Police signup task completed"
            return render_template('PoliceRegister.html', data=context)
        else:
            context = status
            return render_template('PoliceRegister.html', data=context)

@app.route('/AddCourtAction', methods=['POST'])
def AddCourtAction():
    if request.method == 'POST':
        global details
        username = request.form['t1']
        password = request.form['t2']
        contact = request.form['t3']
        email = request.form['t4']
        address = request.form['t5']
        readDetails('adduser')
        arr = details.split("\n")
        status = "none"
        for i in range(len(arr)-1):
            array = arr[i].split("#")
            if array[0] == 'Court' and array[1] == username:
                status = username+" Username already exists"
                break
        if status == "none":
            data = "Court#"+username+"#"+password+"#"+contact+"#"+email+"#"+address+"\n"
            saveDataBlockChain(data,"adduser")
            context = "Court signup task completed"
            return render_template('CourtRegister.html', data=context)
        else:
            context = status
            return render_template('CourtRegister.html', data=context)


@app.route('/LabLoginAction', methods=['POST'])
def LabLoginAction():
    if request.method == 'POST':
        username = request.form['t1']
        password = request.form['t2']
        status = "none"
        readDetails('adduser')
        arr = details.split("\n")
        for i in range(len(arr)-1):
            array = arr[i].split("#")
            if array[0] == 'Lab' and array[1] == username and array[2] == password:
                status = "success"
                break
        if status == "success":
            context = "Welcome " + username
            return render_template('LabScreen.html', data=context)
        else:
            context = "Invalid Details"
            return render_template('LabLogin.html', data=context)


@app.route('/HospitalLoginAction', methods=['POST'])
def HospitalLoginAction():
    if request.method == 'POST':
        username = request.form['t1']
        password = request.form['t2']
        status = "none"
        readDetails('adduser')
        arr = details.split("\n")
        for i in range(len(arr)-1):
            array = arr[i].split("#")
            if array[0] == 'Hospital' and array[1] == username and array[2] == password:
                status = "success"
                break
        if status == "success":
            context = "Welcome " + username
            return render_template('HospitalScreen.html', data=context)
        else:
            context = "Invalid Details"
            return render_template('HospitalLogin.html', data=context)

@app.route('/PoliceLoginAction', methods=['POST'])
def PoliceLoginAction():
    if request.method == 'POST':
        username = request.form['t1']
        password = request.form['t2']
        status = "none"
        readDetails('adduser')
        arr = details.split("\n")
        for i in range(len(arr)-1):
            array = arr[i].split("#")
            if array[0] == 'Police' and array[1] == username and array[2] == password:
                status = "success"
                break
        if status == "success":
            context = "Welcome " + username
            return render_template('PoliceScreen.html', data=context)
        else:
            context = "Invalid Details"
            return render_template('PoliceLogin.html', data=context)


@app.route('/CourtLoginAction', methods=['POST'])
def CourtLoginAction():
    if request.method == 'POST':
        username = request.form['t1']
        password = request.form['t2']
        status = "none"
        readDetails('adduser')
        arr = details.split("\n")
        for i in range(len(arr)-1):
            array = arr[i].split("#")
            if array[0] == 'Court' and array[1] == username and array[2] == password:
                status = "success"
                break
        if status == "success":
            context = "Welcome " + username
            return render_template('CourtScreen.html', data=context)
        else:
            context = "Invalid Details"
            return render_template('CourtLogin.html', data=context)


@app.route('/AddEvidenceAction', methods=['POST'])
def AddEvidenceAction():
    if request.method == 'POST':
        eno = request.form['t1']
        edes = request.form['t2']
        uploaded_file = request.files['t3']
        filename = uploaded_file.filename
        myfile = uploaded_file.read()
        myfile = pickle.dumps(myfile)
        hashcode = api.add_pyobj(myfile)
        status = "none"
        readDetails('lab')
        arr = details.split("\n")
        for i in range(len(arr)-1):
            if arr[0] == eno:
                status = 'Evidence Already Existing.'
                return render_template('AddEvidence.html', data=status)
                break
        
        if status == "none":
            data = eno+"#"+edes+"#"+hashcode+"\n"
            saveDataBlockChain(data,'lab')
            context = 'Evidence Saved to blockchain with hashcode '+hashcode
            return render_template('AddEvidence.html',data=context)
        

def check_evidence(number):
    readDetails('hospital')
    arr = details.split("\n")
    for i in range(len(arr)-1):
        array = arr[i].split("#")
        if array[0] == number:
            return True
            break
    return False

@app.route('/CheckEvidence', methods=['GET', 'POST'])
def CheckEvidences():
    if request.method == 'GET':
        global number,des,evidence
        output = '<table border="1" align="center" width="100%">'
        font = '<font size="3" color="black">'
        headers = ['Evidence Number', 'Evidence Description', 'Evidence', 'Action']

        output += '<tr>'
        for header in headers:
            output += f'<th>{font}{header}{font}</th>'
        output += '</tr>'

        readDetails('lab')
        arr = details.split("\n")

        for i in range(len(arr) - 1):
            array = arr[i].split("#")

            output += '<tr>'
            for cell in array[0:2]:
                output += f'<td>{font}{cell}{font}</td>'
            content = api.get_pyobj(array[2])
            content = pickle.loads(content)
            if os.path.exists('static/evidence/'+array[2]):
                os.remove('static/evidence/'+array[2])
            with open('static/evidence/'+array[2], "wb") as file:
                file.write(content)
            file.close()
            output += '<td><img src=static/evidence/'+array[2]+'  width=500 height=500></img></td>'   
            action_cell = f'<td><a href="/SubmitReview?number={array[0]}&des={array[1]}&evidence={array[2]}">{font}Click Here to submit Feedback{font}</a></td>' if not check_evidence(array[0]) else f'<td>{font}Already Submitted{font}</td>'

            output += action_cell
            output += '</tr>'

        output += '</table><br/><br/><br/>'

        return render_template('CheckEvidence.html', data=output)

@app.route('/SubmitReview', methods=['GET', 'POST'])
def SubmitReview():
    global number,des,evidence

    if request.method == 'GET':
        number = request.args.get('number')
        des =  request.args.get('des')
        evidence = request.args.get('evidence')
        return render_template('SubmitReview.html')

    if request.method == 'POST':
        text = request.form['t1']
        data = number+"#"+des+"#"+text+"#"+evidence+"\n"
        saveDataBlockChain(data, "hospital")

        context = "Evidence Saved to blockchain."

        return render_template('SubmitReview.html', data=context)


def check_evidence1(number):
    readDetails('police')
    arr = details.split("\n")
    for i in range(len(arr)-1):
        array = arr[i].split("#")
        if array[0] == number:
            return True
            break
    return False

@app.route('/PoliceReview', methods=['GET', 'POST'])
def PoliceReview():
    if request.method == 'GET':
        global number,des,evidence,text
        output = '<table border="1" align="center" width="100%">'
        font = '<font size="3" color="black">'
        headers = ['Evidence Number', 'Evidence Description', 'Hospital Review','Evidence', 'Action']

        output += '<tr>'
        for header in headers:
            output += f'<th>{font}{header}{font}</th>'
        output += '</tr>'

        readDetails('hospital')
        arr = details.split("\n")

        for i in range(len(arr) - 1):
            array = arr[i].split("#")

            output += '<tr>'
            for cell in array[0:3]:
                output += f'<td>{font}{cell}{font}</td>'
            content = api.get_pyobj(array[3])
            content = pickle.loads(content)
            if os.path.exists('static/evidence/'+array[3]):
                os.remove('static/evidence/'+array[3])
            with open('static/evidence/'+array[3], "wb") as file:
                file.write(content)
            file.close()
            output += '<td><img src=static/evidence/'+array[3]+'  width=500 height=500></img></td>' 
            action_cell = f'<td><a href="/SubmitReview1?number={array[0]}&des={array[1]}&text={array[2]}&evidence={array[3]}">{font}Click Here to submit Feedback{font}</a></td>' if not check_evidence1(array[0]) else f'<td>{font}Already Submitted{font}</td>'

            output += action_cell
            output += '</tr>'

        output += '</table><br/><br/><br/>'

        return render_template('PoliceReview.html', data=output)

@app.route('/SubmitReview1', methods=['GET', 'POST'])
def SubmitReview1():
    global number,des,evidence,text

    if request.method == 'GET':
        number = request.args.get('number')
        des =  request.args.get('des')
        text =  request.args.get('text')
        evidence = request.args.get('evidence')
        return render_template('SubmitReview1.html')

    if request.method == 'POST':
        review = request.form['t1']
        data = number+"#"+des+"#"+text+"#"+review+"#"+evidence+"\n"
        saveDataBlockChain(data, "police")

        context = "Evidence Saved to blockchain."

        return render_template('SubmitReview1.html', data=context)

@app.route('/CourtReview', methods=['GET', 'POST'])
def CourtReview():
    if request.method == 'GET':
        global number,des,evidence,text
        output = '<table border="1" align="center" width="100%">'
        font = '<font size="3" color="black">'
        headers = ['Evidence Number', 'Evidence Description', 'Hospital Review','Police Review','Evidence']

        output += '<tr>'
        for header in headers:
            output += f'<th>{font}{header}{font}</th>'
        output += '</tr>'

        readDetails('police')
        arr = details.split("\n")

        for i in range(len(arr) - 1):
            array = arr[i].split("#")

            output += '<tr>'
            for cell in array[0:4]:
                output += f'<td>{font}{cell}{font}</td>'
            content = api.get_pyobj(array[4])
            content = pickle.loads(content)
            if os.path.exists('static/evidence/'+array[4]):
                os.remove('static/evidence/'+array[4])
            with open('static/evidence/'+array[4], "wb") as file:
                file.write(content)
            file.close()
            output += '<td><img src=static/evidence/'+array[4]+'  width=500 height=500></img></td>' 
            output += '</tr>'

        output += '</table><br/><br/><br/>'

        return render_template('CourtReview.html', data=output)


@app.route('/CourtLogin', methods=['GET', 'POST'])
def CourtLogin():
    if request.method == 'GET':
       return render_template('CourtLogin.html', msg='')

@app.route('/CourtRegister', methods=['GET', 'POST'])
def CourtRegister():
    if request.method == 'GET':
       return render_template('CourtRegister.html', msg='')

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'GET':
       return render_template('index.html', msg='')

@app.route('/CheckEvidence', methods=['GET', 'POST'])
def CheckEvidence():
    if request.method == 'GET':
       return render_template('CheckEvidence.html', msg='')

@app.route('/CourtScreen', methods=['GET', 'POST'])
def CourtScreen():
    if request.method == 'GET':
       return render_template('CourtScreen.html', msg='')

@app.route('/HospitalLogin', methods=['GET', 'POST'])
def HospitalLogin():
    if request.method == 'GET':
       return render_template('HospitalLogin.html', msg='')

@app.route('/HospitalRegister', methods=['GET', 'POST'])
def HospitalRegister():
    if request.method == 'GET':
       return render_template('HospitalRegister.html', msg='')

@app.route('/HospitalScreen', methods=['GET', 'POST'])
def HospitalScreen():
    if request.method == 'GET':
       return render_template('HospitalScreen.html', msg='')

@app.route('/LabLogin', methods=['GET', 'POST'])
def LabLogin():
    if request.method == 'GET':
       return render_template('LabLogin.html', msg='')

@app.route('/LabRegister', methods=['GET', 'POST'])
def LabRegister():
    if request.method == 'GET':
       return render_template('LabRegister.html', msg='')

@app.route('/LabScreen', methods=['GET', 'POST'])
def LabScreen():
    if request.method == 'GET':
       return render_template('LabScreen.html', msg='')

@app.route('/PoliceLogin', methods=['GET', 'POST'])
def PoliceLogin():
    if request.method == 'GET':
       return render_template('PoliceLogin.html', msg='')

@app.route('/PoliceRegister', methods=['GET', 'POST'])
def PoliceRegister():
    if request.method == 'GET':
       return render_template('PoliceRegister.html', msg='')

@app.route('/PoliceScreen', methods=['GET', 'POST'])
def PoliceScreen():
    if request.method == 'GET':
       return render_template('PoliceScreen.html', msg='')

@app.route('/index', methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
       return render_template('index.html', msg='')

@app.route('/AddEvidence', methods=['GET', 'POST'])
def AddEvidences():
    if request.method == 'GET':
       return render_template('AddEvidence.html', msg='')


if __name__ == '__main__':
    app.run()  