import './App.css'; 
import axios from 'axios';
import React from 'react';


class App extends React.Component{
  state = { details: [], }

  componentDidMount(){
    let data;
    axios.get('http://localhost:8000/api/v1/books/')
    .then(res => {
      data = res.data;
      this.setState({
        details: data
      });
    })
    .catch(err => {
      console.log(err);
    })
  }
  render() {
    return(
      <div>
        <header>Data from Django</header>
        <hr></hr>
        {this.state.details.map((queryset, id) => (
          <div key={id}>
            <div>
              <h2>{queryset.title}</h2>
              <p>{queryset.author}</p>
            </div>
          </div> 
        ))}
      </div>
    )
  }
}

export default App;
