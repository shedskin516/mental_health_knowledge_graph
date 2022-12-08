import React from "react";
import { Table, Popup } from "semantic-ui-react";
import TherapistPagination from "./pagination";
import LinesEllipsis from 'react-lines-ellipsis'


const RenderBody = props => {

    let list = props.rowData.slice(props.offset, props.offset + props.limit)

    return (
        <Table.Body>
            {
                list.map((item, index) => (
                    <Table.Row>
                        <Table.Cell>
                            {
                                item.website && 
                                <a href={item.website} target="_blank">{item.name}</a>
                            }
                            {
                                !item.website && 
                                <span>{item.name}</span>
                            }
                        </Table.Cell>
                        <Table.Cell>{item.title}</Table.Cell>
                        <Table.Cell>{item.address}</Table.Cell>
                        <Table.Cell>{item.mobile}</Table.Cell>
                        <Table.Cell>
                            {
                                item.specialities &&
                                <Popup
                                    content={item.specialities}
                                    wide
                                    trigger={
                                        <LinesEllipsis
                                            text={item.specialities}
                                            maxLine='5'
                                            ellipsis='...'
                                            trimRight
                                            basedOn='letters'
                                        />
                                    }
                                />
                            }
                        </Table.Cell>
                        <Table.Cell>{item.age}</Table.Cell>
                        <Table.Cell>{item.modality}</Table.Cell>
                        <Table.Cell>
                            {
                                item.community &&
                                <Popup
                                    content={item.community}
                                    trigger={
                                        <LinesEllipsis
                                            text={item.community}
                                            maxLine='5'
                                            ellipsis='...'
                                            trimRight
                                            basedOn='letters'
                                        />
                                    }
                                />
                            }
                        </Table.Cell>
                        <Table.Cell>
                            {
                                item.therapyType &&
                                <Popup
                                    content={item.therapyType}
                                    trigger={
                                        <LinesEllipsis
                                            text={item.therapyType}
                                            maxLine='5'
                                            ellipsis='...'
                                            trimRight
                                            basedOn='letters'
                                        />
                                    }
                                />
                            }
                        </Table.Cell>
                        <Table.Cell>
                            {
                                item.about &&
                                <Popup
                                    content={item.about}
                                    wide="very"
                                    trigger={
                                        <LinesEllipsis
                                            text={item.about}
                                            maxLine='2'
                                            ellipsis='...'
                                            trimRight
                                            basedOn='letters'
                                        />
                                    }
                                />
                            }
                        </Table.Cell>
                    </Table.Row>
                ))
            }
        </Table.Body>
    );
}



class TherapistTable extends React.Component {

    state = {
        offset: 0,
    }

    constructor() {
        super();
    }

    changeOffset(offset) {
        this.setState({offset: offset})
    }
    render() {
        const limit = 10
        if (this.props.data) {
            if (this.props.data.length > 0) {
                return (
                    <div style={{ marginTop: '30px' }}>
                        <Table celled>
                            <Table.Header>
                                <Table.Row>
                                    <Table.HeaderCell>Name</Table.HeaderCell>
                                    <Table.HeaderCell>Title</Table.HeaderCell>
                                    <Table.HeaderCell>Address</Table.HeaderCell>
                                    <Table.HeaderCell>Mobile</Table.HeaderCell>
                                    <Table.HeaderCell>Specialities</Table.HeaderCell>
                                    <Table.HeaderCell>Age</Table.HeaderCell>
                                    <Table.HeaderCell>Modality</Table.HeaderCell>
                                    <Table.HeaderCell>Community</Table.HeaderCell>
                                    <Table.HeaderCell>Therapy Type</Table.HeaderCell>
                                    <Table.HeaderCell>About</Table.HeaderCell>
                                </Table.Row>
                            </Table.Header>
                            <RenderBody 
                                rowData={this.props.data}
                                limit = {limit}
                                offset = {this.state.offset}
                            ></RenderBody>
                        </Table>

                        <TherapistPagination 
                            length = {this.props.data.length}
                            limit = {limit}
                            onMsg = {(offset) => this.changeOffset(offset)}
                        ></TherapistPagination>
                    </div>
                );
            } else {
                return (
                    <p>No therapist available</p>
                )
            }
        }

    }
}

export default TherapistTable;
