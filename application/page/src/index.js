import React from 'react'
import { createRoot } from 'react-dom/client';

import 'semantic-ui-css/semantic.min.css'
import './index.css'

import TabHead from "./component/tab";
import Header from "./component/header";
import Footer from './component/footer';


class App extends React.Component {
    render() {
        return (
            <div>
                <Header/>
                <div className="ui container main">
                    <TabHead/>
                </div>
                <Footer/>
            </div>
        );
    }
}


const container = document.getElementById('root');
const root = createRoot(container);
root.render(<App/>);