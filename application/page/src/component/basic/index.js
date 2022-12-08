import React, { Component } from 'react'
import {
    Button,
    Dropdown,
    Form
} from 'semantic-ui-react'
import { disease } from '../../data'
import { getOptions } from '../../util'
import Disease from '../disease';


class Basic extends Component {
    state = {
        'disease': ''
    }

    handleChange = (e, value) => {
        this.setState({
            [value.name]: value.value
        })
        // clear previous result
        if(value.name == 'disease' && !value.value) {
            this.setState({ 'detail': false })
        }
    }

    handleSubmit = (e) => {
        e.preventDefault();
        if (!this.state.disease) {
            return
        }
        fetch(`/api/disease/${this.state.disease}`).then(response => 
            response.json().then(data => {
                this.setState(data)
                this.setState({ 'detail': true })
            }).catch(() => {
                const mockdata = {
                    "description": "mock data",
                    "drugs": null,
                    "risks": null,
                    "symptoms": null
                }
                this.setState(mockdata)
                this.setState({ 'detail': true })
            })
        );
    }

    render() {
        return (
            <div style={{minHeight:'800px'}}>
                <Form onSubmit={this.handleSubmit}>
                    <Form.Group inline>
                        <Form.Field>
                            <label>Disease</label>
                            <Dropdown search selection clearable
                                style={{ width: '330px' }}
                                name='disease'
                                placeholder='Please input disease'
                                options={getOptions(disease)}
                                value={this.state.disease}
                                onChange={this.handleChange}
                            />
                        </Form.Field>
                        <Form.Field control={Button} basic color="blue">Search</Form.Field>
                    </Form.Group>
                </Form>

                <Disease disease={this.state} />
            </div>
        )
    }
}

export default Basic
