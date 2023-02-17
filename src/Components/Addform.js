import React, { useState } from 'react'
import axios from 'axios';
import { Token } from '@mui/icons-material';
// import * as fs from 'fs/promises';

function Addform() {
    const [title, setTitle] = useState('');
    const [author, setAuthor] = useState('');
    const [content, setContent] = useState('');
    const [status, setStatus] = useState('');
    const [image, setImage] = useState('');
    
    let token = localStorage.getItem("Token");
    console.log(token)
  
    const handleSubmit = (event) => {
      event.preventDefault();
      //var axios = require('axios');
var FormData = require('form-data');
//var fs = require('fs');
var data = new FormData();
data.append('picture', (image));
data.append('title', title);
data.append('author', author);
data.append('content', content);
data.append('status', parseInt(status));

var config = {
  method: 'post',
maxBodyLength: Infinity,
  url: 'http://127.0.0.1:8000/blog/bloglist/',
  headers: { 
    'Authorization': 'Token '+token, 
    'Cookie': 'csrftoken=CL9F2B4Csic4i8aKWfSdfJKNSwoevUrQ; sessionid=4or759omow7gdv8nffx4pvl6y3bv2hkj', 
    //...data.getHeaders()
  },
  data : data
};

axios(config)
.then(function (response) {
  console.log(JSON.stringify(response.data));
  alert("lets Siuu")
})
.catch(function (error) {
  console.log(error);
  alert("its not ok")
});

    }
  
    return (
      <form onSubmit={handleSubmit}>
        <label>
          Title:
          <input type="text" value={title} onChange={(event) => setTitle(event.target.value)} />
        </label>
        <label>
          Author's Email:
          <input type="email" value={author} onChange={(event) => setAuthor(event.target.value)} />
        </label>
        <label>
          Content:
          <textarea value={content} onChange={(event) => setContent(event.target.value)} />
        </label>
        <label>
          Status:
          <input type="text" value={status} onChange={(event) => setStatus(event.target.value)} />
        </label>
        <label>
          Image:
          <input type="file" onChange={(event) => setImage(event.target.files[0])} />
        </label>
        <button type="submit">Submit</button>
      </form>
    );
  }

export default Addform
