import React from 'react';
import Pagination from 'semantic-ui-react-button-pagination';


class TherapistPagination extends React.Component {
    constructor() {
        super();
        this.state = { offset: 0 };
    }

    handleClick(offset) {
        this.setState({ offset });
        this.props.onMsg(offset)
    }

    render() {
        return (
            <Pagination
                activePage={1}
                firstItem={null}
                lastItem={null}
                totalPages={this.props.length / this.props.limit}
                limit={this.props.limit}
                offset={this.state.offset}
                total={this.props.length}
                onClick={(e, props, offset) => this.handleClick(offset)}
            />
        );
    }
}

export default TherapistPagination;

