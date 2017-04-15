import "isomorphic-fetch";

var url = "/run_tests";

class React_Tests extends React.Component {
	constructor(props) {
		super(props);
		this.state = {
			"test_output": "Running Tests"
		};
		this.run_tests = this.run_tests.bind(this);
		this.update_state = this.update_state.bind(this);
	}
	run_tests() {
		fetch(url).then(r => r.text())
	    .then(data => this.update_state(data))
	    .catch(e => console.log(e));
	}
	update_state(data) {
		this.state.test_output = data;
		this.forceUpdate();
	}

    render() {
        return (
        	<div>
    		  	<div className="col-md-3 text-center">
    		  		<a href="https://github.com/samuelbraley/idb">Repository</a>
    		  	</div>
    		  	<div className="col-md-3 text-center">
    		  		<a href="https://github.com/samuelbraley/idb/issues">Issue Tracker</a>
    		  	</div>
    		  	<div className="col-md-3 text-center">
    		  		<a href="http://docs.spacecowboys.apiary.io">Rest API</a>
    		  	</div>
    		  	<div className="col-md-3 text-center">
    		  		<a data-toggle="modal" data-target="#myModal" onClick={this.run_tests}>Run Unit Tests</a>
    		  	</div>
    		    <div>
    		        <div id="myModal" className="modal fade" role="dialog">
    		          <div className="modal-dialog">
    		            <div className="modal-content">
    		                <div className="modal-header">
    		                  <button type="button" className="close" data-dismiss="modal">&times;</button>
    		                  <h4 className="modal-title">Test Results</h4>
    		                </div>
    		                <div className="modal-body">
    		                  <pre>{this.state.test_output}</pre>
    		                </div>
    		                <div className="modal-footer">
    		                  <button type="button" className="btn btn-primary" onClick={this.run_tests}>Rerun tests</button>
    		                </div>
    		            </div>
    		          </div>
    		      </div>
    		    </div>
    		</div>
		);
    }
}

export default React_Tests;