import React from "react";
import Grid from "@material-ui/core/Grid";
import Button from "@material-ui/core/Button";

//import OutlinedDropDown from "../../common/OutlinedDropdown";
import OutlinedTextArea from "../../common/OutlinedTextArea";
import FileUploader from "../../common/FileUploader";

import { ServiceDefinition } from "./adr_pb_service";

//The following, used as React object's state, may be set for dynamically updating components (e.g., btn disabling)
const initialUserInput = {
  methodIndex: "0",
  methodNames: [
    {
      label: "AccDecRob",
      content: "adr",
      value: "0",
    }
  ],
  s: "1,2,3,4,5",
  uploadedFile: null,
  isValid: {
    uploadedFile: false,
    validJSON: false,
  },
  invokeBtnDisabled: true
};

export default class TestRiskAwareAssessment extends React.Component {
  constructor(props) {
    super(props);
    console.log("<<<<<<<<<<<<<< CTOR");
    this.submitAction = this.submitAction.bind(this);
    this.handleFileUpload = this.handleFileUpload.bind(this);
    this.handleFormUpdate = this.handleFormUpdate.bind(this);
    this.uploadedFile = null;
    //this.invokeBtnDisabled= "true";
    this.state = { ...initialUserInput };
    //this.state = { ...initialUserInput, this.invokeBtnDisabled };
  }

  handleFormUpdate(event) {
    this.setState({
      [event.target.name]: event.target.value,
    });
  }

  onKeyPressvalidator(event) {
    const keyCode = event.keyCode || event.which;
    if (!(keyCode === 8 || keyCode === 46) && (keyCode < 48 || keyCode > 57)) {
      event.preventDefault();
    } else {
      let dots = event.target.value.split(".");
      if (dots.length > 1 && keyCode === 46) event.preventDefault();
    }
  }

  submitAction() {
    const { methodIndex, methodNames } = this.state;
    //const methodDescriptor = Calculator[methodNames[methodIndex].content];
    const methodDescriptor = ServiceDefinition[methodNames[methodIndex].content];
    console.log(this.state)
    console.log(methodNames)
    const request = new methodDescriptor.requestType();
    console.log(request)
    //request.setA(this.state.a);
    //request.setB(this.state.b);

    //Following confirmed defined in adr_pb.js
    console.log("<<<<<<<<<<< submitAction: s = " + this.state.s);
    request.setS(this.state.s);

    const props = {
      request,
      onEnd: ({ message }) => {
        //console.log("DEBUGGER ==========");debugger;
        //this.setState({ ...initialUserInput, response: { value: message.getS() } });
        //this.setState({ ...initialUserInput, response: { a: message.getA(), d: message.getD(), r: message.getR() } });
        //this.setState({ ...initialUserInput, response: "a: "+toString(message.getA()) + ", d:" + toString(message.getD()) + ", r:"+toString(message.getR()) });
        //this.setState({ ...initialUserInput, response: "a: "+message.getA().toString() + ", <br>d:" + message.getD().toString() + ", r:"+message.getR().toString() });
        //this.setState({ ...initialUserInput, response: "a: "+message.getA().toString() + ", \nd:" + message.getD().toString() + ", r:"+message.getR().toString() });
        //this.setState({ ...initialUserInput, response: { a: message.getA().toString(), d: message.getD().toString(), r: message.getR().toString()} });
        let imgb64 = message.getImg();
        imgb64.length % 4 > 0 && (imgb64 += "=".repeat(4 - (imgb64.length % 4)));
        
        console.log("<<<<<<<<<<<<<<<<< submitAction: img = "+imgb64.slice(0,10)+" (...) "+imgb64.slice(-10));
        this.setState({ ...initialUserInput, response: { 
            a: message.getA().toPrecision(4), 
            d: message.getD().toPrecision(4), 
            r: message.getR().toPrecision(4), 
            img: imgb64,
            numRows: message.getNumr(), 
            numCols: message.getNumc()
        } });
      },
    };
    this.props.serviceClient.unary(methodDescriptor, props);
  }
  
  validateJSON(value) {
    let user_value = "";
    try {
      user_value = JSON.parse(value);
    } catch (error) {
      this.setState({ internal_error: error.toString() });
    }
    return user_value;
  }  

  setValidationStatus(key, valid) {
    if (this.state.isValid[key] !== valid) {
      this.setState(state => {
        const isValid = Object.assign({}, state.isValid);
        isValid[key] = valid;
        return { isValid };
      });
    }   
  }   


