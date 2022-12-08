import React from 'react'
import { Tab } from 'semantic-ui-react'
import Basic from '../basic'
import Costomized from '../costomized'

const panes = [
  {
    menuItem: 'Basic Recommendation',
    render: () => (
      <Tab.Pane attached={false}>
        <Basic></Basic>
      </Tab.Pane>),
  },
  {
    menuItem: 'User Costomized Recommendation',
    render: () => (
      <Tab.Pane attached={false}>
        <Costomized></Costomized>
      </Tab.Pane>),
  },
]

const TabRecommendation = () => (
  <Tab menu={{ secondary: true, pointing: true }} panes={panes} />
)

export default TabRecommendation