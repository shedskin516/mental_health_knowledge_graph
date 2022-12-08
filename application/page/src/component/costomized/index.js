import React, { Component } from 'react'
import {
  Form,
} from 'semantic-ui-react'
import {mock_therapist} from '../../test'
import TherapistTable from '../therapistTable'


class Basic extends Component {
  state = {
    'trouble': ''
  }

  handleChange = (e, value) => {
    this.setState({
      [value.name]: value.value
    })
  }

  handleSubmit = (e) => {
    e.preventDefault();

    const requestOptions = {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({'trouble': this.state.trouble})
    };      
    
    fetch('/api/analysis', requestOptions)
        .then(response => response.json())
        .then(data => {
            console.log(data.length)
            this.setState({data: data})
        }).catch(() => {
            console.log('error')
            const data = mock_therapist
            this.setState({data: data})
        })
  }

  render() {
    return (
      <div>
        <Form onSubmit={this.handleSubmit}>
          <Form.TextArea
            name='trouble'
            value={this.state.trouble}
            style={{ minHeight: 150 }}
            onChange={this.handleChange}
            label='Please tell us what troubles you have these days'
          />
          <Form.Button color='blue'>Submit</Form.Button>
        </Form>
        {
          this.state.data && 
          <p style={{margin: '30px 0 0', fontWeight: 'bold'}}>
            These are recommended therapists for you.
          </p>
        }
        <TherapistTable data={this.state.data}></TherapistTable>

      </div>
    )
  }
}

export default Basic
