import React, { Component } from 'react';
import { Jumbotron, Button, Collapse, Col, Row, Card, CardGroup, CardImg, CardBody, CardTitle, CardText } from 'reactstrap';
import Mydropdown from './mydropdown'
import ContactUs from './contactus'

class Jumbo extends Component {
  constructor(props) {
    super(props);
    this.toggle = this.toggle.bind(this);
    this.state = { collapse: false };
  }
//set the toggle
  toggle() {
    this.setState({ collapse: !this.state.collapse });
  }


  render(props){
    return (
      <div>
        <Jumbotron className='myjumbotron' id='superjumbo'>
      	<div className="container" id="jumbobutton">
        		<div>
          	<h1 id='iot'>IOT</h1>
      	</div>
      		<div>
        			<h3>Recruiting Ideas for the future</h3>
        			 <Button className="btn-secondary" onClick={this.toggle}>Get involved</Button>
      		</div>
    		</div>

      	
        </Jumbotron>
        <Collapse isOpen={this.state.collapse}>
          <div>
          <CardGroup>
            <Col sm={4}>
              <Mydropdown label='Hilliard Projects'>{<ContactUs title="How can you help with Hilliard Projects"/>}</Mydropdown>
                <Card>
                  <CardBody id='jumbocard'>
                  </CardBody>
                  <CardImg top width="100%" src="https://placeholdit.imgix.net/~text?txtsize=33&txt=318%C3%97180&w=318&h=180" alt="Card image cap" />
                </Card>
              </Col>
            
            
              <Col sm={4}>
              <Mydropdown label='Educational Outreach'>{<ContactUs title="How can you help with Educational Outreach?"/>}</Mydropdown>
                <Card>
                  <CardBody id='jumbocard'>
                  </CardBody>
                  <CardImg top width="100%" src="https://placeholdit.imgix.net/~text?txtsize=33&txt=318%C3%97180&w=318&h=180" alt="Card image cap" />
                </Card>
              </Col>
            
            
              <Col sm={4}>
              <Mydropdown label='Production Projects'>{<ContactUs title="How can you help with production products?"/>}</Mydropdown>
                <Card>
                  <CardBody id='jumbocard'>
                  </CardBody>
                  <CardImg top width="100%" src="https://placeholdit.imgix.net/~text?txtsize=33&txt=318%C3%97180&w=318&h=180" alt="Card image cap" />
                </Card>
              </Col>
            
            </CardGroup>
            <Row></Row>
          </div>
          
        </Collapse>
      </div>
          
    )
  }
}
export default Jumbo