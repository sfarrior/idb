import Highlighter from 'react-highlight-words'

class ModelListItem extends React.Component {
	constructor(props) {
		super(props);
		var base_url = "/" + this.props.model.model_type + "/";
		var link = base_url + this.props.model.pid;
		if (this.props.search !== undefined){
			link += "?q=" + this.props.search;
		}
		this.state = {
			style: {
						width: '400px',
						height: '400px'
					},
			image_url: "/undefined",
			link: link
		}
		var image_url = "/api/v1" + base_url + this.props.model.pid + "/image";
		fetch(image_url)
	    .then((response) => response.json())
	    .then((responseJson) => {
	        this.setState({ 
	        	image_url: responseJson.img_url,
	        })})
		.catch((error) => {console.error(error);})
	}
	highlight(name, search) {
		if (search === undefined){
			search = "";
		}
		search = search.split('+');

		return (<Highlighter className='h3' searchWords={search} textToHighlight={name}/>);
	}
	render() {
		return (
			<div className="col-lg-4 col-md-6 col-sm-12 text-center model-list-item">
				<a href={this.state.link}>
					<img className="img-thumbnail about-image" style={this.state.style} src={this.state.image_url} />
					<br/>
					{this.highlight(this.props.model.name, this.props.search)}
				</a>
			</div> 
			);
	}
};


export default ModelListItem;