  handleFileUpload(files) {
    this.setState( {uploadedFile: null });
    if (files.length) {
      const fileReader = new FileReader();
      fileReader.readAsDataURL(files[0]);
      fileReader.onload = () => {
        let encoded = fileReader.result.replace(/^data:(.*;base64,)?/, "");
        encoded.length % 4 > 0 && (encoded += "=".repeat(4 - (encoded.length % 4)));
        let rawText = atob(encoded);

        // Check for invalid inputs
        let re = /[^0-9,.-\s\ne]/;
        if (re.test(rawText)){
          let match = rawText.match(re);
          throw new ValidationError("the input file contains invalid characters.");
        }

        // Check for file size
        if (rawText.length > 3145500){
          throw new ValidationError("the input file is too large.");
        }
        
        // Loop through each row
        for (const row_string of rawText.split("\n")) {
          
          // Split each column
          let row = row_string.split(",");
          let n_classes = row.length -1;

          // Check if last column is int. Ignore if last row is empty string.
          if ((parseFloat(row[n_classes]) % 1 != 0) && (row[n_classes] != "")){
            console.log(row)
            throw new ValidationError("the last column should be an integer.");
          }
          
          // Class label should be between 1 and n_classes
          if (parseInt(row[n_classes]) > n_classes){
            throw new ValidationError("the class label should be between 1 and " + n_classes.toFixed(0) + '.');
          }
        }
        
        let numRows = rawText.split(/\r\n|\r|\n/).length -1;
        let numCols = rawText.split(/\r\n|\r|\n/)[0].split(",").length;
        let user_value = this.validateJSON(atob(encoded));
        console.log("<<<<<<<<<<<<<<<<<< TEST >>>>>>>>>>>>>>>>>>>>>>>>");
        //console.log("<<<<<<<<<<<<<<<<<< enc: " + encoded.toString());
        //console.log("<<<<<<<<<<<<<<<<<< rawText: " + rawText);
        //console.log("<<<<<<<<<<<<<<<<<< numRows: " + numRows.toString());
        //console.log("<<<<<<<<<<<<<<<<<< numCols: " + numCols.toString());
        //let condition = this.validateValues(user_value);
        //this.setValidationStatus("validJSON", condition);
        this.setValidationStatus("validJSON", true);
        this.setState({ uploadedFile: files[0] });
        //this.setState({ s: encoded.toString() });
        this.setState({ s: numRows.toString()+","+numCols.toString()+","+encoded.toString() });
        //this.invokebtn.disabled = "false";
        //this.invokebtn.setState({disabled: "false"});
        //console.log(this.invokebtn);
        //this.invokeBtnDisabled = "false";
        this.setState({invokeBtnDisabled: false});
        //console.log("this.invokeBtnDisabled: " + this.invokeBtnDisabled);
        //console.log("document.getElementById('invokebtn').disabled: " + document.getElementById("invokebtn").disabled);
        //console.log("this.state: " + this.state);
        //document.getElementById("invokebtn").setState({disabled: "false"});
        //document.getElementById("invokebtn").disabled=false;
      };
    }
  }



  handleFocus = event => event.target.select();

//              <OutlinedTextArea
//                id="input_s"
//                name="s"
//                label="Input string"
//                type="text"
//                fullWidth={false}
//                value={this.state.s}
//                rows={1}
//                onChange={this.handleFormUpdate}
//                onKeyPress={e => this.onKeyPressvalidator(e)}
//                onFocus={this.handleFocus}
//              />
  renderForm() {
    //const invokeBtnDisabled = this.invokeBtnDisabled;
    return (
      <React.Fragment>
        <Grid container direction="column" alignItems="center" justify="center">
          <Grid item xs={6} container spacing={1}>
            <Grid item xs>
              <br/>
              Use the below to select a CSV file to upload.
              <br/><br/>
              Assumed format is N+1 columns per record, and M records as the number of rows in the file.  For each record, the first N columns are the respective probabilities (having value [0.0, 1.0]) associated with each categorical class, and the final column has the integer index (starting at "1") of the outcome (or "true") class for that record. <br/><br/>
              It is assumed NO HEADER ROW exists in the .csv file.
              <br/>
              <br/>
              <FileUploader
                name="csv"
                type="file"
                uploadedFiles={this.state.uploadedFile} 
                handleFileUpload={this.handleFileUpload}
                setValidationStatus={valid => this.setValidationStatus("uploadedFile",valid)}
                fileAccept=".csv"
              />
            </Grid>
          </Grid>

          <Grid item xs={12} style={{ textAlign: "center" }}>
            <Button variant="contained" color="primary" onClick={this.submitAction} id="invokebtn" disabled={this.state.invokeBtnDisabled}>
              Invoke
            </Button>
          </Grid>
        </Grid>
      </React.Fragment>
    );
  }
//            <Button variant="contained" color="primary" onClick={this.submitAction} id="invokebtn" disabled={this.getState("invokeBtnDisabled")}>
//            <Button variant="contained" color="primary" onClick={this.submitAction} id="invokebtn" disabled={invokeBtnDisabled}>

