import React, {setState} from 'react'
import FullCalendar from '@fullcalendar/react'
import dayGridPlugin from '@fullcalendar/daygrid'
import { CalendarApi } from '@fullcalendar/common'
// import interactionPlugin from '@fullcalendar/interaction'


export default class DemoApp extends React.Component {

  state = {
    currentEvents: [{ title: 'event 1', date: '2021-05-27T12:30:00'}]
  }

  updateEventNLP = (props) => {

    var { characterData } = props;
    // this.setState({
    //   currentEvents: this.state.currentEvents.concat({title: characterData.event, date: characterData.date})
      
    // })
    console.log(this.state.currentEvents)
    CalendarApi.addEvent({
      title: characterData.event,
      date: characterData.date
    })
  
  }

  render() {
    return (
      <FullCalendar
        plugins={[ dayGridPlugin ]}
        eventContent={renderEventContent}
        events={this.state.currentEvents}
      />
    )
  }
}

function renderEventContent(eventInfo) {
  return (
    <>
      <b>{eventInfo.timeText}</b>
      <i>{eventInfo.event.title}</i>
    </>
  )
}

const updateEventNLP = (props) => {
  var { characterData } = props;
  this.setState({
    currentEvents: this.state.currentEvents.concat({title: characterData.event, date: characterData.date})
    
  })
  console.log(this.state.currentEvents)


}
