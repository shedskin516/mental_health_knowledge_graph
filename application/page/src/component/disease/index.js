import React from 'react'
import { Header } from 'semantic-ui-react'
import Therapist from '../therapist'


const RenderList = props => {
    let list = props.list
    if (list != null) {
        list = list.slice(1, -1).split(',')
        return (
            <div>
                <Header as='h4' style={{ marginTop: '10px' }}>{props.title}</Header>
                <p>
                    {list.map((item, index) => (
                        <span>
                            {index == 0 ? "" : ", "}
                            {item.trim().slice(1, -1)}
                        </span>
                    ))}
                </p>
            </div>
        );
    }
}


const Disease = ({ disease }) => {
    if (disease.detail) {
        if (disease.description != null || disease.symptoms != null || disease.risks != null || disease.drugs != null) {
            return (
                <div className='ui message'>
                    <div style={{ margin: '15px' }}>
                        <Header as='h4' style={{ marginTop: '10px' }}>Description</Header>
                        <p>{disease.description}</p>
                        <RenderList list={disease.symptoms} title="Symtoms"></RenderList>
                        <RenderList list={disease.risks} title="Risk Factors"></RenderList>
                        <RenderList list={disease.drugs} title="Drugs"></RenderList>
                    </div>
                    <Therapist disease={disease.disease}></Therapist>
                </div>
            )
        } else {
            return (
                <div className='ui message'>
                    <div style={{ margin: '15px' }}>
                        <p>No details of this disease in database. You can still search therapists.</p>
                    </div>
                    <Therapist disease={disease.disease}></Therapist>
                </div>
            )
        }
    }
}

export default Disease