  parseResponse() {
    const { response } = this.state;
    if (typeof response !== "undefined") {
      if (typeof response === "string") {
        //return response;
        return (
          <div>
            <h4>Risk Aware Assessment Results</h4>
            <div style={{padding: "10px 10px 0 10px", fontSize: "14px", color:"#9b9b9b"}}>
              Results: <span style={{color: "#222222"}}>{response}</span>
            </div>
          </div>
        );
      } else if (typeof response === "object") {
        //let imgsrc='"data:img/png;base64,'+response.img+'"';
        let imgsrc="data:img/png;base64,"+response.img;
        const atsymbol = '&#64;';
        console.log("<<<<< imgsrc: "+imgsrc.slice(0,25)+" (...) "+imgsrc.slice(-25));
        return (
          <div>
            <h4>Risk Aware Assessment Results</h4>
            <div style={{padding: "0 10px 0 10px", fontSize: "14px", color:"#777777"}}>
              Results computed from processing {response.numRows} records, with each record having respective probabilities for each of {response.numCols-1} categories.
              <br/>
              <br/>
              <span style={{color: "#222222"}}>Accuracy: {response.a.toString()}</span>
              <br/>
Accuracy metric is consistent with the log score of information theory and is computed by the geometric mean (which is the zeroth power of the generalized mean) of the probabilities.  
              <br/>
              <br/>
              <span style={{color: "#222222"}}>Decisiveness: {response.d.toString()}</span>
              <br/>
Decisiveness is measured by the arithmetic mean, which is the first power of the GM. Decisiveness is closely related to the classification performance of an algorithm; i.e. the performance of making decisions rather than the accuracy of the probabilities.
              <br/>
              <br/>
              <span style={{color: "#222222"}}>Robustness: {response.r.toString()}</span>
              <br/>
Because Decisiveness is a weak measurement, it is necessary to include a stronger metric to make sure that an algorithm will be robust against deviations from the original training set distribution. To measure the Robustness, Photrek utilizes the -2/3rds generalized-mean. The negative power inverts the probabilities, thus giving more weight to low probabilities.  This provides a metric of the performance of poor forecasts with low probability. 
              <br/>
              <br/>
              <center><img src={imgsrc} width="800" text-align='center' display='block'/></center>
              <br/>
Thank you for using Risk Aware Assessment by <a href="https://photrek.io">Photrek</a>. Should you have experienced difficulty using or understanding results of this service, please contact us at <a href="mailto:kenric.nelson@photrek.io">kenric.nelson@photrek.io</a>.
            </div>
          </div>
        );
      }
      //console.log("<<<<<<<<<<<<<<<<<<<<< Response type: "+typeof response);
      //return response.value;
    }
  }
//              Img str: {response.img.slice(0,20)} (...) {response.img.slice(-20)}

//              <img src='data:img/png;base64,${response.img}'/> 
//              <img src="data:img/png;base64,${response.img}"/> 
//              <img src="data:img/png;base64,{response.img}"/> 

//              Img str: {response.img.toString()}


//              <img src="data:img/png;base64, 
//iVBORw0KGgoAAAANSUhEUgAAABgAAAAYCAAAAADFHGIkAAABHklEQVQoz43RPUvDQBgH8H9yl2hz
//tlBiSJXSKjUK+iVcRPxYfhNHZwfBwcnFRcFNkIKWLFqjMXBJuLycQ68XkSDe+uOe//NCNy20vYLK
//k1a4pHJG2kBQ2foB8g9QwqNEwO65bAk1AKAK4z4tzvjj+fuQAEC9KFVNKfmEmZOD04ubCWkyQisz
///d3+rTPoHpf3Yw38y6GTfSDPPza8wzvOlhD56fpeBQAIDefoWkPi0VGp+nwdeIkuJSR1KgVpJkUT
//bsnKUFBnspnctqtUDQYzK2wNvdpKVhVY2VtXg/uyU8ZrAAAi8DDUwDqxK5IVYkCWCG3WhI+eDB9i
//0W4UqCVKACSYzbeYAcmfO8HPJYJs8/m0gNUbs9+HYuzfF7xql28IqYY3SRNSpAAAAABJRU5ErkJg
//gg=="/>






//              Results: <span style={{color: "#222222"}}>{response}</span>

//              <img src="data:img/png;base64, 
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"/>


//                <img src="data:image/jpeg;base64, 0yMDIzLTAxLTMxIDE3OjU2OjU1LS0gIGh0dHBzOi8vaXMzLXNzbC5tenN0YXRpYy5jb20vaW1hZ2UvdGh1bWIvUHVycGxlMTEyL3Y0LzY0LzYyLzQxLzY0NjI0MTkzLTc0YmEtNzZlOC1jZmRjLTA1YTc2YjE3NDRkNy9BcHBJY29uLTAtMC0xeF9VMDA3ZW1hcmtldGluZy0wLTAtMC0xMC0wLTAtc1JHQi0wLTAtMC1HTEVTMl9VMDAyYzAtNTEyTUItODUtMjIwLTAtMC5wbmcvNTEyeDUxMmJiLmpwZwpSZXNvbHZpbmcgaXMzLXNzbC5tenN0YXRpYy5jb20gKGlzMy1zc2wubXpzdGF0aWMuY29tKS4uLiAyMy41Ni44LjI2LCAyNjAwOjE0MDI6OTgwMDo2OTY6OjJhMSwgMjYwMDoxNDAyOjk4MDA6NjkzOjoyYTEsIC4uLgpDb25uZWN0aW5nIHRvIGlzMy1zc2wubXpzdGF0aWMuY29tIChpczMtc3NsLm16c3RhdGljLmNvbSl8MjMuNTYuOC4yNnw6NDQzLi4uIGNvbm5lY3RlZC4KSFRUUCByZXF1ZXN0IHNlbnQsIGF3YWl0aW5nIHJlc3BvbnNlLi4uIDIwMCBPSwpMZW5ndGg6IDM4ODU2ICgzOEspIFtpbWFnZS9qcGVnXQpTYXZpbmcgdG86IOKAmDUxMng1MTJiYi5qcGfigJkKCiAgICAgMEsgLi4uLi4uLi4uLiAuLi4uLi4uLi4uIC4uLi4uLi4uLi4gLi4uLi4uLiAgICAgICAgICAgICAgMTAwJSAgNDE4Sz0wLjA5cwoKMjAyMy0wMS0zMSAxNzo1NzowMiAoNDE4IEtCL3MpIC0g4oCYNTEyeDUxMmJiLmpwZ+KAmSBzYXZlZCBbMzg4NTYvMzg4NTZdCgo="/>

// <!--<img src="data:image/jpeg;base64, 0yMDIzLTAxLTMxIDE3OjU2OjU1LS0gIGh0dHBzOi8vaXMzLXNzbC5tenN0YXRpYy5jb20vaW1hZ2UvdGh1bWIvUHVycGxlMTEyL3Y0LzY0LzYyLzQxLzY0NjI0MTkzLTc0YmEtNzZlOC1jZmRjLTA1YTc2YjE3NDRkNy9BcHBJY29uLTAtMC0xeF9VMDA3ZW1hcmtldGluZy0wLTAtMC0xMC0wLTAtc1JHQi0wLTAtMC1HTEVTMl9VMDAyYzAtNTEyTUItODUtMjIwLTAtMC5wbmcvNTEyeDUxMmJiLmpwZwpSZXNvbHZpbmcgaXMzLXNzbC5tenN0YXRpYy5jb20gKGlzMy1zc2wubXpzdGF0aWMuY29tKS4uLiAyMy41Ni44LjI2LCAyNjAwOjE0MDI6OTgwMDo2OTY6OjJhMSwgMjYwMDoxNDAyOjk4MDA6NjkzOjoyYTEsIC4uLgpDb25uZWN0aW5nIHRvIGlzMy1zc2wubXpzdGF0aWMuY29tIChpczMtc3NsLm16c3RhdGljLmNvbSl8MjMuNTYuOC4yNnw6NDQzLi4uIGNvbm5lY3RlZC4KSFRUUCByZXF1ZXN0IHNlbnQsIGF3YWl0aW5nIHJlc3BvbnNlLi4uIDIwMCBPSwpMZW5ndGg6IDM4ODU2ICgzOEspIFtpbWFnZS9qcGVnXQpTYXZpbmcgdG86IOKAmDUxMng1MTJiYi5qcGfigJkKCiAgICAgMEsgLi4uLi4uLi4uLiAuLi4uLi4uLi4uIC4uLi4uLi4uLi4gLi4uLi4uLiAgICAgICAgICAgICAgMTAwJSAgNDE4Sz0wLjA5cwoKMjAyMy0wMS0zMSAxNzo1NzowMiAoNDE4IEtCL3MpIC0g4oCYNTEyeDUxMmJiLmpwZ+KAmSBzYXZlZCBbMzg4NTYvMzg4NTZdCgo="></img>-->

  renderComplete() {
    const response = this.parseResponse();
    return (
      <Grid item xs={12} container justify="center">
        <p style={{ fontSize: "20px" }}>Response from service: {response} </p>
      </Grid>
    );
  }

  render() {
    if (this.props.isComplete) return <div>{this.renderComplete()}</div>;
    else {
      return <div>{this.renderForm()}</div>;
    }
  }
}

class ValidationError extends Error {
  constructor(message) {
    super(message); // (1)
    this.name = "ValidationError"; // (2)
  }
}
