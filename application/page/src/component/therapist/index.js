import React, { Component } from 'react'
import {
    Button,
    Dropdown,
    Form,
    Input,
} from 'semantic-ui-react'
import {
    ageBracket,
    community,
    modality,
    therapyType
} from '../../data'
import { getOptions } from '../../util'
import {mock_therapist} from '../../test'
import TherapistTable from '../therapistTable'


class Therapist extends Component {
    state = {
        'address': '',
        'therapy': '',
        'modality': '',
        'community': '',
        'age': '',
    }

    handleChange = (e, value) => {
        this.setState({
            [value.name]: value.value
        })
    }

    handleSubmit = (e) => {
        e.preventDefault();
        let requestData = {
            'disease': this.props.disease,
            'address': this.state.address,
            'therapy': this.state.therapy,
            'modality': this.state.modality,
            'community': this.state.community,
            'age': this.state.age
        }

        const requestOptions = {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify(requestData)
        };      
        
        fetch('/api/therapist', requestOptions)
            .then(response => response.json())
            .then(data => {
                this.setState({data: data})
            }).catch(() => {
                const data = mock_therapist
                this.setState({data: data})
            })
    }

    render() {
        return (
            <div style={{ margin: '15px', marginTop: '30px' }}>
                <Form onSubmit={this.handleSubmit}>
                    <Form.Group inline>
                        <Input
                            style={{ width: '400px' }}
                            name='address'
                            placeholder='Please Input Address'
                            value={this.state.address}
                            onChange={this.handleChange}
                        />
                        <Dropdown search selection clearable
                            style={{ width: '330px', marginLeft: '10px' }}
                            name='therapy'
                            placeholder='Therapy Type'
                            options={getOptions(therapyType)}
                            value={this.state.therapy}
                            onChange={this.handleChange}
                        />
                    </Form.Group>
                    <Form.Group inline>
                        <Dropdown search selection clearable
                            style={{ width: '240px' }}
                            name='modality'
                            placeholder='Modality'
                            options={getOptions(modality)}
                            value={this.state.modality}
                            onChange={this.handleChange}
                        />
                        <Dropdown search selection clearable
                            style={{ width: '240px', marginLeft: '10px' }}
                            name='community'
                            placeholder='Community'
                            options={getOptions(community)}
                            value={this.state.community}
                            onChange={this.handleChange}
                        />
                        <Dropdown search selection clearable
                            style={{ width: '240px', marginLeft: '10px' }}
                            name='age'
                            placeholder='Age'
                            options={getOptions(ageBracket)}
                            value={this.state.age}
                            onChange={this.handleChange}
                        />
                    </Form.Group>
                    <Form.Field control={Button} color="blue">Find Therapist</Form.Field>
                </Form>
                <TherapistTable data={this.state.data}></TherapistTable>
            </div>
        )
    }
}

export default Therapist
