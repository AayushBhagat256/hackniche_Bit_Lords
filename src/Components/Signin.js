import React,{useState,useEffect} from 'react'
import './App.css';
import Salute from './salute.png'
import {Box,TextField,Typography,Button} from '@mui/material'
import Validation from './Validation';
import {
  Link
} from "react-router-dom";
import EmailIcon from '@mui/icons-material/Email';
import InputAdornment from '@mui/material/InputAdornment';
import LockIcon from '@mui/icons-material/Lock';

function Signin() {
      
        const container = document.querySelector(".container");

        const handleClick=()=>{
            container.classList.add("sign-up-mode")

        }
        const handleSignin=()=>{
            container.classList.remove("sign-up-mode");

        }
        const [inpval,setInpval]=useState({
          email:"",password:"",
      
       })
       const getdata=(e)=>{
      
         const {value,name}= e.target;
      
         setInpval(()=>{
           return {
             ...inpval,
             [name]:value
           }
         })
      
       }
       const [data,setData]=useState([])
      
       const addData=(e)=>{
         e.preventDefault();
         const getuserArr= localStorage.getItem("useryoutube");
         console.log(getuserArr);
         const {email,password}=inpval;
         setErrors(Validation(inpval));
                 setDataIsCorrect(true);
                 const newRecords={...inpval, id:new Date().getTime().toString()};
                 setRecords([...records,newRecords])
      
                 if(getuserArr && getuserArr.length){
                  const userdata=JSON.parse(getuserArr);
                  const userlogin= userdata.filter((el,k)=>{
                    return el.email===email && el.password===password
                  });
                  if(userlogin.length===0){
                    alert("This account doesn't exist!")
                  }
                  else{
                    console.log("User Login Successfully!")
                    // history("/Gridcomp")
                  }
                 }
      
       }
        const [isSignup,setIsSignup]= useState(false);
        const [inputs,setInputs]=useState({
                  email:"",password:"",
      
        });
      
        const [records,setRecords]=useState([]);
        const handlesubmit=(e)=>{
                  e.preventDefault();
                     
                  setErrors(Validation(inputs));
                  setDataIsCorrect(true);
                  const newRecords={...inputs, id:new Date().getTime().toString()};
                  setRecords([...records,newRecords])
      
        }
      
       
        
        const resetstate=()=>{
      
      
          setInputs({email:'',password:'',})
          setErrors({email:'',password:'',})
         
        }
        const [errors,setErrors]=useState({});
        
        const [dataIsCorrect, setDataIsCorrect]=useState(false);
      
        useEffect(()=>{
          if(Object.keys(errors).length===0 && dataIsCorrect) {
      
      
          }
         },[errors]);
     

  return (
        
    
    <div className="container">
      <div className="forms-container">
        <div className="signin-signup">
        <form  style={
          {color:"#4d84e2",
           maxWidth:"600px",
           maxHeight:"650px"
          }}
          onSubmit={handlesubmit}
          >
      
            <Typography variant="h4" style={{color:"#5a5a5a"}} textAlign="center">
             <strong>Log In</strong>
            </Typography>
            <TextField 
             id="input-with-icon-textfield"
             InputProps={{
               startAdornment: (
                 <InputAdornment position="start">
                   < EmailIcon/>
                 </InputAdornment>
               ),
             }}
             className="TextField-with-border-radius" fullWidth onChange={getdata} value={inpval.email} name="email" margin="normal" type={'email'} variant="outlined" placeholder="Email"/>
            {errors.email && <p className="error">{errors.email}</p>} 

            <TextField 
            id="input-with-icon-textfield"
            InputProps={{
              startAdornment: (
                <InputAdornment position="start">
                  < LockIcon/>
                </InputAdornment>
              ),
            }}
            className="TextField-with-border-radius" fullWidth onChange={getdata} value={inpval.password} name="password" margin="normal" type={'password'} variant="outlined" placeholder="Password"/>
            {errors.password && <p className="error">{errors.password}</p>}

           

            <Button  className="btn" onClick={addData} onChange={resetstate} type="submit" variant="contained" sx={{borderRadius:"30px", marginTop:"5px"}}>
              Log In
            </Button>
 
      </form>
        </div>
      </div>

      <div className="panels-container">
        <div className="panel left-panel">
          <div className="content">
            <p style={{color:"black"}}>
            "A hero is someone who has given his or her life to something bigger than oneself."
            </p>
            <h4>New here ?</h4>
            <Link to='/Signup' 
                style={{textDecoration:"none"}}
                > <button className="btn transparent" onClick={handleClick}  id="sign-in-btn"> Sign up</button>
                </Link> 
          </div>
          <img src={Salute} className="image" alt="No image seen" />
        </div>
     </div>
    </div>

  
  
  )
}

export default Signin