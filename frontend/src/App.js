import React, { useState } from "react";
import './App.css';

import Titlebar from './Components/Titlebar/Titlebar';
import Holdings from './Components/Holdings/Holdings';
import Suggesstions from './Components/Suggesstions/Suggesstions';
import NewsContainer from './Components/NewsContainer/NewsContainer';



function App() {

  const [user_credentials,set_user_credentials] = useState({
    'UserID':'Samyakjn18',
    'Password':'pass123'
  })

  const [newsDate,set_newsDate] = useState([])

  // const [Sentiment_result,set_Sentiment_result] = useState([])

  const [isSentiment_fetcing,set_isSentiment_fetcing] = useState(false);

  
  return (
    <div className="App-div">
      <Titlebar/>
      <div className = "App-body">
        <Suggesstions 
          newsDate = {newsDate} isloading = {isSentiment_fetcing}/>
        <Holdings user_credentials = {user_credentials} UpdateNewsData = {set_newsDate} 
                  Isfetching = {set_isSentiment_fetcing} />
      </div>
      <NewsContainer
        newsDate = {newsDate}/>
    </div>
  );
}

export default App;
